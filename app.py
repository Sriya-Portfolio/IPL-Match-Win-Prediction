import streamlit as st
from about import about_page
from calculations import calculation_page
from prediction import prediction_page
from conclusion import conclusion_page

st.set_page_config(
    page_title="IPL Match Win Predictor",
    page_icon="🏏"
)

if 'page' not in st.session_state:
    st.session_state.page = 'about'

with st.sidebar:
    st.sidebar.title("📑 Pages")
    pages = [
        ("ℹ️ About", "about"),
        ("🧮 Calculations", "calculations"),
        ("🏏 Win Prediction", "prediction"),
        ("🤝 Conclusion", "conclusion")
    ]

    # CSS for Active Page Styling
    st.markdown(
        """
        <style>
            div.stButton > button {
                width: 100%;
                padding: 10px;
                font-weight: bold;
                border-radius: 10px;
                margin-bottom: 8px;
                border: 2px solid transparent;
                transition: all 0.2s;
            }
            .active-btn button {
                background-color: #f0f8ff; /* Light Blue Background */
                border: 2px solid #87CEFA; /* Sky Blue Border */
                box-shadow: 0px 0px 12px rgba(135, 206, 250, 0.5);
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display Sidebar Buttons
    for label, page_id in pages:
        button_key = f"{page_id}_btn"

        # Highlight Active Button
        if st.session_state.page == page_id:
            st.markdown('<div class="active-btn">', unsafe_allow_html=True)
            if st.button(label, key=button_key, use_container_width=True):
                st.session_state.page = page_id
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            if st.button(label, key=button_key, use_container_width=True):
                st.session_state.page = page_id

if st.session_state.page == 'about':
    about_page()
if st.session_state.page == 'calculations':
    calculation_page()
if st.session_state.page == 'prediction':
    prediction_page()
if st.session_state.page == 'conclusion':
    conclusion_page()