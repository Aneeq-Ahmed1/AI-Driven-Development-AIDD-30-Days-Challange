import os
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, function_tool
import asyncio
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Assuming tools.py is in the same directory
from tools import extract_text_from_pdf_tool_func

# Ensure your Gemini API key is set as an environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

# 1. Create an AsyncOpenAI client configured for the Gemini API
gemini_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

# 2. Define the model to be used by the agent
gemini_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=gemini_client,
)

# Define a tool for extracting text from PDF using the wrapper function
pdf_extraction_tool = function_tool(extract_text_from_pdf_tool_func)

class QuizAgent:
    def __init__(self):
        self.summarizer_agent = Agent(
            name="SummarizerAgent",
            instructions="You are a helpful assistant that summarizes PDF documents. Provide a concise and clean summary of the given text. When asked to summarize a PDF, you should call the 'extract_text_from_pdf_tool_func' tool with the full prompt you received.",
            model=gemini_model,
            tools=[pdf_extraction_tool]
        )

        self.quiz_generator_agent = Agent(
            name="QuizGeneratorAgent",
            instructions="You are a helpful assistant that generates multiple-choice questions (MCQs) from text. Generate 5 MCQs with 4 options each, and clearly mark the correct answer. Ensure questions are directly based on the provided text. When asked to generate a quiz from a PDF, you should call the 'extract_text_from_pdf_tool_func' tool with the full prompt you received.",
            model=gemini_model,
            tools=[pdf_extraction_tool]
        )

    async def summarize_pdf(self, pdf_path: str) -> str:
        """
        Summarizes the content of a PDF file.
        """
        # The agent will call the tool internally
        # Pass the full prompt to the agent, which the tool function will parse
        result = await Runner.run(self.summarizer_agent, input=f"Summarize the content from the document with PDF_PATH: {pdf_path}")
        return result.final_output

    async def generate_quiz(self, pdf_path: str) -> str:
        """
        Generates MCQs from the content of a PDF file.
        """
        # The agent will call the tool internally
        # Pass the full prompt to the agent, which the tool function will parse
        result = await Runner.run(self.quiz_generator_agent, input=f"Generate 5 multiple-choice questions (MCQs) with 4 options and mark the correct answer from the document with PDF_PATH: {pdf_path}")
        return result.final_output

async def main():
    # This part is for testing the agent functionality
    print("QuizAgent initialized. Please set GEMINI_API_KEY environment variable.")
    print("You can call summarize_pdf and generate_quiz methods.")

if __name__ == "__main__":
    asyncio.run(main())