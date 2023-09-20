from imageai.Detection import ObjectDetection
import os

exectuion_path =os.getcwd()

detector =ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(exectuion_path,"resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()

detections =detector.detectObjectsFromImage(input_image=os.path.join(exectuion_path,"image.jpg"),output_image_path=os.path.join(exectuion_path,"imagenew.jpg"))

for eachObject in detections:
    print(eachObject["name"] ,":",eachObject["percentage_probability"])

from IPython.display import Image
Image(filename = 'imagenew.jpg')
