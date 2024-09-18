# Hotdog Detector

This project aims to develop a Hotdog Detector leveraging a pre-existing model YOLO v8n. The pre-trained model is fine-tuned with a dataset of approximately 3,000 images and corresponding labels. Specifically, supervised learning enables the model to tailor its detection capability and feature extraction to hotdogs, thereby optimizing the algorithm for single object detection. Additionally, hyperparameters such as batch size, learning rate, patience tolerance, and weight decay are tested and well-tuned. As a result, the after-trained model can correctly identify one or more hotdogs in a given image. 

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)


## Installation
To set up this project on your local machine, follow these steps:

1. Navigate to the project directory:
   ```bash
   cd path-to-your-folder
   ```
2. Clone the repository: (Skip this step if you already have the ZIP file.)
   ```bash
   git clone https://github.com/PmmerHc/Hotdog-Detector.git
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Once the project is set up, you can either train the model with the source code or use the trained Hotdog Detector to identify hotdogs in your images.
#### 1. Train a model
After installing all the dependencies, please set the path of your working directory in the directory_to_store_dataset variable in main.py within the src folder. Additionally, choose a directory to store the model after training and assign its path to the directory_to_store_model variable in main.py within the src folder.

Lastly, run the main.py file to begin the training. (Note: The use of a GPU is highly recommended.)
```bash
python your-directory/main.py
```

#### 2. Identify hotdogs
Before starting the identification process, please prepare either a URL or a path to the image.

Then, run the run.py file. 
```bash
python your-directory/run.py
```
After a few moments, it will request user to input the url/path of the image. 

A pictures with bounding boxes will pop-up in a few seconds. 
