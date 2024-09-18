from src.display import detection_display
from src.utils import retrieve_model

def main():
    # Define the path/url to the image
    directory_to_store_model = ''

    img_path = "path/url"

    # Retrieve the trained model
    model = retrieve_model(directory_to_store_model) 
    

    # Process the image with the retrieved model then display the result
    detection_display(model, img_path)


if __name__ == "__main__":
    main()
