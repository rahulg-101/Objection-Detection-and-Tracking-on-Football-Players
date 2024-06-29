import gradio as gr
from PIL import Image
import os
from ultralytics import YOLO
import tempfile
import time
import shutil

# Define a constant for the output directory
OUTPUT_DIR = "yolo_predictions"

def ensure_output_dir():
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)

def predictRoute(im):
    ensure_output_dir()
    
    # Convert to PIL Image
    img = Image.fromarray(im.astype('uint8'), 'RGB')

    # Create a temporary file
    with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as temp:
        temp_path = temp.name

    # Save the image to the temporary file
    img.save(temp_path)

    # Run YOLO prediction
    os.system(f'yolo predict model="artifacts/model_trainer/best.pt" source="{temp_path}" imgsz=416 project="{OUTPUT_DIR}" name="predict"')

    # Read the result
    result_path = os.path.join(OUTPUT_DIR, "predict", os.listdir(os.path.join(OUTPUT_DIR, "predict"))[0])

    # Clean up
    os.remove(temp_path)

    return gr.Image(result_path)

# Initialize the YOLO model
model = YOLO('artifacts/model_trainer/best.pt')

def process_video(input_video):
    ensure_output_dir()
    
    start = time.time()
    os.system(f'yolo predict model="artifacts/model_trainer/best.pt" source="{input_video}" imgsz=416 project="{OUTPUT_DIR}" name="predict"')
    elapsed = time.time() - start
    
    result_path = os.path.join(OUTPUT_DIR, "predict", os.listdir(os.path.join(OUTPUT_DIR, "predict"))[0])

    return gr.Video(result_path), f"Time taken for Prediction: {elapsed:.2f} seconds"

# Create a Gradio interface
image_prediction = gr.Interface(fn=predictRoute, inputs="image", outputs="image")
video_prediction = gr.Interface(process_video, gr.Video(), ["playable_video", gr.Textbox(label="Time Elapsed")])

demo = gr.TabbedInterface([image_prediction, video_prediction], ['Image Inferencing', 'Video Inferencing'], title="YOLO Football Player Detection App")
demo.launch()