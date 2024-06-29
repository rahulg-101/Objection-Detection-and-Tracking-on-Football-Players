import sys,os
from YOLO_Object_Detection_and_Tracking.pipeline.training_pipeline import TrainingPipeline
from YOLO_Object_Detection_and_Tracking.utils.main_utils import decodeImage, encodeImageIntoBase64
from flask import Flask, request, jsonify, render_template,Response
from flask_cors import CORS, cross_origin
from YOLO_Object_Detection_and_Tracking.constant.application import APP_HOST, APP_PORT
import cv2
from ultralytics import YOLO


app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"



@app.route("/train")
def trainRoute():
    obj = TrainingPipeline()
    obj.run_pipeline()
    return "Training Successfull!!" 


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/predict", methods=['POST','GET'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)

        os.system('yolo predict model="artifacts/model_trainer/best.pt" source="inputImage.jpg" imgsz=416')

        opencodedbase64 = encodeImageIntoBase64("runs/detect/predict3/inputImage.jpg")
        result = {"image": opencodedbase64}
        os.system("rm -rf runs/detect/predict3")

    except ValueError as val:
        print(val)
        return Response("Value not found inside json data")
    except KeyError:
        return Response("Key value error incorrect key passed")
    except Exception as e:
        print(e)
        result = "Invalid input"

    return jsonify(result)



# @app.route("/live", methods=['GET'])
# @cross_origin()
# def predictLive():
#     try:
#         os.system('yolo predict model="artifacts/model_trainer/best.pt" source=0 imgsz=416')
#         os.system("rm -rf runs/detect/predict3")
#         return "Camera starting!!" 

#     except ValueError as val:
#         print(val)
#         return Response("Value not found inside json data")
    
model = YOLO('artifacts/model_trainer/best.pt')

def generate_frames():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            break

        # Process the frame with the YOLOv8 model
        results = model(frame)[0]

        # Draw the detections on the frame
        annotated_frame = results.plot()

        # Convert the annotated frame to bytes
        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        frame = buffer.tobytes()

        # Yield the processed frame
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    # Release the webcam when done
    cap.release()

@app.route('/live')
def live_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host=APP_HOST, port=APP_PORT)       # The app will run on http://127.0.0.1:8080/
