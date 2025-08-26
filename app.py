import streamlit as st
import pandas as pd
import random

# Load the vocabulary CSV file
@st.cache_data
def load_data():
    return pd.read_csv("n400_flashcards.csv")

data = load_data()

# Initialize session state
if "current_index" not in st.session_state:
    st.session_state.current_index = random.randint(0, len(data) - 1)
if "show_definition" not in st.session_state:
    st.session_state.show_definition = False

# --- Define callbacks ---
def show_definition():
    st.session_state.show_definition = True

def next_word():
    st.session_state.current_index = random.randint(0, len(data) - 1)
    st.session_state.show_definition = False

# Display header
st.title("US N-400 Naturalization Vocabulary Flashcards")
st.markdown("Study definitions for your U.S. Citizenship interview.")

# Get current word and definition
term = data.iloc[st.session_state.current_index]["Term"]
definition = data.iloc[st.session_state.current_index]["Definition"]

# Show term
st.markdown(f"### Word or Phrase:")
st.markdown(f"<div style='font-size: 28px; font-weight: bold; color: #4F8BF9;'>\"{term}\"</div>", unsafe_allow_html=True)

# Buttons using callbacks
col1, col2 = st.columns(2)
with col1:
    st.button("Show Definition", on_click=show_definition)
with col2:
    st.button("Next Word", on_click=next_word)

# Show definition if revealed
if st.session_state.show_definition:
    st.markdown(
        f"<div style='font-size: 20px; color: orange;'> {definition.capitalize()}</div>",
        unsafe_allow_html=True
    )
