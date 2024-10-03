#
# SU communicate with SI on messages Send_SUCSI_Ctrl_Msg:
# Send_SUCSI_Ctrl_Msg: SUCSI msg 08, Data0 05, Data1 00 is send to sth Robot

import os
import sys
import re
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
        match = re.search(r'DEB \d{2}:\d{2}:\d{2}:\d{3}  Send_SUCSI_Ctrl_Msg: SUCSI msg (\d+), Data0 (\d+), Data1 (\d+)', line)
        if match:
            main_state = int(match.group(1))
            sub_state = int(match.group(2))
            state_text = find_state_text(main_state, sub_state)
            line = line.strip() + state_text + "\n"
        modified_lines.append(line)

    # Write the modified contents back to the same file
    with open(file_path, 'w') as file:
        file.writelines(modified_lines)

# run command in notepad++ python:
# python C:\Users\urimrm\Projekty\Scripts\AnalyzeRxLogFiles\AddSUCSI\AddSUCSI.py "$(FULL_CURRENT_PATH)"
fn = sys.argv[1]
if os.path.exists(fn):
    print(fn)
    modify_file(fn)
