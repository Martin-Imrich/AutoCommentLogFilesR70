# This script is used to comment log from R70 SUC.
# It will append a full target text comment to log message.
#
# @author: Martin Imrich (martin.imrich@rieter.com) Version: 1.0.0
# @modified: your_name () Version: 1.0.1
#
# Example:
# You run logging to a file SUC_20241113.log using QCterminal tool.
# Use debug mask 0x7f it will log messages like:
# "DEB 09:59:40:046  StartPos(Target=0, Position=36000, Ctrl=0)"
# Running this script, a comment is appended
# "<<< SWF_MTD - Measuringhead Traverse Drive >>>"

# You can update comment strings in search_target_texts dictionary.

# To run from notepad++ use:
# python {Your_path}}\AnalyzeRxLogFiles\AddTargetTexts\AddTargetTexts.py "$(FULL_CURRENT_PATH)"
# Example:
# python C:/Users/urimrm/Projekty/Scripts/AnalyzeRxLogFiles/AddTargetTexts/AddTargetTexts.py "$(FULL_CURRENT_PATH)"

import os
import re
import sys

# Dictionary of strings to search for with their corresponding comments
search_target_texts = {
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
    for search_text, comment in search_target_texts.items():
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


fn = sys.argv[1]
# fn = "C:/Users/urimrm/Projekty/Rx/Documentation to R70/MyNotesToRx/R70_dbglogs/240821_SucLog/SUC_20240821_delete.log"
if os.path.exists(fn):
    print(fn)
    modify_file(fn)
