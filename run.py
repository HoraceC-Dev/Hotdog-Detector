from src.display import detection_display

from ultralytics import YOLO
def main():
    # Define the path/url to the image
    img_path = input("Please enter the url/path of the image:")

    directory_to_store_model = r'model\YOLO_hotdog_model.pt'
    model = YOLO(directory_to_store_model)
    
    # Process the image with the retrieved model then display the result
    detection_display(model, img_path)


if __name__ == "__main__":
    main()
