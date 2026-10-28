# AnimalGuard — Wild Boar Detection & Alert System

An end-to-end real-time wildlife monitoring and intrusion alert system designed to prevent crop damage and human-wildlife conflict. Developed for the Thoothukudi Hackathon.

---

## 📌 Architecture Overview

```
                        +----------------------+
                        |   Webcam / Camera    |
                        +----------+-----------+
                                   |
                                   v
                        +----------------------+
                        |   Python AI Module   |
                        | (YOLOv8 + OpenCV)    |
                        +----------+-----------+
                                   | HTTP POST /api/detections
                                   v
                        +----------------------+
                        |  Spring Boot Backend |
                        |     REST Service     |
                        +----------+-----------+
                                   |
                                   v
                        +----------------------+
                        |     H2 Database      |
                        |   (Detection Logs)   |
                        +----------------------+
```

- **`ai-module/`**: Real-time computer vision inference engine using YOLOv8 and OpenCV. Detects boars and forwards structured alert payloads to the backend REST API.
- **`backend/`**: Java Spring Boot backend service with H2 in-memory database to persist detection events, timestamps, device IDs, and confidence levels.
- **`dashboard/`**: Monitoring interface module for live feeds and detection logs.

---

## 🛠️ Tech Stack

- **Computer Vision & AI**: Python 3, Ultralytics YOLOv8, OpenCV
- **Backend**: Java 17+, Spring Boot 3, Spring Data JPA, REST APIs
- **Database**: H2 Database (In-Memory / File-based)
- **Build & Management**: Maven

---

## 🚀 Getting Started

### 1. Start the Spring Boot Backend

```bash
cd backend
./mvnw spring-boot:run
```
> On Windows:
```cmd
mvnw.cmd spring-boot:run
```
The REST API will be available at `http://localhost:8080`.
The H2 database console is accessible at `http://localhost:8080/h2-console`.

### 2. Run the AI Detection Module

Install the Python dependencies:
```bash
cd ai-module
pip install ultralytics opencv-python requests
```

Run live webcam detection:
```bash
python live_detect.py
```

Run detection on a test image:
```bash
python detect_boar.py
```

---

## 📡 REST API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/detections` | Log a new detection event with `deviceId`, `boarDetected`, `confidence` |
| `GET` | `/api/detections` | Retrieve all logged detection events |

---

## 👥 Author
- **Dharnish V** ([@DharnishV9361](https://github.com/DharnishV9361))
