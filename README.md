# Hotdog Detector

This project leverages the pre-existing YOLO v8n model to build a Hotdog Detector by fine-tuning it with a dataset of approximately 3,000 images and corresponding labels. The model undergoes supervised learning in an attempt to maximize its capability and feature extraction tailored to hotdogs. Hyperparameters such as batch size, learning rate, patience tolerance, and weight decay are tested and well-tuned. As a result, the model is capable of correctly identifying one or more hotdogs in a given image.


## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Model Training Data Analysis](#model-training-data-analysis)


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
After installing all the dependencies, please set the path of your working directory in the directory_to_store_dataset variable in main.py within the src folder. Additionally, choose a directory to store the model after training and assign its path to the directory_to_store_model variable in main.py within the src folder.

Lastly, run the main.py file to begin the training. (Note: The use of a GPU is highly recommended.)
```bash
python your-path/main.py
```

#### 2.Identify hotdogs
Before starting the identification process, please provide either a URL or a path to the image and assign it to the img_path variable in the main function in run.py:
```python
    img_path = "paste your path here"
```

Then, run the run.py file. 

## Model Training Data Analysis
To objectively evaulate model's performance, multiple metrcies are adopted throughout the training process, including mAP50, mAP50-90, class loss, and box loss. Below are the graphs of each individual metrics over time.
![result](Graphs/results.png)

As seen in the graphs, while the metrics for the training dataset continue to decline, the validation dataset has already stabilized and converged to a value at the 70th epochs. The mAP50 index of the validation dataset seemingly level off around 0.6 at the end of the training, indicating a moderate accuracy has been achieved and yet, there is room for improvement. 

![f1_curve](Graphs/F1_curve.png)
The F1 vs. Confidence Threshold curve illustrates a phenomenon where the model exhibits lower confidence when the F1 score is high, and vice versa. This highlights a concern of the current model being unable to balance Recall and Precision at the same time.  

Here is a list of potential enhancement for the model but have not been implemented yet due to either the lack of resources or time constraints:
- Enlarge the data smaple size
- Employ another YOLO v8 model (n, s, m, l, x)
- Further optimize hyperparameters (e.g. learning rate, batch size, weight decay, optimizer)
- Incraese the number of epochs

   
