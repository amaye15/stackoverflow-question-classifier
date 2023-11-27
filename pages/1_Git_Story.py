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
import subprocess
import os

# Path for the generated video
video_path = 'git_history_video.mp4'

# Check if the video already exists and delete it if so
if os.path.exists(video_path):
    os.remove(video_path)

# Use subprocess to call git-story and generate the video
try:
    subprocess.run(['git-story', '--media-dir', video_path], check=True)
    # Display the video in Streamlit
    st.video(video_path)
except subprocess.CalledProcessError as e:
    st.error(f"An error occurred while generating the video: {e}")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")


