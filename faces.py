import cv2

size = 2
webcam = cv2.VideoCapture(0)   # Use camera 0
classifier = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
while True:
    (rval, im) = webcam.read()
    im=cv2.flip(im,1,0)         #Flip to act as a mirror
    mini = cv2.resize(im, (im.shape[1] / size, im.shape[0] / size))
    faces = classifier.detectMultiScale(mini)
    for f in faces:
        (x, y, w, h) = [v * size for v in f]    #Scale the shapesize backup
        cv2.rectangle(im, (x, y), (x + w, y + h),(0,255,0),thickness=4)
    cv2.imshow('OpenCV', im)
    key = cv2.waitKey(10)
    if key == 27: #The Esc key
        break