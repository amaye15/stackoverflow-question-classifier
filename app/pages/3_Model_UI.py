
import streamlit as st
import pandas as pd
import numpy as np
import requests
import plotly.express as px
import time
from functions import generate_title, ZeroShotClassificationPipeline, classify_text

generate_title()

st.markdown("## Model UI")

# User input for the text
input_text = st.text_area("Write your question here:", "How to loop over a list?")

# User input for the labels, separated by commas
input_labels = st.text_input("Add your programming languages here:", "python, javascript, java, c#, android, c++, php, git, ios, html")

# Convert string of labels into a list
candidate_labels = [label.strip() for label in input_labels.replace(" ", "").split(',') if label]  # Ensure no empty strings

but1, _ , _ = st.columns([0.15,0.16,0.8])

with but1:
    classify = st.button('Classify')

# with but2:
#     generate = st.button('Generate')

# Initialize the zero-shot classification pipeline
zero_shot_pipeline = ZeroShotClassificationPipeline("amaye15/Stack-Overflow-Zero-Shot-Classification", st.secrets.Authorization)


# Button to perform classification
if classify:
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
# if generate:
#     df = pd.read_pickle("data/StackOverFlow.pkl.gz")
#     df["Label"] = df.Tags.str.split(",").apply(lambda x: x[0])
#     sample = df.sample(1)
#     input_text = sample["Title"].values[0]
#     top_labels = list(df["Label"].value_counts().to_dict().keys())[:8]
#     candidate_labels = list(set([*sample["Label"].values.tolist(), *top_labels]))

#     # Display a loading message and make the API request
#     with st.spinner('Checking model status...'):
#         result, should_wait = classify_text(zero_shot_pipeline, input_text, candidate_labels)
    
#     # If the model was loading, wait for the estimated time and then retry
#     while should_wait:
#         with st.spinner(f'Model is loading, please wait... Estimated time: {result["estimated_time"]:.2f} seconds'):
#             time.sleep(result["estimated_time"])  # Wait for the estimated time
#             result, should_wait = classify_text(zero_shot_pipeline, input_text, candidate_labels)
#     # If there's no error, proceed to display results
#     if not should_wait and 'labels' in result and 'scores' in result:
#         # Extract the labels and scores
#         labels = result['labels']
#         scores = result['scores']
#         labels.reverse()
#         scores.reverse()

#         # Create a Plotly bar plot
#         fig = px.bar(x=scores, 
#                      y=labels, 
#                      orientation='h', 
#                      labels={'x':'Score (%)', 'y':'Label'}, 
#                      title= f"{sample['Label'].values[0]} - {input_text}", 
#                      )
#         fig.update_layout(xaxis_title='Score', yaxis_title='Label')

#         # Display the Plotly bar plot
#         st.plotly_chart(fig)