import roboflow

roboflow.login()

rf = roboflow.Roboflow()

WORKSPACE_ID = "Tiffany Detector" 
PROJECT_ID = "tiffany-detector" 
VERSION = 1  
MODEL_PATH = "/homes/joaopqds/Desktop/tiffany_detector/Tifanny_detector"

project = rf.workspace(WORKSPACE_ID).project(PROJECT_ID)
dataset = project.version(VERSION)

project.version(dataset.version).deploy(
    model_type="yolov8", model_path=MODEL_PATH
)

print(f"Model from {MODEL_PATH} uploaded to Roboflow project {PROJECT_ID}, version {VERSION}.")
print("Deployment may take up to 30 minutes.")