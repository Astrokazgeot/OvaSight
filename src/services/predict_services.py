from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing import image
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


model_path = os.path.join(project_root, "artifacts", "pcos_cnn_model.h5")
model=load_model(model_path)

def predict_pcos(image_path):
    img = image.load_img(image_path, target_size=(180, 180))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0][0]
    result = "PCOS" if prediction >= 0.5 else "Normal"
    ovulation_status = "Not Ovulating" if result == "PCOS" else "Ovulating"
    return result, ovulation_status
