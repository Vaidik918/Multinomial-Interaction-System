# auth_module.py
from deepface import DeepFace
import cv2
import tempfile

class FacialAuthenticator:
    def __init__(self, reference_img_path):
        self.reference_img_path = reference_img_path

    def authenticate(self, frame):
        _, temp_path = tempfile.mkstemp(suffix=".jpg")
        cv2.imwrite(temp_path, frame)
        try:
            result = DeepFace.verify(temp_path, self.reference_img_path, model_name='Facenet')
            return result['verified']
        except:
            return False

