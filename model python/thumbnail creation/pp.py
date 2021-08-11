import dlib
from PIL import Image
from skimage import io
import matplotlib.pyplot as plt


def numberOfFaces(image):
    face_detector = dlib.get_frontal_face_detector()
    detected_faces = face_detector(image, 1)
    return len(detected_faces))

def detect_faces(image):

    # Create a face detector
    face_detector = dlib.get_frontal_face_detector()

    # Run detector and get bounding boxes of the faces on image.
    detected_faces = face_detector(image, 1)
    face_frames = [(x.left(), x.top(),
                    x.right(), x.bottom()) for x in detected_faces]
    face=[]
    for n, face_rect in enumerate(face_frames):
        face.append(Image.fromarray(image).crop(face_rect))
    
    
    return face


img_path = 'text.jpg'
image = io.imread(img_path)
face=detect_faces(image)
plt.imshow(face[0])
print(numberOfFaces(image))
