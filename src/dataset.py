import os
from datasets import Dataset
from transformers import AutoImageProcessor
from PIL import Image

DATA_DIR = "data/Covid-19_Radiography_Dataset"

def load_covid_dataset(data_dir: str):
    class_names = []

    for name in os.listdir(data_dir):
         if os.path.isdir(os.path.join(data_dir, name)):
              class_names.append(name)

    class_names.sort()

    class_labels = {name : i for i, name in enumerate(class_names)}

    res = []

    for name in class_names:
        folder = os.path.join(data_dir, name)

        for current_folder, subfolders, filenames in os.walk(folder):
             for filename in filenames:
                  if filename.lower().endswith((".png", ".jpeg", ".jpg")):
                       res.append({"image_path" : os.path.join(current_folder, filename), "label" : class_labels[name]})

if __name__ == "__main__":
     load_covid_dataset(DATA_DIR)