from PIL import Image
import os

def find_broken_images(root_folder):
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            path = os.path.join(root, file)
            try:
                img = Image.open(path)
                img.verify()
            except Exception as e:
                print(f"Corrupt or unreadable image: {path}")

find_broken_images("artifacts/train")
find_broken_images("artifacts/val")
find_broken_images("artifacts/test")
