## Training Data Analysis and Potential Improvement
To objectively evaluate the model's performance, multiple mercies are adopted in the training process, for example, mAP50, mAP50-90, class loss, and box loss. Below are the graphs of each metric over time.
![result](Graphs/results.png)

As seen in the graphs, while the loss calculations for the training dataset continue to decline, the validation dataset has already stabilized and converged to a value by the time of the 70th epoch. Even though the graphical representation of the values indicates a good learning slope, there is a potential overfitting concern with the current training configuration. Moreover, mAP50 is widely considered one of the most reliable indicators of the overall performance of an image recognition model. In this case, it levels off around 0.6 by the end of the training, suggesting that a moderate accuracy has been achieved and yet, there is still room for improvement.

![f1_curve](Graphs/F1_curve.png)
While mAP50 and other loss calculations are significant in model training, the F1 vs, Confidence threshold curve also conveys important messages about the model. The F1 score represents the level of excellence in balancing Recall and Precision, a higher score is usually preferred and vice versa. In the curve above, the model exhibits low confidence when the F1 score is high and high confidence when the F1 is low or sometimes nearly 0. This result is not ideal and needs to be improved later on. 

Due to the lack of resources and time constraints of the project, here are some suggestions regarding next steps or approaches that enhance the model. 
- Enlarge the data sample size which directly allows the model to be more familiar with the object hotdog.
- Employ another YOLO v8 model (n, s, m, l, x)
- Further optimize hyperparameters (e.g. learning rate, batch size, weight decay, optimizer)
- Increase the number of epochs in the training loop and extend the training iterations to collect more data.