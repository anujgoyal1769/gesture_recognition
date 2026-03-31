"""
Hand Gesture Recognizer using OpenCV and MediaPipe
Author: Anuj Goyal
Description: Real-time hand gesture recognition using webcam
"""

import cv2
import mediapipe as mp
import math

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Gesture names mapped to finger states
GESTURES = {
    (0, 0, 0, 0, 0): "✊ Fist",
    (1, 1, 1, 1, 1): "🖐 Open Hand",
    (0, 1, 0, 0, 0): "☝ Point Up",
    (0, 1, 1, 0, 0): "✌ Peace / Victory",
    (1, 0, 0, 0, 1): "🤙 Call Me",
    (1, 1, 1, 1, 0): "🤟 Four Fingers",
    (0, 0, 0, 0, 1): "🤙 Pinky Up",
    (1, 0, 0, 0, 0): "👍 Thumbs Up",
    (0, 1, 1, 1, 1): "🤘 Four Fingers (no thumb)",
    (1, 1, 0, 0, 0): "👌 L-Shape",
}


def get_finger_states(hand_landmarks):
    """
    Returns a tuple of 5 values (thumb, index, middle, ring, pinky)
    1 = finger is UP / extended, 0 = finger is DOWN / folded
    """
    landmarks = hand_landmarks.landmark

    # Finger tip and pip (joint) landmark indices
    finger_tips = [4, 8, 12, 16, 20]
    finger_pips = [3, 6, 10, 14, 18]

    states = []

    # Thumb: compare x-coordinates (horizontal movement)
    if landmarks[finger_tips[0]].x < landmarks[finger_pips[0]].x:
        states.append(1)
    else:
        states.append(0)

    # Other fingers: compare y-coordinates (vertical movement)
    for i in range(1, 5):
        if landmarks[finger_tips[i]].y < landmarks[finger_pips[i]].y:
            states.append(1)
        else:
            states.append(0)

    return tuple(states)


def recognize_gesture(finger_states):
    """Returns the gesture name for the given finger states."""
    return GESTURES.get(finger_states, "🤔 Unknown Gesture")


def draw_info(frame, gesture_name, hand_count, fps):
    """Draws gesture info and FPS on the frame."""
    h, w, _ = frame.shape

    # Background box for text
    cv2.rectangle(frame, (0, 0), (w, 90), (0, 0, 0), -1)
    cv2.rectangle(frame, (0, 0), (w, 90), (0, 255, 100), 2)

    # Title
    cv2.putText(frame, "Hand Gesture Recognizer", (10, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 100), 2)

    # Gesture name
    cv2.putText(frame, f"Gesture: {gesture_name}", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    # FPS and hand count
    cv2.putText(frame, f"FPS: {fps:.0f}  |  Hands: {hand_count}", (10, 82),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 150, 150), 1)

    # Instructions at bottom
    cv2.putText(frame, "Press 'Q' to quit", (10, h - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 100, 255), 1)


def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    print("Hand Gesture Recognizer started!")
    print("Show your hand to the camera. Press 'Q' to quit.\n")

    import time
    prev_time = time.time()

    with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.5
    ) as hands:

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame.")
                break

            # Flip frame horizontally (mirror effect)
            frame = cv2.flip(frame, 1)

            # Convert BGR to RGB for MediaPipe
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            rgb_frame.flags.writeable = False
            results = hands.process(rgb_frame)
            rgb_frame.flags.writeable = True

            gesture_name = "No Hand Detected"
            hand_count = 0

            if results.multi_hand_landmarks:
                hand_count = len(results.multi_hand_landmarks)

                for hand_landmarks in results.multi_hand_landmarks:
                    # Draw landmarks on hand
                    mp_drawing.draw_landmarks(
                        frame,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style()
                    )

                    # Recognize gesture
                    finger_states = get_finger_states(hand_landmarks)
                    gesture_name = recognize_gesture(finger_states)

            # Calculate FPS
            curr_time = time.time()
            fps = 1 / (curr_time - prev_time + 1e-6)
            prev_time = curr_time

            # Draw info overlay
            draw_info(frame, gesture_name, hand_count, fps)

            cv2.imshow("Hand Gesture Recognizer", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Exiting...")
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
