
To set up your environment and run the application:

1.  **Obtain a Gemini API Key:** If you don't have one, get a `GEMINI_API_KEY` from Google AI Studio.
2.  **Set the Environment Variable:** Set the `GEMINI_API_KEY` as an environment variable in your system.
    *   **Windows:**
        ```powershell
        $env:GEMINI_API_KEY="YOUR_API_KEY_HERE"
        ```
        (For persistent setting, use System Properties -> Environment Variables)
    *   **macOS/Linux:**
        ```bash
        export GEMINI_API_KEY="YOUR_API_KEY_HERE"
        ```
        (Add to your `~/.bashrc`, `~/.zshrc`, or equivalent for persistent setting)
3.  **Run the Streamlit Application:** Navigate to the project directory in your terminal and run:
    ```bash
    streamlit run app.py
    ```

This will launch the Streamlit application in your web browser, where you can upload a PDF, summarize it, and generate a quiz.
