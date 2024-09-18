import cv2
import matplotlib.pyplot as plt

def detection_display(model,path):
    results = model(path)

    for result in results:
        # Extract bounding boxes and class names from the result object
        boxes = result.boxes  # This contains the bounding box coordinates
        names = result.names  # Class names dictionary (e.g., {0: 'hotdog'})

        # Convert the original image back to OpenCV format
        img = result.orig_img

        # Loop through the detected boxes
        for box in boxes:
            # Extract the coordinates of the bounding box
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()  # Convert to numpy array if necessary
            conf = float(box.conf.cpu().numpy())  # Convert the confidence score to a scalar (float)

            # Get the class name using the class ID
            class_id = int(box.cls.cpu().numpy())
            class_name = names[class_id]

            # Draw the bounding box and class label on the image
            cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(img, f'{class_name} {conf:.2f}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        # Display the image with bounding boxes and labels
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.axis('off')  # Hide axes

