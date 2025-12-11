from geometry import Squatcounter
import cv2
from ultralytics import YOLO
import numpy as np

model=YOLO('yolov8s-pose.pt')
cap=cv2.VideoCapture('http://172.20.10.3:4747/video')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
counter=Squatcounter(180)
if not cap.isOpened():
    print('Not Found')
    exit()

while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        #对这一帧画面经行计数
        results=model(frame,conf=0.65)
        #我们只统计第一个人的下蹲记录
        xy_boxes=results[0].boxes.xyxy.cpu().numpy()#人所在框
        if len(xy_boxes)==0:
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            continue
        keypoints_all=results[0].keypoints.data.cpu().numpy()
        keypoints=list()#分别对应髋，膝，踝
        for i in range(3):
            keypoints.append(keypoints_all[0,12+i*2,:2])
        x1,y1,x2,y2=map(int,xy_boxes[0])
        #接下来进行人框绘制和特征点标注
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
        for i in range(3):
            x,y=map(int,keypoints[i])
            cv2.circle(frame,(x,y),5,(255,0,0),5)
        counter.update_angle(keypoints[1],keypoints[0],keypoints[2])
        counter.state_machine()
        cv2.putText(frame,f'counts:{counter.count}',(20,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
    


        
        
        