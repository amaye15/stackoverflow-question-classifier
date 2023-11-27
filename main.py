# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import pandas as pd
import numpy as np
import requests
import plotly.express as px
import time



#st.sidebar.header("Questions")
st.set_page_config(page_title="Model UI", page_icon="📹")

# Define the wrapper class as before
class ZeroShotClassificationPipeline:
    def __init__(self, model_name, api_token):
        self.api_url = f"https://api-inference.huggingface.co/models/{model_name}"
        self.headers = {"Authorization": f"Bearer {api_token}"}

    def __call__(self, inputs, candidate_labels, multi_label=False):
        data = {
            "inputs": inputs,
            "parameters": {"candidate_labels": candidate_labels, "multi_label": multi_label}
        }
        response = requests.post(self.api_url, headers=self.headers, json=data)
        return response.json()

col1, col2, col3 = st.columns([0.2, 0.6, 0.2])

with col1:
    st.image("./images/logo.png")

with col2:
    # Streamlit app starts here
    st.markdown("<h1 style='text-align: center;'>The Hugging Stack</h1>", unsafe_allow_html=True)

with col3:
    st.image("./images/logo.png")


# User input for the text
input_text = st.text_area("Write your question here:", "")

# User input for the labels, separated by commas
input_labels = st.text_input("Add your programming languages here:", "")

# Convert string of labels into a list
candidate_labels = [label.strip() for label in input_labels.split(',') if label]  # Ensure no empty strings

# Function to handle API requests and retry if model is loading
@st.cache_data(ttl=30, show_spinner=False)  # Cache the function call to prevent re-runs on every interaction
def classify_text(_zero_shot_pipeline, input_text, candidate_labels):
    response = zero_shot_pipeline(input_text, candidate_labels)
    if "error" in response and "estimated_time" in response:  # Check if the model is still loading
        return response, True  # Return the response and a flag indicating to wait
    print(response, flush=True)
    return response, False  # Return the response and a flag indicating no need to wait

but1, but2 = st.columns(2)

with but1:
    classify = st.button('Classify')

with but2:
    generate = st.button('Generate')


# Button to perform classification
if classify:

    # Initialize the zero-shot classification pipeline
    zero_shot_pipeline = ZeroShotClassificationPipeline("amaye15/Stack-Overflow-Zero-Shot-Classification", st.secrets.Authorization)

    # Display a loading message and make the API request
    with st.spinner('Checking model status...'):
        result, should_wait = classify_text(zero_shot_pipeline, input_text, candidate_labels)

    # If the model was loading, wait for the estimated time and then retry
    while should_wait:
        with st.spinner(f'Model is loading, please wait... Estimated time: {result["estimated_time"]:.2f} seconds'):
            time.sleep(result["estimated_time"])  # Wait for the estimated time
            result, should_wait = classify_text(zero_shot_pipeline, input_text, candidate_labels)

    # If there's no error, proceed to display results
    if not should_wait and 'labels' in result and 'scores' in result:

        # Extract the labels and scores
        labels = result['labels']
        scores = result['scores']
        labels.reverse()
        scores.reverse()

        # Create a Plotly bar plot
        fig = px.bar(x=scores, 
                     y=labels, 
                     orientation='h', 
                     labels={'x':'Score', 'y':'Label'}, 
                     title='Zero-Shot Classification Results', 
                     )
        fig.update_layout(xaxis_title='Score', yaxis_title='Label')

        # Display the Plotly bar plot
        st.plotly_chart(fig)

# Button to perform classification
if generate:
    df = pd.read_pickle("data/StackOverFlow.pkl.gz")
    df["Label"] = df.Tags.str.split(",").apply(lambda x: x[0])
    sample = df.sample(1)
    input_text = sample["Title"].values[0]
    top_labels = list(df["Label"].value_counts().to_dict().keys())[:8]
    candidate_labels = [*sample["Label"].values.tolist(), *top_labels]

    # Initialize the zero-shot classification pipeline
    zero_shot_pipeline = ZeroShotClassificationPipeline("amaye15/Stack-Overflow-Zero-Shot-Classification", st.secrets.Authorization)

    # Display a loading message and make the API request
    with st.spinner('Checking model status...'):
        result, should_wait = classify_text(zero_shot_pipeline, input_text, candidate_labels)
    
    # If the model was loading, wait for the estimated time and then retry
    while should_wait:
        with st.spinner(f'Model is loading, please wait... Estimated time: {result["estimated_time"]:.2f} seconds'):
            time.sleep(result["estimated_time"])  # Wait for the estimated time
            result, should_wait = classify_text(zero_shot_pipeline, input_text, candidate_labels)
    # If there's no error, proceed to display results
    if not should_wait and 'labels' in result and 'scores' in result:
        # Extract the labels and scores
        labels = result['labels']
        scores = result['scores']
        labels.reverse()
        scores.reverse()

        # Create a Plotly bar plot
        fig = px.bar(x=scores, 
                     y=labels, 
                     orientation='h', 
                     labels={'x':'Score (%)', 'y':'Label'}, 
                     title= f"{sample['Label'].values[0]} - {input_text}", 
                     )
        fig.update_layout(xaxis_title='Score', yaxis_title='Label')

        # Display the Plotly bar plot
        st.plotly_chart(fig)