import os
import random
import shutil

img_dir = "ToothNumber_TaskDataset\images"
lbl_dir = "ToothNumber_TaskDataset\labels"
out_dir = "ToothNumber_TaskDataset"

splits = ["train", "val", "test"]
for split in splits:
    os.makedirs(os.path.join(out_dir, "images", split), exist_ok=True)
    os.makedirs(os.path.join(out_dir, "labels", split), exist_ok=True)

images = [f for f in os.listdir(img_dir) if f.endswith(".jpg")]
images.sort()

random.seed(42)
random.shuffle(images)

n = len(images)
train_end = int(0.8 * n)
val_end = int(0.9 * n)

train_files = images[:train_end]
val_files = images[train_end:val_end]
test_files = images[val_end:]

splits_dict = {"train": train_files, "val": val_files, "test": test_files}

for split, files in splits_dict.items():
    for img in files:
        base = os.path.splitext(img)[0]
        lbl = base + ".txt"

        img_src = os.path.join(img_dir, img)
        lbl_src = os.path.join(lbl_dir, lbl)

        img_dst = os.path.join(out_dir, "images", split, img)
        lbl_dst = os.path.join(out_dir, "labels", split, lbl)

        shutil.copy(img_src, img_dst)
        shutil.copy(lbl_src, lbl_dst)

print("✅ Dataset split completed!")
print(f"Train: {len(train_files)} | Val: {len(val_files)} | Test: {len(test_files)}")
