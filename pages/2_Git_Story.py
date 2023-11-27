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

import pandas as pd
import streamlit as st
import subprocess
import os

col1, col2, col3 = st.columns([0.2, 0.6, 0.2])

with col1:
    st.image("./images/logo.png")
with col2:
    st.markdown("<h1 style='text-align: center;'>The Hugging Stack</h1>", unsafe_allow_html=True)
with col3:
    st.image("./images/logo.png")

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

# Load the commit data
df_commits = get_git_commits()

st.dataframe(df_commits, use_container_width=True)

# We do not need to sort by date since we're plotting by commit index
# df_commits.sort_values('date', inplace=True)

# Path for the generated video
video_path = '/mount/src/stackoverflow-question-classifier/git-story_media/videos/480p15/GitStory.mp4'

# Check if the video already exists and delete it if so
if os.path.exists(video_path):
    os.remove(video_path)

# Use subprocess to call git-story and generate the video
try:
    subprocess.run(['git-story','--low-quality'], check=True)
    # Display the video in Streamlit
    st.video(video_path)
except subprocess.CalledProcessError as e:
    st.error(f"An error occurred while generating the video: {e}")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")



