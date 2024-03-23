from roboflow import Roboflow

rf = Roboflow(api_key="OxsAN6ixRjwybe4l6akJ")
project = rf.workspace("gaelcam").project("gaelcam")
version = project.version(1)

dataset = version.download("yolov8")

from ultralytics import YOLO

model = YOLO('yolov8m')  
model.train(data=dataset.location + '/data.yaml', epochs=50, img_size=640)
