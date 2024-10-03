import os
import sys
import re
from MoMaStates import search_texts

# def find_text_suffix():
#     # Define your suffix logic here
#     return f" <<< Action with YSD >>>"

# def modify_file(file_path):
#     # Read the file contents
#     with open(file_path, 'r') as file:
#         lines = file.readlines()

#     # Modify the contents
#     modified_lines = []
#     for line in lines:
#         # Check if any of the search texts are in the line
#         if any(search_text in line for search_text in search_texts):
#             # Find the matching text in the line
#             matching_text = next(search_text for search_text in search_texts if search_text in line)
#             # Append the suffix
#             line = line.strip() + find_text_suffix() + "\n"
#         modified_lines.append(line)

#     # Write the modified contents back to the same file
#     with open(file_path, 'w') as file:
#         file.writelines(modified_lines)

def find_text_suffix(text):
    if text in search_texts:
        return f" << {search_texts[text]['id']} {search_texts[text]['comment']}"
    return ""

def modify_file(file_path):
    # Read the file contents
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Modify the contents
    modified_lines = []
    for line in lines:
        # Check if any of the search texts are in the line
        if any(search_text in line for search_text in search_texts):
            # Find the matching text in the line
            matching_text = next(search_text for search_text in search_texts if search_text in line)
            # Append the suffix
            line = line.strip() + find_text_suffix(matching_text) + "\n"
        modified_lines.append(line)

    # Write the modified contents back to the same file
    with open(file_path, 'w') as file:
        file.writelines(modified_lines)

# run command in notepad++ python C:/Users/urimrm/Projekty/Scripts/AnalyzeRxLogFiles/HighLightMoMa/HighLightMoMa.py "$(FULL_CURRENT_PATH)"
fn = sys.argv[1]
if os.path.exists(fn):
    print(fn)
    modify_file(fn)