# Extract-Images-from-videos


A simple python script to extract images from videos 

Here we are maily using 

Opencv and os

- opencv for extracting images and saving.

- Os for creating the directory and saving the images in the respective path.

1. Importing the libraries  
```python
import cv2
import os
```

2. Taking the input of the video and no of frames we want per-second to be extracted

```python
videoName = input("Enter the video name : ").split(".")
imgPerSec = int(input("Enter the no of images per second : "))
```

3. Passing the video to the openCV and getting the path of the video and making a directory to store the images
```python
cap = cv2.VideoCapture(os.path.abspath(videoName[0]+"."+videoName[1]))
directory = os.path.abspath(videoName[0])
fps = cap.get(cv2.CAP_PROP_FPS)
os.mkdir(videoName[0])
```
4. Finally we are extracting the no of frames that we want from the video

```python
n = 0
c = 0
while True:
    ret, frame = cap.read()
    if (imgPerSec*n) % (fps) == 0:
        cv2.imwrite(f"{directory}/{c}.jpg", frame)
        c += 1
    n += 1
    if ret == False:
        break
cap.release()
cv2.destroyAllWindows()
```


