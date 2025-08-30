from ultralytics import YOLO
import cv2

model = YOLO("runs/detect/train4/weights/best.pt")

results = model("test_image.jpg", conf=0.5)

detections = []
for r in results:
    boxes = r.boxes.xywh.cpu().numpy()
    classes = r.boxes.cls.cpu().numpy()
    confs = r.boxes.conf.cpu().numpy()
    for (x,y,w,h), cls_id, conf in zip(boxes, classes, confs):
        detections.append({"x":x,"y":y,"w":w,"h":h,"cls":int(cls_id),"conf":float(conf)})

y_mid = sum([d["y"] for d in detections]) / len(detections)
upper = sorted([d for d in detections if d["y"] < y_mid], key=lambda d: d["x"])
lower = sorted([d for d in detections if d["y"] >= y_mid], key=lambda d: d["x"])

for i, d in enumerate(upper, start=11): d["FDI"] = i
for i, d in enumerate(lower, start=31): d["FDI"] = i

img = cv2.imread("test_image.jpg")
for d in detections:
    x1,y1 = int(d["x"]-d["w"]/2), int(d["y"]-d["h"]/2)
    x2,y2 = int(d["x"]+d["w"]/2), int(d["y"]+d["h"]/2)
    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
    cv2.putText(img, f"{d['FDI']}", (x1,y1-5), cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
cv2.imwrite("post_processed.jpg", img)
