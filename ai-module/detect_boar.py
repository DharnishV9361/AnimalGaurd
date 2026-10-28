from ultralytics import YOLO
import cv2
import requests

# Load YOLO model
model = YOLO("yolov8n.pt")

# Load test image
image_path = "test.jpg"
img = cv2.imread(image_path)

if img is None:
    print("Error: Image not found.")
    exit()

# Run detection
results = model(img)

boar_detected = False

for r in results:
    for box in r.boxes:
        cls = int(box.cls[0])
        label = model.names[cls].lower()

        print("Detected:", label)

        # YOLO usually labels boars as "pig"
        if label in ["pig", "boar"]:
            boar_detected = True

if boar_detected:
    print("ALERT: Wild boar detected!")

    data = {
        "deviceId": "FARM001",
        "boarDetected": True,
        "confidence": 0.90
    }

    try:
        response = requests.post(
            "http://localhost:8080/api/detections",
            json=data
        )
        print("Sent to backend:", response.status_code)
    except:
        print("Could not connect to backend")

else:
    print("No wild boar detected.")
print("Testing backend connection...")

data = {
    "deviceId": "TEST001",
    "boarDetected": True,
    "confidence": 0.75
}

try:
    response = requests.post(
        "http://localhost:8080/api/detections",
        json=data
    )
    print("Backend response:", response.status_code)
    print(response.text)
except Exception as e:
    print("Error connecting to backend:", e)
