import cv2
from ultralytics import YOLO
import numpy as np
yolo=YOLO('yolov8s-pose.pt')
results=yolo('/mnt/d/image/mom.jpg',conf=0.65)
print(results[0].keypoints.data.shape)
print(type(results))
img=results[0].orig_img
print(results[0].boxes.shape)
print(type(results[0].boxes))
xy_boxes=results[0].boxes.xyxy.cpu().numpy()
conf_boxes=results[0].boxes.conf.cpu().numpy()
cls_boxes=results[0].boxes.cls.cpu().numpy()
for i in range(len(xy_boxes)):
    x1,y1,x2,y2=map(int,xy_boxes[i])
    conf=conf_boxes[i]
    cls=cls_boxes[i]
    cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
    cv2.putText(img,f'conf:{conf:.2f} cls{cls}',(x2,y2),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
cv2.imshow('result',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


