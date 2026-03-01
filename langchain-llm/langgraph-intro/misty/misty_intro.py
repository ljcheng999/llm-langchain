# # Get the directory where this __init__.py file is located
# module_dir = os.path.dirname(os.path.abspath(__file__))

# with open(os.path.join(module_dir, "misty.md"), "r") as f:
#     misty_system_prompt = f.read()
#     print("misty_system_prompt: ", misty_system_prompt)

with open("misty.md", "r") as f:
    misty_system_prompt = f.read()
    print("misty_system_prompt: ", misty_system_prompt)
