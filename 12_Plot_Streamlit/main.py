import os
import streamlit as st


INPUT_PATH = os.path.join(os.path.dirname(__file__),'input')

@st.cache_data()
def get_data():
    filename = [files.split('.')[0] for files in os.listdir(INPUT_PATH)]
    value = [float(open(os.path.join(INPUT_PATH,files), 'r').read()) for files in os.listdir(INPUT_PATH)]
    return dict(zip(filename, value))

if __name__ == "__main__":
    st.set_page_config(
        page_icon=":bar_chart:",
        page_title="12 day"
    )
    
    st.title("Streamlit LineChart")
    
    with st.spinner("Loading Data ..."):
        data = get_data()
    st.line_chart(data)