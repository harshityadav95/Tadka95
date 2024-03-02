from uihelpers import ui_utils
import streamlit as st


def sidebar_head():

    st.set_page_config(
        page_title="Tadka 95",
        page_icon="images/tadka95_squarelogo.png",
        layout="wide",
        initial_sidebar_state="auto"
    )

    # Tadka 95 Logo
    html_code = ui_utils.show_tadka95_logo(100, [1, 1, 1, 1], margin=[0, 0, 0, 0])
    st.sidebar.markdown(html_code, unsafe_allow_html=True)
    st.sidebar.markdown('')
    st.sidebar.markdown('')

def print_widget_labels(widget_title, margin_top=5, margin_bottom=10):
    """
    Prints Widget label on the sidebar and lets adjust its margins easily
    :param widget_title: Str
    """
    st.sidebar.markdown(
        f"""<p style="font-weight:500; margin-top:{margin_top}px;margin-bottom:{margin_bottom}px">{widget_title}</p>""",
        unsafe_allow_html=True)

