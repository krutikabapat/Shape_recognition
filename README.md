# Shape_recognition
Deep Learning based Shape detection and counting

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

2. As the .xml file annotations had only few class labels and the json folder contained .txt files which do not have bounding box annotations in the COCO/PASCAL_VOC dataset, I have generated annotations for 150 images in tha dataset manually using LabelImg software.  

3. Since the number of images are less, some data annotation is performed for training with YOLOv3 such as changing backgrounds, cropping and changing HSV values.  

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
   --backup
   --cfg
   --data
   --predictions on test data
-- freezed weights  

1. The /darknet/backup/ folder contains three different types of files:
   a) customdata.data:- It contains number of classes, path to train and test file, path to customdata.names.  
   b) customdata.names:- It contains names of different classes for detection.  
   c) train.txt and test.txt files:- These files contain the path to the train and test images.  
   
2. /darknet/cfg/ folder contains three files for YOLOv3:
  a) custom.data
  b) customdata.cfg which contains the architecture that we have used for the network.
  
## Predictions:  

1. The /darknet folder contains predictions.png images for different test images, when the network is trained for different number of epochs.  

2. 
    
  


