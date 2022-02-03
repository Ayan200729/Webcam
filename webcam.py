from ast import While
from distutils.command.upload import upload
from tkinter import Frame
from tkinter.tix import Tree
import cv2 
import time
import dropbox
import random
start_time = time.time()

def takeSnapshort():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):

        ret, frame = videoCaptureObject.read()
        imgName = "img"+str(number) + ".png"
        cv2.imwrite(imgName, frame)
        start_time = time.time
        result = False

    return imgName
    print("Snapshot taken..")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(imgName):
    access_token = "sl.BBAgBCs1JDlB4vQFjpUh4yEOpqdzjm2HK8ZkYdbhFN56Iui0OyMtMEEXd5UqMCWTUlbVoDExK3hR0unYhDgWjjTjmj98DF_rwdy-GwFt9NY_k_BO6oCNV71HDKcBZK_D6AaER0wz_i0"
    file = imgName
    file_from = file
    file_to = "/NewFolder1/"+(imgName)
    dbx = dropbox.Dropbox(access_token)
    
    with open(file_from, "rb") as f :
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.ovrewrite)
        print("file_uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=300):
            name = takeSnapshort()
            upload_file(name)

main()

