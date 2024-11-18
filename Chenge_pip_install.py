import json

print("Change")

def modify_notebook(notebook_file):
    # Read the notebook file
    with open(notebook_file, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Flag to check if modification is done
    modified = False
    
    # Iterate through each cell in the notebook
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            # Check if the target line exists in the cell content
            source_lines = cell['source']
            modified_lines = []
            for line in source_lines:
                if "!pip install MRzeroCore &> /dev/null" in line:
                    # Replace the line if found
                    modified_lines.append(
                        "!pip install playgroundmr01 &> /dev/null\n"
                    )
                    modified = True
                else:
                    modified_lines.append(line)
            
            # Update the cell source with modified lines
            cell['source'] = modified_lines
    
    # If modification is done, write back to the notebook file
    if modified:
        with open(notebook_file, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1)

# Usage example
if __name__ == "__main__":
    notebook_file = 'Test_change_pip_install.ipynb'  # Replace with your actual notebook file path
    modify_notebook(notebook_file)
    print(f"Notebook '{notebook_file}' has been modified.")
