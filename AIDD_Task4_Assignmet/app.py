import streamlit as st
import asyncio
import os
from agent import QuizAgent # Import the QuizAgent class

# Function to safely run async functions in Streamlit
def run_async_in_thread(coro):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(coro)

st.set_page_config(page_title="Study Notes Summarizer & Quiz Generator", layout="wide")
st.title("📚 Study Notes Summarizer & Quiz Generator")

# Check for GEMINI_API_KEY
if "GEMINI_API_KEY" not in os.environ:
    st.error("GEMINI_API_KEY environment variable not set. Please set it to use the application.")
    st.stop()

# Initialize QuizAgent
quiz_agent = QuizAgent()

uploaded_file = st.file_uploader("Upload your PDF document", type="pdf")

if uploaded_file is not None:
    # Create a temporary file to save the uploaded PDF
    temp_file_path = os.path.join("./", uploaded_file.name)
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"PDF uploaded successfully: {uploaded_file.name}")

    st.subheader("Actions")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Summarize PDF"):
            st.info("Generating summary... This may take a moment.")
            with st.spinner("Summarizing..."):
                try:
                    summary = run_async_in_thread(quiz_agent.summarize_pdf(temp_file_path))
                    st.subheader("Summary")
                    st.markdown(summary)
                except Exception as e:
                    st.error(f"Error generating summary: {e}")

    with col2:
        if st.button("Generate Quiz"):
            st.info("Generating quiz... This may take a moment.")
            with st.spinner("Generating quiz..."):
                try:
                    quiz = run_async_in_thread(quiz_agent.generate_quiz(temp_file_path))
                    st.subheader("Generated Quiz")
                    st.markdown(quiz)
                except Exception as e:
                    st.error(f"Error generating quiz: {e}")

    # Clean up the temporary file after use or add a button to do so
    # For simplicity, we're leaving it for now. In a production app, you'd want a more robust cleanup.

else:
    st.info("Please upload a PDF document to get started.")
