import streamlit as st



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