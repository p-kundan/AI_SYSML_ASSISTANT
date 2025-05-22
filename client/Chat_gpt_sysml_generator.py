import openai
import os
from dotenv import load_dotenv
import datetime

# 1. Load your OpenAI API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# 2. Get user prompt
print("Enter your system modeling prompt:")
user_prompt = input("> ")

# 3. Send prompt to ChatGPT
response = openai.ChatCompletion.create(
    model="gpt-4",  # or use "gpt-3.5-turbo" if you don't have GPT-4 access
    messages=[
        {"role": "system", "content": "You are a SysML modeling assistant. Generate YAML output with blocks and relationships."},
        {"role": "user", "content": user_prompt}
    ]
)

# 4. Extract and print the output
yaml_output = response['choices'][0]['message']['content']
print("\n--- YAML OUTPUT ---\n")
print(yaml_output)

# 5. Save the YAML to test_models/model_output.yaml
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
file_path = f"../test_models/model_output_{timestamp}.yaml"

with open(file_path, "w") as file:
    file.write(yaml_output)

print(f"\n✅ YAML saved to: {file_path}")
