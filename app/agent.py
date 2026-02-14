import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GENAI_API_KEY"))

def generate_solution(train_inputs, train_outputs):
    task_desc=""
    for i, (inp, out) in enumerate(zip(train_inputs, train_outputs)):
        task_desc += f"\nExample {i+1}:\nInput:\n{inp}\nOutput:\n{out}\n"

    prompt = f"""
    You are an expert Python developer solving logic puzzles.
    Your goal is to write a Python function `solve(input_grid)` that transforms the input grid to the output grid.
    
    You have access to `numpy` as `np`.
    
    Here are the input/output examples:
    
    {task_desc}
    
    Analyze the pattern. Is it a color change? A movement? A crop?
    Write the `solve` function in Python. Do not use markdown blocks. Just the code.
    """

    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)

    code = response.text.replace("```python", "").replace("```", "").strip()
    return code