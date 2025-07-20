import os

def count_images_in_folder(folder_path):
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
    count = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(image_extensions):
                count += 1
    return count


folder = "artifacts/valid"  
total_images = count_images_in_folder(folder)
print(f"Total images in '{folder}':", total_images)
