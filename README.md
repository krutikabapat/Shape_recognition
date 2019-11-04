# Shape_recognition
Deep Learning based Shape detection and counting.  

## Problem statement
Count or segment the number of Images in the test data, which contains the images of flowchart which has various shapes like
rectangle, square, circle, rhombus and ellipse.   

## Solution
Since we need the number of figures of each type in each flowchart, it is a localization and detection probelem and we have to solve it using object detection methods, which generates boundig box for each of the shape and total number of shapes of each category can be counted.  

## Dataset  

1. There are 5 classes in the dataset:  
a) Circle  
b) Rectangle  
c) Ellipse  
d) Square  
e) Rhombus  

## Dataset generation:  

1. As the .xml file annotations had only few class labels and the json folder contained .txt files which do not have bounding box annotations in the COCO/PASCAL_VOC dataset, <b>I have generated annotations for 150 images in tha dataset manually using LabelImg software</b>.  

2. Since the number of images are less, some data annotation is performed for training with YOLOv3 such as changing backgrounds, cropping and changing Hue, Saturation and Values.    

## Network Used (YOLOv3):  

The following possible networks can be used:  

1. YOLOv3  
2. SSD  
3. Semantic Segmentation  

Since YOLOv3 is most robust among all of the above and also good comparatively for small dataset, I have used YOLOv3 for training and detecting shapes in the images.  

## Framework used:  

1. Darknet for YOLOv3.  

## Data organization:  

--darknet  
 |--backup  
  |--cfg  
   |--data  
    |--predictions on test data  
-- freezed weights   

1. The ```/darknet/backup/``` folder contains three different types of files:  
   a) customdata.data:- It contains number of classes, path to train and test file, path to customdata.names.  
   b) customdata.names:- It contains names of different classes for detection.  
   c) ```train.txt``` and ```test.txt``` files:- These files contain the path to the train and test images.  
   
2. ```/darknet/cfg/``` folder contains three files for YOLOv3:  
  a) ```custom.data```  
  b) ```customdata.cfg``` which contains the architecture that we have used for the network.  
  
## Predictions:  

1. The ```/darknet ``` folder contains predictions.png images for different test images, when the network is trained for different number of epochs.  

## Training:  

1. Since YOLOv3 requires good amount of training, running it on Google Colabs is not feasible as once run-time is finished the code has to run from scratch.   

2. I have used the CPU for training. There are nearly 50,0000 iterations in the code and for the model to completely get trained on CPU, it will take around 6-7 days. I have attached the results of the predictions (which are good enough, when we consider 150 images for training and around 8 hours of traning on CPU).  

3. a) Momentum - 0.9  
   b) learning rate - 0.001  
   c) max_batches - 500000  
   d) activation - leaky  RELU
   e) batch_size - 64  
   f) num_of_classes - 05  
   
   
## Improvements Required for best results:  

1. Using a large dataset, around 1000 images minimum.  
2. Changing activation and using Mish or Swish instead.  
3. Changing the network configuration by changing the number of layers and using dilated convolutions.
4. Using RetinaNet for localization task.  

## How to run the files:  

1. For training:  
```python   
 ./darknet detector train backup/customdata.data cfg/customdata.cfg darknet53.conv.74  
```   
 
 2. For testing:  
 ```python   
 ./darknet detector test backup/customdata.data cfg/customdata.cfg darknet53.conv.74  '/path/to/test_image'  
 ```   
 
 3. For plotting the graphs of Loss vs Batch/Epochs:  
 ```python  
 python3 TrainLoss.py /path/to/train.log  
 ```
 4. For saving the logs in the file <train.log> whilel training:  
 ```python  
 ./darknet detector train backup/customdata.data cfg/customdata.cfg darknet53.conv.74 >> backup/train.log  
 ```
 


 






    
  


