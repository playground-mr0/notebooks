import json

def modify_notebook(notebook_file):
    # Read the notebook file
    with open(notebook_file, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Flag to check if modification is done
    modified = False
    
    # Iterate through each cell in the notebook
    for cell in notebook['cells']:
        print(cell)
        if cell['cell_type'] == 'code':
            # Check if the target line exists in the cell content
            if "!pip install MRzeroCore &> /dev/null" in cell['source']:
                # Replace the line within the cell content
                cell['source'] = cell['source'].replace(
                    "!pip install MRzeroCore &> /dev/null\n",
                    "!pip install playgroundmr01 &> /dev/null\n"
                )
                print("Found line")
                modified = True  # Set modified flag to True
    
    # If modification is done, write back to the notebook file
    if modified:
        with open(notebook_file, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1)

# Usage example
if __name__ == "__main__":
    notebook_file = 'Test_change_pip_install.ipynb'  # Replace with your actual notebook file path
    modify_notebook(notebook_file)
    print(f"Notebook '{notebook_file}' has been modified.")
