import inspect
import textwrap
import streamlit as st
from functions import generate_title, ZeroShotClassificationPipeline

def show_code(demo):
    """Showing the code of the demo."""
    #show_code = st.sidebar.checkbox("Show code", True)
    if show_code:
        # Showing the code of the demo.
        #st.markdown("## Code")
        sourcelines, _ = inspect.getsourcelines(demo)
        st.code(textwrap.dedent("".join(sourcelines[1:])))


def api_demo() -> None:

    import requests

    API_URL = "https://api-inference.huggingface.co/models/amaye15/Stack-Overflow-Zero-Shot-Classification"
    headers = {"Authorization": "Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    output = query({
        "inputs": "Simulation of Service using Mockito 2 leads to stubbing error",
        "parameters": {"candidate_labels": ['java', 'javascript', 'c#',]},
    })


generate_title()

st.write("Copy & Paste:")
show_code(api_demo)
