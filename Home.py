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
from functions import generate_title, ZeroShotClassificationPipeline, classify_text

generate_title()

import time

def my_task():
    # Replace this with the task you want to perform

    input_text = "Write your question here:"
    candidate_labels = ""

    # Initialize the zero-shot classification pipeline
    zero_shot_pipeline = ZeroShotClassificationPipeline("amaye15/Stack-Overflow-Zero-Shot-Classification", st.secrets.Authorization)

    # Display a loading message and make the API request
    with st.spinner('Checking model status...'):
        result, should_wait = classify_text(zero_shot_pipeline, input_text, candidate_labels)

    # If the model was loading, wait for the estimated time and then retry
    while should_wait:
        #with st.spinner(f'Model is loading, please wait... Estimated time: {result["estimated_time"]:.2f} seconds'):
        time.sleep(result["estimated_time"])  # Wait for the estimated time
        result, should_wait = classify_text(zero_shot_pipeline, input_text, candidate_labels)
    print("Task executed")

while True:
    st.markdown("""
## Welcome to Our Stack Overflow Community Contribution Project!

Hello and welcome!

As a fellow enthusiast of Stack Overflow, a platform that has often been our go-to solution for tackling tough development questions, we understand the importance of giving back to the community that has helped us so much. This is why we are thrilled to announce an exciting opportunity for you to contribute to the betterment of Stack Overflow.

## Join Our Tag Management Enhancement Initiative!

Stack Overflow is all set to enhance the tag management system, which is crucial for streamlining the question-answering process, especially for our new users. Currently, when users post questions, they often face challenges in selecting the most relevant tags. To address this, we are planning to introduce an automated tag suggestion feature.

## Be a Part of This Transformative Journey

By participating in this initiative, not only will you contribute to a platform that has been a valuable resource for developers worldwide, but you will also sharpen your skills in machine learning and data analysis.            
""")
    my_task()           # Execute the task
    time.sleep(300)     # Wait for 300 seconds (5 minutes)
