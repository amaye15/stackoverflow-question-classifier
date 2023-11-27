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
        "inputs": "Hi, I recently bought a device from your company but it is not working as advertised and I would like to get reimbursed!",
        "parameters": {"candidate_labels": ["refund", "legal", "faq"]},
    })


st.set_page_config(page_title="Model API", page_icon="📹")
st.markdown("# Model API")
st.sidebar.header("Model API")


show_code(api_demo)
