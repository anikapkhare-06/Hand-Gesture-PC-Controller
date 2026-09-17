import cv2
import mediapipe as mp
import pyautogui
import math
import time

# ---------------------------------------
# SCREEN SIZE
# ---------------------------------------

screen_width, screen_height = pyautogui.size()

# ---------------------------------------
# MEDIAPIPE INITIALIZATION
# ---------------------------------------

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(
        model_asset_path="hand_landmarker.task"
    ),
    running_mode=VisionRunningMode.IMAGE,
    num_hands=1,
    min_hand_detection_confidence=0.5,
    min_hand_presence_confidence=0.5,
    min_tracking_confidence=0.5
)

# ---------------------------------------
# HELPER FUNCTION
# ---------------------------------------

def distance(p1, p2):
    return math.sqrt(
        (p1.x - p2.x) ** 2 +
        (p1.y - p2.y) ** 2
    )


def finger_up(landmarks, tip, pip):
    return landmarks[tip].y < landmarks[pip].y


# ---------------------------------------
# CAMERA
# ---------------------------------------

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: Webcam could not be opened.")
    exit()

# ---------------------------------------
# VARIABLES
# ---------------------------------------

previous_x = 0
previous_y = 0

last_click_time = 0
click_delay = 0.8

# ---------------------------------------
# HAND LANDMARKER
# ---------------------------------------

with HandLandmarker.create_from_options(options) as landmarker:

    while True:

        success, frame = cap.read()

        if not success:
            print("ERROR: Could not read webcam.")
            break

        # Mirror image
        frame = cv2.flip(frame, 1)

        # Convert OpenCV BGR → RGB
        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        # Convert to MediaPipe Image
        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame
        )

        # Detect hand
        result = landmarker.detect(mp_image)

        gesture = "No Hand Detected"

        # ---------------------------------------
        # IF HAND DETECTED
        # ---------------------------------------

        if result.hand_landmarks:

            landmarks = result.hand_landmarks[0]

            # Draw landmarks
            for landmark in landmarks:

                x = int(landmark.x * frame.shape[1])
                y = int(landmark.y * frame.shape[0])

                cv2.circle(
                    frame,
                    (x, y),
                    5,
                    (0, 255, 0),
                    -1
                )

            # Draw connections manually
            connections = [
                (0, 1), (1, 2), (2, 3), (3, 4),
                (0, 5), (5, 6), (6, 7), (7, 8),
                (5, 9), (9, 10), (10, 11), (11, 12),
                (9, 13), (13, 14), (14, 15), (15, 16),
                (13, 17), (17, 18), (18, 19), (19, 20),
                (0, 17)
            ]

            for start, end in connections:

                x1 = int(landmarks[start].x * frame.shape[1])
                y1 = int(landmarks[start].y * frame.shape[0])

                x2 = int(landmarks[end].x * frame.shape[1])
                y2 = int(landmarks[end].y * frame.shape[0])

                cv2.line(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (255, 0, 0),
                    2
                )

            # ---------------------------------------
            # FINGER DETECTION
            # ---------------------------------------

            index_up = finger_up(landmarks, 8, 6)
            middle_up = finger_up(landmarks, 12, 10)
            ring_up = finger_up(landmarks, 16, 14)
            pinky_up = finger_up(landmarks, 20, 18)

            # Thumb-index distance
            thumb_index_distance = distance(
                landmarks[4],
                landmarks[8]
            )

            # ---------------------------------------
            # LEFT CLICK
            # ---------------------------------------

            if thumb_index_distance < 0.05:

                gesture = "LEFT CLICK"

                current_time = time.time()

                if current_time - last_click_time > click_delay:

                    pyautogui.click()

                    last_click_time = current_time

            # ---------------------------------------
            # RIGHT CLICK
            # ---------------------------------------

            elif (
                index_up
                and middle_up
                and not ring_up
                and not pinky_up
            ):

                gesture = "RIGHT CLICK"

                current_time = time.time()

                if current_time - last_click_time > click_delay:

                    pyautogui.rightClick()

                    last_click_time = current_time

            # ---------------------------------------
            # MOVE MOUSE
            # ---------------------------------------

            elif (
                index_up
                and not middle_up
                and not ring_up
                and not pinky_up
            ):

                gesture = "MOVE"

                index_x = landmarks[8].x
                index_y = landmarks[8].y

                target_x = int(
                    index_x * screen_width
                )

                target_y = int(
                    index_y * screen_height
                )

                # Smooth movement
                smooth_x = int(
                    0.7 * previous_x +
                    0.3 * target_x
                )

                smooth_y = int(
                    0.7 * previous_y +
                    0.3 * target_y
                )

                pyautogui.moveTo(
                    smooth_x,
                    smooth_y,
                    duration=0.01
                )

                previous_x = smooth_x
                previous_y = smooth_y

            # ---------------------------------------
            # OPEN PALM
            # ---------------------------------------

            elif (
                index_up
                and middle_up
                and ring_up
                and pinky_up
            ):

                gesture = "OPEN PALM - STOP"

            # ---------------------------------------
            # FIST
            # ---------------------------------------

            elif (
                not index_up
                and not middle_up
                and not ring_up
                and not pinky_up
            ):

                gesture = "FIST"

            else:

                gesture = "UNKNOWN"

        # ---------------------------------------
        # DISPLAY GESTURE
        # ---------------------------------------

        cv2.rectangle(
            frame,
            (10, 10),
            (380, 65),
            (0, 0, 0),
            -1
        )

        cv2.putText(
            frame,
            "Gesture: " + gesture,
            (20, 48),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (0, 255, 0),
            2
        )

        # Instructions
        cv2.putText(
            frame,
            "Q = Exit",
            (20, frame.shape[0] - 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2
        )

        # Show webcam
        cv2.imshow(
            "Hand Gesture Based PC Controller",
            frame
        )

        # ---------------------------------------
        # EXIT
        # ---------------------------------------

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


# ---------------------------------------
# RELEASE
# ---------------------------------------

cap.release()
cv2.destroyAllWindows()

print("Program closed successfully.")