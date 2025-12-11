# import cv2
# from ultralytics import YOLO
# import numpy as np
# yolo=YOLO('yolov8s-pose.pt')
# results=yolo('/mnt/d/image/mom.jpg',conf=0.65)
# print(results[0].keypoints.data.shape)
# print(type(results))
# img=results[0].orig_img
# print(results[0].boxes.shape)
# print(type(results[0].boxes))
# xy_boxes=results[0].boxes.xyxy.cpu().numpy()
# conf_boxes=results[0].boxes.conf.cpu().numpy()
# cls_boxes=results[0].boxes.cls.cpu().numpy()
# for i in range(len(xy_boxes)):
#     x1,y1,x2,y2=map(int,xy_boxes[i])
#     conf=conf_boxes[i]
#     cls=cls_boxes[i]
#     cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
#     cv2.putText(img,f'conf:{conf:.2f} cls{cls}',(x2,y2),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
# cv2.imshow('result',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# import cv2
# Linux 下通常是 0，但也可能是 1 或 2，取决于挂载顺序
# cap = cv2.VideoCapture('http://172.20.10.3:4747/video') 

# if not cap.isOpened():
#     print("❌ 无法打开摄像头！请检查 /dev/video0 是否存在，或权限是否正确。")
# else:
#     print("✅ 摄像头连接成功！")
#     ret, frame = cap.read()
#     if ret:
#         print(f"当前帧尺寸: {frame.shape}")
#         # 在 Linux 服务器/WSL 调试建议直接保存图片查看，比配 X11 转发更稳
#         cv2.imwrite("test_linux_cam.jpg", frame) 
#         print("📸 已保存测试图至 test_linux_cam.jpg")

# cap.release()


