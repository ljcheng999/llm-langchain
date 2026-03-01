import os

# Get the directory where this __init__.py file is located
PROJECT_PATH = os.getcwd()
# print("PROJECT_PATH: ", PROJECT_PATH)

# module_dir = os.path.dirname(os.path.abspath(__file__))
# print("module_dir: ", module_dir)

with open(os.path.join(PROJECT_PATH, "src", "data", "misty.md"), "r") as f:
    misty_system_prompt = f.read()
    # print("misty_system_prompt: ", misty_system_prompt)
