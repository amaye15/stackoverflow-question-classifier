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
        with st.spinner(f'Model is loading, please wait... Estimated time: {result["estimated_time"]:.2f} seconds'):
            time.sleep(result["estimated_time"])  # Wait for the estimated time
            result, should_wait = classify_text(zero_shot_pipeline, input_text, candidate_labels)
    print("Task executed")

while True:
    my_task()           # Execute the task
    time.sleep(300)     # Wait for 300 seconds (5 minutes)
