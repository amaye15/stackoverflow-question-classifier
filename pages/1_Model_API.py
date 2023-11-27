import inspect
import textwrap
import streamlit as st

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
        "parameters": {"candidate_labels": ['java', 'javascript', 'c#', 'python', 'git', 'c++', 'ios', 'android']},
    })


col1, col2, col3 = st.columns([0.2, 0.6, 0.2])

with col1:
    st.image("./images/logo.png")
with col2:
    st.markdown("<h1 style='text-align: center;'>The Hugging Stack</h1>", unsafe_allow_html=True)
with col3:
    st.image("./images/logo.png")

show_code(api_demo)
