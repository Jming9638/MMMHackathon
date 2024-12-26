import streamlit as st


def run():
    st.set_page_config(
        page_title="PT Hackathon",
        page_icon="💻",
        layout="centered",
        initial_sidebar_state="auto"
    )
    st.logo("assets/images/logo.png", size="large")
    with open("./README.md", "r") as f:
        content = f.read()

    st.markdown(content)


if __name__ == "__main__":
    run()
