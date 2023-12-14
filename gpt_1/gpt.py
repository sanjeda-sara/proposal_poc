import os
import openai
import json
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Set your OpenAI GPT-3.5 Turbo API key
openai.api_key = os.getenv("OPENAI_API_KEY")
prompt_message = [
    {"role": "system", "content": "You are a helpful assistant."}

]


def ask_gpt3(prompt):
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # Check if 'choices' key exists in the response
    content = response.choices[0].text
    return content


def process_template(template_data, demo_data):
    for section, content in demo_data.items():
        if section in template_data:
            if isinstance(content, dict):
                for key, value in content.items():
                    if key in template_data[section]:
                        template_data[section][key] = value
            elif isinstance(content, list):
                template_data[section] = content  # Assume it's a list
    return template_data


def main():
    # Provide the path to your template and demo files
    template_path = 'C:/Users/User_01/Desktop/gpt-3.5/proposal_template.json'
    demo_path = 'C:/Users/User_01/Desktop/gpt-3.5/demo_template_1.json'
    output_path = 'C:/Users/User_01/Desktop/gpt-3.5/final_proposal_output.json'

    # Load the template from the template file
    with open(template_path, 'r') as template_file:
        template_data = json.load(template_file)

    # Load the demo data
    with open(demo_path, 'r') as demo_file:
        demo_data = json.load(demo_file)

    # Process the template based on the demo data
    # processed_template = process_template(template_data, demo_data)

    # Write the modified data back to the output JSON file
    # with open(output_path, 'w') as output_file:
    #     json.dump(processed_template, output_file, indent=2)

    # print(processed_template)

    prompt = "learn from this text: " + \
        str(demo_data) + "\n now generate a project proposal following this key values: " + \
        str(template_data) + "\n complete proposal as a complete json format"
    prompt_message.append({"role": "user", "content": prompt})
    proposal = ask_gpt3(prompt=prompt)
    proposal = proposal.strip()
    proposal = proposal + ' }'
    print(":::::::::::::::::::::::::::::::::::")
    proposal = json.dumps(proposal)
    _proposal = json.loads(proposal)
    print(_proposal)
    print(type(_proposal))
   

def test_1(first: int , second: int, third: str = None):
    print(first, second, third)


if __name__ == "__main__":
    # main()
    test_1(1,2,3)
