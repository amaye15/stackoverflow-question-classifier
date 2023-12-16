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

### Harnessing Cutting-Edge Technology for Enhanced Tag Suggestions

In our quest to revolutionize Stack Overflow's tag management system, we are excited to incorporate the power of Hugging Face's "deberta-v3-base-zeroshot-v1" model. This advanced AI model represents a significant leap in natural language processing (NLP) capabilities.

### Why DeBERTa V3?

- **State-of-the-Art NLP**: The DeBERTa (Decoding-enhanced BERT with disentangled attention) model is at the forefront of NLP technology. It brings enhanced understanding and interpretation of the context and semantics of Stack Overflow questions.
- **Zero-Shot Learning Capabilities**: This model is specially designed for zero-shot learning, allowing it to understand and categorize content effectively without extensive training on specific tagging examples from Stack Overflow. This means it can start providing accurate tag suggestions almost immediately.
- **Adaptability and Efficiency**: The DeBERTa model adapts to the unique language and technical terms of Stack Overflow. It efficiently processes queries, ensuring a seamless user experience.

### Impact on Our Tag Suggestion Feature

By integrating the DeBERTa V3 model, our automated tag suggestion system will not only become more accurate but also more intuitive. It will be capable of understanding a wide range of programming queries and suggesting the most relevant tags, even for complex or less common questions.

This cutting-edge technology ensures that our tag management system will be incredibly effective in assisting both new and experienced users in navigating and contributing to the vast knowledge base of Stack Overflow.

### Join Us in This Technological Leap

Your contribution to this project helps in fine-tuning this advanced AI model for our specific use-case, making Stack Overflow more accessible and efficient for millions of users worldwide. Be a part of this exciting journey in harnessing AI to empower our community!
                """)
    my_task()           # Execute the task
    time.sleep(300)     # Wait for 300 seconds (5 minutes)
