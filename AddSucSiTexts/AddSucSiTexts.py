# This script is used to comment log from R70 SUC.
# It will append a SUCSI text comment to log message.
#
# @author: Martin Imrich (martin.imrich@rieter.com)
# @modified: your_name
#
# Example:
# You run logging to a file SUC_20241113.log using QCterminal tool.
# Use debug mask 0x7f it will log messages like:
# "DEB 09:59:40:047  Send_SUCSI_Ctrl_Msg: SUCSI msg 02, Data0 25, Data1 00"
# Running this script, a comment is appended
# "<<< SUSI_STATE >, < YARNTRANSFER >>>"

# You can update comment strings in SUCSIstates.py.

# To run from notepad++ use:
# python {Your_path}}\AnalyzeRxLogFiles\AddSucSiTexts\AddSucSiTexts.py "$(FULL_CURRENT_PATH)"
# Example:
# python C:\Users\urimrm\Projekty\Scripts\AnalyzeRxLogFiles\AddSucSiTexts\AddSucSiTexts.py "$(FULL_CURRENT_PATH)"

import os
import re
import sys

from SUCSIstates import SUCSIState


def find_state_text(main_state, sub_state):
    for state in SUCSIState:
        if state['id'] == main_state:
            for sub in state['substates']:
                if sub['code'] == sub_state:
                    return f" <<< {state['text']} >, < {sub['text']} >>>"
    return ""


def modify_file(file_path):
    # Read the file contents
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Modify the contents
    modified_lines = []
    for line in lines:
        match = re.search(
            r'DEB \d{2}:\d{2}:\d{2}:\d{3}  Send_SUCSI_Ctrl_Msg: SUCSI msg ([0-9a-fA-F]+), Data0 ([0-9a-fA-F]+), Data1 ([0-9a-fA-F]+)', line)

        if match:
            main_state = int(match.group(1), 16)  # Convert from hex to decimal
            sub_state = int(match.group(2), 16)   # Convert from hex to decimal
            data1 = int(match.group(3), 16)       # Convert from hex to decimal
            print(match.group(1), main_state, match.group(2), sub_state)

            state_text = find_state_text(main_state, sub_state)
            line = line.strip() + state_text + "\n"

        modified_lines.append(line)

    # Write the modified contents back to the same file
    with open(file_path, 'w') as file:
        file.writelines(modified_lines)


fn = sys.argv[1]

if os.path.exists(fn):
    print(fn)
    modify_file(fn)
