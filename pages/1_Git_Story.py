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
import altair as alt
import subprocess

import streamlit as st
import pandas as pd
import altair as alt
import subprocess

# Function to get commits from git log
def get_git_commits():
    # Use subprocess to execute the git log command and capture the output
    git_log_output = subprocess.check_output(
        ['git', 'log', '--pretty=format:%h,%an,%ad,%s', '--date=short'],
        encoding='utf-8'
    )
    # Split the output into lines and then into a list of lists
    lines = git_log_output.strip().split('\n')

    commit_data = [line.split(',', 3) for line in lines]
    
    # Convert to DataFrame
    df_commits = pd.DataFrame(commit_data, columns=['hash', 'author', 'date', 'message'])
    df_commits['date'] = pd.to_datetime(df_commits['date'])
    # Add an index column that will serve as a quantitative scale for the y-axis
    df_commits['index'] = range(len(df_commits))
    return df_commits

# Load the commit data
df_commits = get_git_commits()

# We do not need to sort by date since we're plotting by commit index
# df_commits.sort_values('date', inplace=True)

print(df_commits, flush=True)

# Create an interactive chart using Altair with commits on the y-axis
chart = alt.Chart(df_commits).mark_circle(size=60).encode(
    y=alt.Y('index:Q', title='Commit Number'),  # Using the index for the y-axis
    x='author:N',  # Authors are on the x-axis
    color='author:N',
    tooltip=['index:Q', 'author:N', 'message:N', 'hash:N']
).properties(
    height=600  # You might want to adjust the height to fit all your data
).interactive()

st.title('Git Commit History')
st.altair_chart(chart, use_container_width=True)

st.altair_chart(chart, use_container_width=True)


#st.set_page_config(page_title="Git Story", page_icon="📈")
#st.markdown("# Git Story")
#st.sidebar.header("Git Story")

