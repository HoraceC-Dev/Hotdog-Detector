import gdown
import os
import shutil
import zipfile
import yaml
from ultralytics import YOLO

def retrieve_dataset(local_directory):
    # Create a local directory to store the provided datasets
    output_path = local_directory  

    # Check if the directory already exists
    if os.path.exists(output_path):
        # If the directory exists, remove it and its contents to ensure a fresh start
        shutil.rmtree(output_path)

    # Create a new, empty directory to store the downloaded datasets
    os.makedirs(output_path)

    url = "https://drive.google.com/drive/folders/1UoM2fdY9uALEiuDtHyTwNU3ldgD1l6oB"

    # Download the folder and store it in the output path
    gdown.download_folder(url, output=output_path, quiet=True)

    # List all the files that were downloaded into the 'output_path' directory
    list_of_files = os.listdir(output_path)

    # Loop through the list of files to unzip each one and clean up
    for filename in list_of_files:
        file_path = os.path.join(output_path, filename)

        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(output_path)
        
        os.remove(file_path)




def create_data_yaml_f(root):

    data = {
        'path': f'{root}/Hot Dog Detection YOLO',
        'train': 'train/images',
        'val': 'valid/images',
        'nc': 1,
        'names': ['hotdog'],
        'train_labels':'train/labels',
        'valid_labels': 'valid/labels'
    }

    # Write the YAML file
    with open(f'{root}/data.yaml', 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

def retrieve_model(path):
    if not os.path.exists(path):

        # Create the download URL
        url = 'https://drive.google.com/file/d/1LXxkSa_AdG_tUTDLpAdysZltsivvgWzq/view?usp=drive_link'
        
        # Download the model
        gdown.download(url, path, quiet=True)

    return YOLO(path)