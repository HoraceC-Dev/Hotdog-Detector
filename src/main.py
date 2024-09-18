from ultralytics import YOLO

from src.utils import retrieve_dataset, create_data_yaml_f
from src.training import model_training


def main():
    
    # Define the directory to hold the dataset
    directory_to_store_dataset = "path"

    # Download the dataset and store it for trianing
    retrieve_dataset(directory_to_store_dataset)

    # Create a yaml file for YOLO model configuration
    create_data_yaml_f(directory_to_store_dataset)
    
    # Get the model after fine-tuning
    model, _result = model_training(YOLO('yolov8s.pt'),directory_to_store_dataset)

    # Define the location to store the model
    directory_to_store_model = "path"

    # Save the model
    model.save(directory_to_store_model)

if __name__ == "__main__":
    main()
