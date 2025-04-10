import cv2
from gesture_module import GestureRecognizer
from auth_module import FacialAuthenticator
from tts_module import MultilingualTTS

gesture_recognizer = GestureRecognizer("gesture_model.pth")
authenticator = FacialAuthenticator("authorized_user.jpg")
tts = MultilingualTTS()

cap = cv2.VideoCapture(0)
authenticated = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if not authenticated:
        authenticated = authenticator.authenticate(frame)
        if authenticated:
            tts.speak("Access granted", lang='en')
        continue

    gesture = gesture_recognizer.recognize(frame)
    if gesture is not None:
        gesture_text = f"Gesture {gesture} detected"
        print(gesture_text)
        tts.speak(gesture_text, lang='en')

    cv2.imshow("System", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

