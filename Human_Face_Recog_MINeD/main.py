import cv2
import face_recognition
import numpy as np
import os
import pandas as pd
from datetime import datetime
# from numba import jit, cuda
import numpy as np
# to measure exec time
from timeit import default_timer as timer

def fdr():
    
    path="known_faces"
    images=[]
    classNames = []
    mylist=os.listdir(path)
    print(mylist)

    for cls in mylist:
        curImg=cv2.imread(f"{path}/{cls}")
        images.append(curImg)
        classNames.append(os.path.splitext(cls)[0])

    print(classNames)
    print(len(images))

    def find_encodings(images):
        encoding_list=[]
        for img in images:
            img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            encode=face_recognition.face_encodings(img)[0]
            encoding_list.append(encode)
            
        return encoding_list

    #import csv
    def markAttendance(name):
        with open('Attendance.csv','r+') as f:
            myDataList=f.readlines()
            nameList=[]
            #print(myDataList)
            for line in myDataList:
                entry=line.split(',')
                nameList.append(entry[0])

            #csv_dict = [row for row in csv.DictReader(f)]
            
            if name not in nameList:
                now =datetime.now()
                dtString= now.strftime('%H:%M:%S')
                dtDate=now.strftime('%Y-%m-%d')
                f.writelines(f'\n{name},{dtDate},{dtString}')
                                    
            
  

    encodelist_knownfaces = find_encodings(images)
    print(len(encodelist_knownfaces))

    print("Encoding Completed!!!!!!")

    def detect():
        vc=cv2.VideoCapture('VID_20230302_170157.mp4')
        frame=1
        with open('Attendance.csv','w+') as f:
            f.writelines('Employee Id, Date , Time ')

        while True:
            success,img=vc.read()
            if(frame%25==0):
                imgs=cv2.resize(img,(0,0),None,0.25,0.25)
                imgs=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                faces_curframe= face_recognition.face_locations(imgs)
                encode_curframe = face_recognition.face_encodings(imgs,faces_curframe)

                for encodeFace,faceLoc in zip(encode_curframe,faces_curframe):
                    matches=face_recognition.compare_faces(encodelist_knownfaces,encodeFace)
                    faceDis=face_recognition.face_distance(encodelist_knownfaces,encodeFace)
                    
                    value=min(faceDis)
                    acc=1-value
                    acc=acc*100
                    matchIndex=np.argmin(faceDis)
                    if(value<0.5):
                        if(matches[matchIndex]):
                            name=classNames[matchIndex].upper()
                            print(faceDis)
                            print(name)
                            y1,x2,y2,x1=faceLoc
                            y1,x2,y2,x1= y1*4,x2*4,y2*4,x1*4
                            cv2.rectangle(img,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(0,255,0),4)
                            cv2.rectangle(img,(faceLoc[3],faceLoc[2]-10),(faceLoc[1],faceLoc[2]),(0,255,0),cv2.FILLED)
                            names=name+" "+str(round(acc,2))+"%"
                            cv2.putText(img,names,(faceLoc[3]+6,faceLoc[2]-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),4)
                            markAttendance(name)
                    else:
                        cv2.rectangle(img,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(0,255,0),4)
                        cv2.rectangle(img,(faceLoc[3],faceLoc[2]-10),(faceLoc[1],faceLoc[2]),(0,255,0),cv2.FILLED)
                        names="Unknown"
                        cv2.putText(img,names,(faceLoc[3]+6,faceLoc[2]-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)

                cv2.namedWindow('Video',cv2.WINDOW_NORMAL)
                cv2.resizeWindow('Video',600,1000)
                cv2.imshow('Video',img)
            
            frame=frame+1        
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                vc.release()
                break
        vc.release()
    
        

    detect()
