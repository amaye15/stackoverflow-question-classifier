

import os
import subprocess

import pandas as pd
import streamlit as st

from pages.functions import generate_title, get_git_commits


# Ttile
generate_title()

# Load the commit data
df_commits = get_git_commits()

st.markdown("## The Git Dataframe")

st.dataframe(df_commits, use_container_width=True)

# We do not need to sort by date since we're plotting by commit index
# df_commits.sort_values('date', inplace=True)
if st.button("Generate Git Video"):
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



