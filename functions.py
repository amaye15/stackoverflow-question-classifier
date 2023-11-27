import streamlit as st
import requests
import subprocess
import pandas as pd



def generate_title():
    # Ttile
    col1, col2, col3 = st.columns([0.2, 0.6, 0.2])

    with col1:
        st.image("./images/logo.png")
    with col2:
        st.markdown("<h1 style='text-align: center;'>The Hugging Stack</h1>", unsafe_allow_html=True)
    with col3:
        st.image("./images/logo.png")
    

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
    
# Function to get commits from git log
def get_git_commits():
    # Use subprocess to execute the git log command and capture the output
    git_log_output = subprocess.check_output(
        ['git', 'log', '--pretty=format:%h,%an,%ad,%s'],
        encoding='utf-8'
    )
    # Split the output into lines and then into a list of lists
    lines = git_log_output.strip().split('\n')

    commit_data = [line.split(',', 3) for line in lines]
    
    # Convert to DataFrame
    df_commits = pd.DataFrame(commit_data, columns=['hash', 'author', 'date', 'message'])
    df_commits['date'] = pd.to_datetime(df_commits['date'])
    # Add an index column that will serve as a quantitative scale for the y-axis
    #df_commits['index'] = range(len(df_commits))
    return df_commits