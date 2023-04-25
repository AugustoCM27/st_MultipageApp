import streamlit as st
from Homepage import Homepage
from Análises import Análises
from Contato import Contato

PAGES = {
    "Home": Homepage,
    "Contact": Contato
    "Análises": Análises 
}

st.set_page_config(page_title="My Multipage App")

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page()

if __name__ == "__main__":
    main()
