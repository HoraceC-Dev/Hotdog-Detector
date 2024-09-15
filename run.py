from ultralytics import YOLO

from model import YOLO_hotdog_model
from src.display import detection_display


def main():
    img_path = "path"
    
    model = YOLO(YOLO_hotdog_model)

    detection_display(model, img_path)


if __name__ == "__main__":
    main()
