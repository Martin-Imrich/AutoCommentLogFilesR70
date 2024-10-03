import re
import sys
import os

# Dictionary of strings to search for with their corresponding comments
search_texts = {
    "Target=0": " <<< SWF_MTD - Measuringhead Traverse Drive >>>",
    "Target=1": " <<< SWF_DYD - Delivery Drive >>>",
    "Target=2": " <<< SWF_YTD - Yarn Traverse Drive >>>",
    "Target=3": " <<< SWB_WRD - Winding Roller Drive >>>",
    "Target=4": " <<< SWB_LCD - Loop Compensator Drive >>>",
    "Target=5": " <<< SWB_YSD - Yarn Storage Drive >>>",
    "Target=6": " <<< SWF_TLD - Top roller Lift Drive >>>",
    "Target=7": " <<< SWF_YHD - Yarn Handling Drive >>>",
    "Target=8": " <<< SWF_SND - Suction Nozzle Drive >>>",
    "Target=10": " <<< SWF_WXD - Waxing Drive >>>", 
    # Add more search strings and their corresponding comments here
}

def find_text_suffix(line):
    # Check if any of the search texts are in the line
    for search_text, comment in search_texts.items():
        if search_text in line:
            return comment
    return ""

def modify_file(file_path):
    # Read the file contents
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Modify the contents
    modified_lines = []
    for line in lines:
        # Check if any of the search texts are in the line
        suffix = find_text_suffix(line)
        if suffix:
            # Append the suffix
            line = line.strip() + suffix + "\n"
        modified_lines.append(line)

    # Write the modified contents back to the same file
    with open(file_path, 'w') as file:
        file.writelines(modified_lines)

# Use this function to modify your file
#modify_file('C:/Users/urimrm/Programy/QC_Terminal/QC_Terminal506/QcSettings/log/SUC_20240821_delete.log')


# C:\Users\urimrm\Programy\QC_Terminal\QC_Terminal506\QcSettings\log\SUC_20240821_delete.log
# run command in notepad++ python C:\Users\urimrm\Programy\QC_Terminal\QC_Terminal506\QcSettings\log\SUC_20240821_delete.log "$(FULL_CURRENT_PATH)"
fn = sys.argv[1]
if os.path.exists(fn):
    print(fn)
    modify_file(fn)

