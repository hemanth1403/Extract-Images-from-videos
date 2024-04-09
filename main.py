import cv2
import os

path = os.getcwd()
# print(path)

try:
    videoName = input("Enter the video name : ").split(".")
    imgPerSec = int(input("Enter the no of images per second : "))

    # print(os.path.dirname(videoName[0]))
    cap = cv2.VideoCapture(os.path.abspath(videoName[0]+"."+videoName[1]))
    # print(os.path.abspath(videoName[0]+"."+videoName[1]))
    directory = os.path.abspath(videoName[0])
    fps = cap.get(cv2.CAP_PROP_FPS)
    os.mkdir(videoName[0])
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
except:
    print("Please check the format")

# If the video file more than 200 mb then use this terminal command 
# ffmpeg -i input.mp4 -r 30/1 out-%03d.png 
    # (input)    (30 frames per second)
