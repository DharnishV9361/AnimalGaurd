import cv2
import requests
from ultralytics import YOLO

# Load model
model = YOLO("yolov8n.pt")

# Backend URL
BACKEND_URL = "http://localhost:8080/api/detections"

cap = cv2.VideoCapture(0)

print("Starting live detection...")
print("Press 'q' to quit")

boar_sent = False  # prevent spamming backend

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    results = model(frame)

    boar_detected = False
    confidence = 0.0

    for result in results:
        boxes = result.boxes
        for box in boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            conf = float(box.conf[0])

            # Draw box
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{label} {conf:.2f}",
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (0, 255, 0), 2)

            # Check for boar/pig
            if label in ["pig", "boar"]:
                boar_detected = True
                confidence = conf

    # Send to backend once
    if boar_detected and not boar_sent:
        data = {
            "deviceId": "LIVE_CAM_01",
            "boarDetected": True,
            "confidence": confidence
        }

        try:
            response = requests.post(BACKEND_URL, json=data)
            print("Alert sent:", response.status_code, response.text)
            boar_sent = True
        except:
            print("Could not connect to backend")

    if not boar_detected:
        boar_sent = False

    cv2.imshow("Live Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
