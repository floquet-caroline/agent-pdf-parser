import os
import pymupdf  # PyMuPDF
from openai import OpenAI
from dotenv import load_dotenv
import base64

# Load environment variables and initialize the client
load_dotenv()
api_key = os.getenv("API_KEY")

client = OpenAI(
    base_url="https://llm.hyperfluid.cloud/v1/organizations/ebc6b7a8-9ecd-4d3d-bafc-fef40ebe986f/shared-models/gemma-4-12b/v1", 
    api_key=api_key
)

# Infer the type of a PDF file (text-based or image-based)

def check_pdf_type(pdf_path: str, text_threshold: int = 100) -> str:
    """Checks if a PDF is text-based or image-based based on character count."""
    doc = pymupdf.open(pdf_path)
    total_text = "".join([page.get_text() for page in doc])
    return "image_based" if len(total_text.strip()) < text_threshold else "text_based"

def parse_pdf_with_endpoints(pdf_path: str) -> str:
    """Routes the PDF depending on its type."""
    pdf_type = check_pdf_type(pdf_path)
    
    if pdf_type == "image_based":
        print(f"[{pdf_path}] Detected as image-based. Routing to OCR (lighton3)...")
        # Add your lighton3 OCR logic here
        markdown_result = "[OCR placeholder output]"
    else:
        print(f"[{pdf_path}] Detected as text-based. Routing to gemma-4-12b parser...")
        raw_text = extract_raw_text(pdf_path)
        markdown_result = call_gemma_parser(raw_text)
        
    return markdown_result

# Parse text-based PDF files

def extract_raw_text(pdf_path: str) -> str:
    """Extracts raw text from a digitally native PDF."""
    doc = pymupdf.open(pdf_path)
    return "\n".join([page.get_text() for page in doc])

def call_gemma_parser(raw_text: str) -> str:
    """
    Sends raw text to the gemma endpoint using the OpenAI SDK client 
    to structure it into clean Markdown.
    """
    prompt = f"Convert the following raw PDF text into clean, structured Markdown format, preserving headers, lists, and tables where applicable:\n\n{raw_text}"
    
    response = client.chat.completions.create(
        model="gemma-4-12b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        max_tokens=2048
    )
    
    return response.choices[0].message.content

# Parse image-based PDF files

def convert_pdf_page_to_base64_image(page) -> str:
    """Converts a PyMuPDF page into a base64 encoded PNG string."""
    pix = page.get_pixmap(dpi=150)
    img_bytes = pix.tobytes("png")
    encoded = base64.b64encode(img_bytes).decode("utf-8")
    return encoded

def call_lighton_ocr(pdf_path: str) -> str:
    """
    Converts PDF pages to images and sends them to the lightonocr-3-1b-test endpoint.
    """
    doc = pymupdf.open(pdf_path)
    full_markdown = []
    
    for page_num, page in enumerate(doc):
        print(f"Processing page {page_num + 1} with OCR...")
        base64_image = convert_pdf_page_to_base64_image(page)
        
        # Standard multimodal chat completion format often used for vision/OCR models
        response = client.chat.completions.create(
            model="lightonocr-3-1b-test",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Extract all text from this image and output it in clean Markdown format."},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            temperature=0.1,
            max_tokens=2048,
        )
        
        full_markdown.append(response.choices[0].message.content)
        
    return "\n\n".join(full_markdown)