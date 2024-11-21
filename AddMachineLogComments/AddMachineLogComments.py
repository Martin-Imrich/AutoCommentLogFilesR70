# This script is used to comment log from R70 Machine.
# It will append a debug text comment to log message.
#
# @author: Martin Imrich (martin.imrich@rieter.com) Version: 1.0.0
# @modified: your_name () Version: 1.0.1
#
# Example:
# You download log files from machine log.
#
# "DEB 09:59:40:047  Send_SUCSI_Ctrl_Msg: SUCSI msg 02, Data0 25, Data1 00"
# Running this script, a comment is appended
# "<<< SUSI_STATE >, < YARNTRANSFER >>>"
#
# You can update comment strings in MachineLogMap.py.
#
# To run from notepad++ use:
# python {Your_path}}\AnalyzeRxLogFiles\AddMachineLogComments\AddMachineLogComments.py "$(FULL_CURRENT_PATH)"
# Example:
# python C:\Users\urimrm\Projekty\Scripts\AnalyzeRxLogFiles\AddMachineLogComments\AddMachineLogComments.py "$(FULL_CURRENT_PATH)"

import os
import re
import sys

from MachineLogMap import Debug_0x00, Debug_0x01, Debug_0x02, Debug_0x03, Debug_0x04


def get_debug_0_comment(substate: int) -> str:
    """
    Search for comment in Debug_0x00 dictionary.
    #comment = f" <<< {Debug_0x00['substates']}, {sub['text']} >>>"
    """
    comment: str = ""

    for sub in Debug_0x00['substates']:
        if sub['code'] == substate:
            comment = (
                f" <<< {Debug_0x00['text']},"
                f"     {sub['text']} >>>"
            )
            break

    return comment


def get_debug_1_comment() -> str:
    """
    Search for comment in Debug_0x01 dictionary.
    """
    comment: str = ""

    comment = (
        f" <<< {Debug_0x01['text']}, >>>"
    )
    return comment


def get_debug_2_comment() -> str:
    """
    Search for comment in Debug_0x02 dictionary.
    """
    comment: str = ""
    return comment


def get_debug_3_comment() -> str:
    """
    Search for comment in Debug_0x03 dictionary.
    """
    comment: str = ""

    comment = (
        f" <<< {Debug_0x03['text']}, >>>"
    )

    return comment


def get_debug_4_comment() -> str:
    """
    Search for comment in Debug_0x04 dictionary.
    """
    comment: str = ""
    return comment

    """
        for state in MEvt_Info:
            if state['id'] == main_state:
                for sub in state['substates']:
                    if sub['code'] == sub_state:
                        return f" <<< {state['text']} >, < {sub['text']} >>>"
        return ""
    """


def is_line_debug_message(line: str) -> bool:
    """
    Check if a line matches the debug message pattern.

    Args:
        line (str): The line to check.

    Returns:
        bool: True if the line matches the debug pattern, otherwise False.
    """
    debug_pattern = (
        r"MEvt Info.*?Debug (?P<val1>0x[0-9a-fA-F]+)\s+"
        r"(?P<val2>0x[0-9a-fA-F]+)\s+"
        r"(?P<val3>0x[0-9a-fA-F]+)\s+"
        r"(?P<val4>0x[0-9a-fA-F]+)"
    )

    return bool(re.search(debug_pattern, line))


def get_debug_message_comment(line: str) -> str:
    """
    Extract data from debug message and return
    the appropriate comment for a debug message
    in the line.

    Args:
        line (str): The line containing the debug message.

    Returns:
        str: The comment for the debug message.
    """
    comment = ""

    # r"MEvt Info.*?Debug (?P<val1>0x[0-9a-fA-F]+)\s+(?P<val2>0x[0-9a-fA-F]+)\s+(?P<val3>0x[0-9a-fA-F]+)\s+(?P<val4>0x[0-9a-fA-F]+)",
    debug_pattern = (
        r"MEvt Info.*?Debug (?P<val1>0x[0-9a-fA-F]+)\s+"
        r"(?P<val2>0x[0-9a-fA-F]+)\s+"
        r"(?P<val3>0x[0-9a-fA-F]+)\s+"
        r"(?P<val4>0x[0-9a-fA-F]+)"
    )

    debug_match = re.search(debug_pattern, line)

    if debug_match:
        # Extract and convert values from the debug message
        category = int(debug_match.group("val1"), 16)
        data0 = int(debug_match.group("val2"), 16)
        data1 = int(debug_match.group("val3"), 16)
        data2 = int(debug_match.group("val4"), 16)

        # Use a mapping for better scalability
        if category == Debug_0x00['Debug_id']:
            comment = get_debug_0_comment(data0)
        elif category == Debug_0x01['Debug_id']:
            comment = get_debug_1_comment()
        elif category == Debug_0x02['Debug_id']:
            comment = get_debug_2_comment()
        elif category == Debug_0x03['Debug_id']:
            comment = get_debug_3_comment()
        elif category == Debug_0x04['Debug_id']:
            comment = get_debug_4_comment()

    if comment == "":
        print(line)

    return comment


def modify_file(file_path) -> None:
    """
    Search for comment in Debug_0xXX dictionary.
    """

    # Read the file contents
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Modify the contents
    modified_lines = []
    for line in lines:
        if is_line_debug_message(line):
            line = line.strip() + get_debug_message_comment(line) + "\n"

        modified_lines.append(line)

    # Write the modified contents back to the same file
    with open(file_path, 'w') as file:
        file.writelines(modified_lines)


# run command in notepad++ python:
# python C:\Users\urimrm\Projekty\Scripts\AnalyzeRxLogFiles\dbglog_comment\dbglog_comment.py "$(FULL_CURRENT_PATH)"

# fn = sys.argv[1]
fn = 'C:/Users/urimrm/Projekty/Rx/Documentation to R70/MyNotesToRx/R70_Velen/02_Feeder_running/SUC002_01.txt'

# option = sys.argv[2]  # Option
option = "Debug_all"

option_list = ["Debug_all", "Debug_0",
               "Debug_1", "Debug_2",
               "Debug_3", "Debug_4"]

if option not in option_list:
    option = "Debug_all"  # search in all dbglog_map dictionaries

#

if os.path.exists(fn):
    print(fn)
    modify_file(fn)
