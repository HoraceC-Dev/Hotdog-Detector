# Pre-trained model fine-tuning
def model_training(selected_model, root):

    # The selected pre-trained model
    model = selected_model
    
    result = model.train(
        data=f'{root}/data.yaml',  # path to your data.yaml file
        epochs=70,        # number of training epochs
        imgsz=640,         # image size
        patience=15,       # early stopping patience
        weight_decay=5e-4, # weight_decay
        lr0= 0.003,        # learning rate
        batch=32,          # batch size
        device='0',        # GPU ID 
    )
    
    # Return the model and the training data (mAP, cls_loss...etc)
    return model, result