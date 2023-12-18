# Step 1: Install necessary packages
# You can do this via the command line: pip install fastapi uvicorn transformers

from fastapi import FastAPI, HTTPException
from transformers import pipeline
from pydantic import BaseModel
import os
import mlflow

os.environ['MLFLOW_TRACKING_USERNAME'] = "andrewmayes14"
os.environ['MLFLOW_TRACKING_PASSWORD'] = "ccb096afadd26486a787461f3495219662998c4b"
os.environ['MLFLOW_TRACKING_PROJECTNAME'] = "stackoverflow-question-classifier"

mlflow.set_tracking_uri(f'https://dagshub.com/' + os.environ['MLFLOW_TRACKING_USERNAME']
                        + '/' + os.environ['MLFLOW_TRACKING_PROJECTNAME'] + '.mlflow')

with mlflow.start_run():

    # Step 2: Create the FastAPI app
    app = FastAPI()

    # Step 3: Load the Hugging Face zero-shot classification model
    classifier = pipeline("zero-shot-classification", model="amaye15/Stack-Overflow-Zero-Shot-Classification")

    # Define a request model
    class ClassificationRequest(BaseModel):
        text: str
        labels: list[str]

    # Step 4: Define a route for classification
    @app.post("/classify")
    async def classify(request: ClassificationRequest):
        try:
            result = classifier(request.text, request.labels)
            # Log parameters and results
            mlflow.log_params({"text": request.text, "labels": result['labels'], "scores": result["scores"]})
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

# Step 5: Run the server
# This will be done via the command line: uvicorn script_name:app --reload
# curl -X 'POST' \
#   'http://127.0.0.1:8000/classify' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{ "text": "How to iterate over a list?", "labels": ["python", "c++", "javascript"]}'
