import os
import openai
import PyPDF2
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Set your OpenAI GPT-3.5 Turbo API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):  # Update this line
            page = pdf_reader.pages[page_num]           # Update this line
            text += page.extract_text()
    return text


def ask_gpt3(question, context):
    prompt = f"Context: {context}\n\nQuestion: {question}\nAnswer:"
    response = openai.completions.create(
    model="text-davinci-003",  # or another engine
    prompt=prompt,
    max_tokens=150,
    n=1,
    stop=None,
)

    return response.choices[0].text.strip()

def main():
    # Provide the path to your PDF file
    pdf_path = 'C:/Users/User_01/Desktop/gpt-3.5/demo_template_1.json'

    # Read the template from the JSON file
    with open('path/to/your/template.json', 'r') as template_file:
        output_data = json.load(template_file)

    # Read the content of the PDF
    pdf_content = read_pdf(pdf_path)

    while True:
        # Get user question from the terminal
        user_question = input("Ask a question (or type 'exit' to quit): ")

        if user_question.lower() == 'exit':
            break

        # Ask GPT-3.5 Turbo for an answer
        answer = ask_gpt3(user_question, pdf_content)

        # Print the answer
        print(f"Answer: {answer}\n")

if __name__ == "__main__":
    main()
