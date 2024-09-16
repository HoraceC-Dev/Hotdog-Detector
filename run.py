from ultralytics import YOLO

from model import YOLO_hotdog_model
from src.display import detection_display


def main():
    # Define the path/url to the image
    img_path = "path/url"

    # Retrieve the trained model
    model = YOLO(YOLO_hotdog_model)

    # Process the image with the retrieved model then display the result
    detection_display(model, img_path)


if __name__ == "__main__":
    main()
