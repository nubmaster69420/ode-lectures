from google import genai
from PIL import Image
import os
from tqdm import tqdm
import time


with open('src/system_instruction.txt', 'r', encoding='utf-8') as f:
    system_instruction = f.read()    

folder = "assets/hand_lectures"

client = genai.Client()

c = 0 
files = sorted([ f for f in os.listdir(folder) if f.endswith((".jpg", ".jpeg", ".png")) ])[c:]


for filename in tqdm(files, desc="Processing images", unit="page"):

    filepath = os.path.join(folder, filename)
    image = Image.open(filepath)

    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=[
                    system_instruction,
                    image
                ]
            )
            with open('raw/raw_output.md', 'a', encoding="utf-8") as of:
                of.write(f'{filename} -- {c}')
                of.write(f'\n\n --- \n\n')
                of.write(response.text)
                of.write('\n\n --- \n\n')
            break # Success, exit retry loop
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"Error at {filename} (attempt {attempt + 1}): {e}. Retrying...")
                time.sleep(2 ** attempt) # Exponential backoff
            else:
                print(f"Failed to process {filename} after {max_retries} attempts. Error: {e}")

    c += 1
