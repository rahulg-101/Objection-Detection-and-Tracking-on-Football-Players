import gradio as gr
from PIL import Image
import os
from ultralytics import YOLO
import tempfile
import cv2



def predictRoute(im):
        # Convert to PIL Image
        img = Image.fromarray(im.astype('uint8'), 'RGB')

        # Create a temporary file
        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as temp:
            temp_path = temp.name

        # Save the image to the temporary file
        img.save(temp_path)

        # Run YOLO prediction
        os.system(f'yolo predict model="artifacts/model_trainer/best.pt" source="{temp_path}" imgsz=416')

        # Read the result (modify this part based on your actual output)
        image_name = os.listdir("runs/detect/predict3")[0]
        result_path = os.path.join("runs/detect/predict3",str(image_name))
        # Clean up
        os.remove(temp_path)
        # os.system("rm -rf runs/detect/predict3")

        return gr.Image(result_path)
    
# Initialize the YOLO model
model = YOLO('artifacts/model_trainer/best.pt')

def process_video(input_video):
    os.system(f'yolo predict model="artifacts/model_trainer/best.pt" source="{input_video}" imgsz=416')

    image_name = os.listdir("runs/detect/predict3")[0]
    result_path = os.path.join("runs/detect/predict3",str(image_name))

    return gr.Video(result_path)

    
    
# Create a Gradio interface
image_prediction = gr.Interface(fn=predictRoute, inputs="image", outputs="image")
# iface.launch()
video_prediction = gr.Interface(process_video, gr.Video(),"playable_video")

gr.TabbedInterface([image_prediction, video_prediction],['Image Inferencing','Video Inferencing']).launch()

