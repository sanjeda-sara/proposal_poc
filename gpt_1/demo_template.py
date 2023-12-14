import PyPDF2
from pdfminer.high_level import extract_text
import json

# Define a global variable to store the PDF dictionary
pdf_dict = {}

def pdf_to_dict(pdf_path):
    global pdf_dict  # Use the global variable

    # Extract text from the PDF using PyPDF2
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page_text = pdf_reader.pages[page_num].extract_text()
            pdf_dict[f'Page_{page_num + 1}'] = page_text

    # If PyPDF2 does not work well, fall back to pdfminer.six
    if not any(pdf_dict.values()):
        page_texts = extract_text(pdf_path).split('\x0c')
        for page_num, page_text in enumerate(page_texts):
            pdf_dict[f'Page_{page_num + 1}'] = page_text

def save_dict_as_json(json_path):
    global pdf_dict  # Use the global variable
    with open(json_path, 'w') as json_file:
        json.dump(pdf_dict, json_file, indent=2)

def main():
    pdf_path = 'C:/Users/User_01/Downloads/demo_template_1.pdf'
    
    # Call pdf_to_dict to populate the global pdf_dict
    pdf_to_dict(pdf_path)

    # Print the dictionary
    print(pdf_dict)

    # Save the dictionary as a JSON file
    json_path = 'C:/Users/User_01/Desktop/gpt-3.5/sample_1.json'
    save_dict_as_json(json_path)
    print(f'The dictionary has been saved as {json_path}')

if __name__ == "__main__":
    main()
















import PyPDF2
from pdfminer.high_level import extract_text
import json
import os

# Define a global variable to store the PDF dictionary
pdf_dict = {}

def pdf_to_dict(pdf_path):
    global pdf_dict  # Use the global variable

    # Extract text from the PDF using PyPDF2
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page_text = pdf_reader.pages[page_num].extract_text()
            pdf_dict[f'Page_{page_num + 1}'] = page_text

    # If PyPDF2 does not work well, fall back to pdfminer.six
    if not any(pdf_dict.values()):
        page_texts = extract_text(pdf_path).split('\x0c')
        for page_num, page_text in enumerate(page_texts):
            pdf_dict[f'Page_{page_num + 1}'] = page_text

def save_dict_as_json(json_path):
    global pdf_dict  # Use the global variable
    with open(json_path, 'w') as json_file:
        json.dump(pdf_dict, json_file, indent=2)

def main():
    pdf_path = 'C:/Users/User_01/Downloads/demo_template_1.pdf'

    # Create the JSON path in the same directory as the PDF
    json_path = os.path.join(os.path.dirname(pdf_path), 'demo_template_1.json')

    # Call pdf_to_dict to populate the global pdf_dict
    pdf_to_dict(pdf_path)

    # Print the dictionary
    print(pdf_dict)

    try:
        # Save the dictionary as a JSON file
        save_dict_as_json(json_path)
        print(f'The dictionary has been saved as {json_path}')
    except Exception as e:
        print(f'Error saving JSON: {e}')

if __name__ == "__main__":
    main()

