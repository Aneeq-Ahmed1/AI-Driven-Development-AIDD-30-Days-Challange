from pypdf import PdfReader
import re

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Internal function: Extracts all text from a PDF file.

    Args:
        pdf_path: The path to the PDF file.

    Returns:
        A string containing all extracted text from the PDF.
    """
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        return f"Error extracting text from PDF: {e}"

def extract_text_from_pdf_tool_func(prompt_with_path: str) -> str:
    """
    Tool function: Extracts all text from a PDF file specified in the prompt.
    The prompt should contain 'PDF_PATH: <path_to_pdf>'.
    Example: "Summarize the content of the document with PDF_PATH: /path/to/document.pdf"
    """
    match = re.search(r"PDF_PATH:\s*(.+)", prompt_with_path)
    if match:
        pdf_path = match.group(1).strip()
        return extract_text_from_pdf(pdf_path)
    else:
        return "Error: PDF path not found in the prompt. Please provide the path in the format 'PDF_PATH: <path_to_pdf>'."