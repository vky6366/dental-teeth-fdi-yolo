# 🦷 Tooth Detection & Numbering with YOLOv8

This project demonstrates how to train a YOLOv8 object detection model to detect and number teeth in panoramic dental X-rays using the FDI Tooth Numbering System. This task was developed as part of an internship assessment.

---

## 📂 Dataset

- **Images:** ~500 panoramic dental X-ray images  
- **Labels:** Provided in YOLO format:  
  ```
  class_id center_x center_y width height
  ```
- **Tooth Classes:** FDI numbering system (32 classes)
- **Split:**  
  - Train: 80%  
  - Validation: 10%  
  - Test: 10%

**Example file structure:**
```
/images/train/abc123.jpg
/labels/train/abc123.txt
```

---

## 🧩 Tooth Classes (FDI System)

| ID  | Tooth         |
|-----|--------------|
| 0   | Canine (13)  |
| 1   | Canine (23)  |
| 2   | Canine (33)  |
| 3   | Canine (43)  |
| 4   | Central Incisor (21) |
| ... | ...          |
| 31  | Third Molar (48) |

---

## ⚙️ Training Setup

- **Framework:** [Ultralytics YOLOv8](https://docs.ultralytics.com/)
- **Model:** yolov8s.pt (pretrained)
- **Image size:** 640×640
- **Epochs:** 100
- **Batch size:** 16
- **Hardware:** Tesla T4 GPU (Google Colab)

**Training command:**
```sh
yolo detect train data=data.yaml model=yolov8s.pt imgsz=640 epochs=100 batch=16
```

---

## 📊 Results

- **Precision:** 0.905
- **Recall:** 0.921
- **mAP@50:** 0.941
- **mAP@50-95:** 0.674

---

## 🖼️ Sample Predictions

Sample predictions with FDI numbering are available in the [`predictions/`](predictions/) directory.

---

## 📦 Repository Structure

- `data.yaml` &rarr; Dataset config (paths & classes)
- `best.pt` &rarr; Trained YOLOv8 weights
- `results.png` &rarr; Training curves
- `confusion_matrix.png` &rarr; Model confusion matrix
- `predictions/` &rarr; Sample predictions on test set

---

## 🚀 How to Use

### 1. Inference

Run detection on new X-rays:
```sh
yolo detect predict model=best.pt source=path/to/xray.jpg save=True
```

### 2. Validation

Evaluate on the test set:
```sh
yolo detect val model=best.pt data=data.yaml
```

---

## 📬 Contact

For questions or suggestions, please open an issue or discussion in this repository.

---