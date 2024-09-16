# Hotdog Detector

This project leverages the pre-existing YOLO v8n model to build a Hotdog Detector by fine-tuning it with a dataset of approximately 3,000 images and corresponding labels. The model undergoes supervised learning in an attempt to maximize its capability and feature extraction tailored to hotdogs. Hyperparameters such as batch size, learning rate, patience tolerance, and weight decay are tested and well-tuned. As a result, the model is capable of correctly identifying one or more hotdogs in a given image.


## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Results](#results)


## Installation
To set up this project on your local machine, follow these steps:

1. Navigate to the project directory:
   ```bash
   cd path-to-your-folder
   ```
2. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
## Usage
Once the project is set up, you can either train the model with the source code or use the trained Hotdog Detector to identify hotdogs in your images.
#### 1. Train a model
After install all the dependency, please 
run the main.py file(GPU is highly recommended).
```bash
python your-path/main.py
```

#### 2.Identify hotdogs
Before starting the identification process, please provide either a URL or a path to the image and assign it to the img_path variable in the main function in run.py:
```python
    img_path = "paste your path here"
```



   
