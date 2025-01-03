# Map of Gui states on R70 SUC.
#
# @author: Martin Imrich (martin.imrich@rieter.com) Version: 1.0.0
# @modified: your_name () Version: 1.0.1

GUIState = [
    {'id': 0x00, 'text': 'Spinning unit fault', 'substates': [
        {'code': 0x00, 'text': " "},
        {'code': 0x01, 'text': " "},
        {'code': 0x02, 'text': " "},
        {'code': 0x03, 'text': " "},
        {'code': 0x04, 'text': " "},
        {'code': 0x05, 'text': " "},
        {'code': 0x06, 'text': " "},
        {'code': 0x07, 'text': " "}
    ]},
    {'id': 0x01, 'text': 'General fault', 'substates': [
        {'code': 0x00, 'text': " "},
        {'code': 0x01, 'text': " "},
        {'code': 0x02, 'text': " "},
        {'code': 0x03, 'text': " "},
        {'code': 0x04, 'text': " "},
        {'code': 0x05, 'text': " "},
        {'code': 0x06, 'text': " "},
        {'code': 0x07, 'text': " "}
    ]},
    {'id': 0x02, 'text': 'Operator call', 'substates': [
        {'code': 0x00, 'text': "Piecing is negative"},
        {'code': 0x01, 'text': "Sliver is missing"},
        {'code': 0x02, 'text': "Yarn not found"},
        {'code': 0x03, 'text': "REDIpac failed"},
        {'code': 0x04, 'text': "ROBOfeed failed"},
        {'code': 0x05, 'text': "Check tube"},
        {'code': 0x06, 'text': "OR is blocked"},
        {'code': 0x07, 'text': "Confirm PG change"},
        {'code': 0x08, 'text': "Yarn injection failed"},
        {'code': 0x09, 'text': "Check Yarn Suction"},
        {'code': 0x0A, 'text': "Check Loop Compensator"}
    ]},
    {'id': 0x03, 'text': 'Yarn alarm group 2', 'substates': [
        {'code': 0x00, 'text': " "},
        {'code': 0x01, 'text': " "},
        {'code': 0x02, 'text': " "},
        {'code': 0x03, 'text': " "},
        {'code': 0x04, 'text': " "},
        {'code': 0x05, 'text': " "},
        {'code': 0x06, 'text': " "},
        {'code': 0x07, 'text': " "}
    ]},
    {'id': 0x04, 'text': 'Yarn alarm group 1', 'substates': [
        {'code': 0x00, 'text': " "},
        {'code': 0x01, 'text': " "},
        {'code': 0x02, 'text': " "},
        {'code': 0x03, 'text': " "},
        {'code': 0x04, 'text': " "},
        {'code': 0x05, 'text': " "},
        {'code': 0x06, 'text': " "},
        {'code': 0x07, 'text': " "}
    ]},
    {'id': 0x05, 'text': 'Quality alarm', 'substates': [
        {'code': 0x00, 'text': " "},
        {'code': 0x01, 'text': " "},
        {'code': 0x02, 'text': " "},
        {'code': 0x03, 'text': " "},
        {'code': 0x04, 'text': " "},
        {'code': 0x05, 'text': " "},
        {'code': 0x06, 'text': " "},
        {'code': 0x07, 'text': " "}
    ]},
    {'id': 0x06, 'text': 'Quality alarm MPR', 'substates': [
        {'code': 0x00, 'text': " "},
        {'code': 0x01, 'text': " "},
        {'code': 0x02, 'text': " "},
        {'code': 0x03, 'text': " "},
        {'code': 0x04, 'text': " "},
        {'code': 0x05, 'text': " "},
        {'code': 0x06, 'text': " "},
        {'code': 0x07, 'text': " "}
    ]},
    {'id': 0x07, 'text': 'MPR', 'substates': [
        {'code': 0x00, 'text': " "},
        {'code': 0x01, 'text': "Initiated"},
        {'code': 0x02, 'text': "Done"},
        {'code': 0x03, 'text': " "},
        {'code': 0x04, 'text': " "},
        {'code': 0x05, 'text': " "},
        {'code': 0x06, 'text': " "},
        {'code': 0x07, 'text': " "}
    ]},
    {'id': 0x08, 'text': 'Stand by', 'substates': [
        {'code': 0x00, 'text': " "},
        {'code': 0x01, 'text': "Seed yarn needed"},
        {'code': 0x02, 'text': "Target length reached"},
        {'code': 0x03, 'text': "Yarn break"},
        {'code': 0x04, 'text': "Quality cut (<12m)"},
        {'code': 0x05, 'text': "Quality cut (>12m)"},
        {'code': 0x06, 'text': "Piecing is negative"},
        {'code': 0x07, 'text': "REDIpac is active"},
        {'code': 0x08, 'text': "Rotor cleaning active"},
        {'code': 0x09, 'text': "ROBOfeed is required"},
        {'code': 0x0A, 'text': "SU receives data"},
        {'code': 0x0B, 'text': "Spinning pos. locked"},
        {'code': 0x0C, 'text': "Avoid drag yarn"},
        {'code': 0x0D, 'text': "Yarn was not found"},
        {'code': 0x0E, 'text': "Waiting for CTS"},
        {'code': 0x0F, 'text': "Waiting for resources"},
        {'code': 0x10, 'text': "Forced stop"},
        {'code': 0x11, 'text': "PG not running"},
        {'code': 0x12, 'text': "Vacuum not OK"},
        {'code': 0x13, 'text': "Adjust speed"},
        {'code': 0x14, 'text': "Wait for permission"}
    ]},
    {'id': 0x09, 'text': 'Yarn is running', 'substates': [
        {'code': 0x00, 'text': " "},
        {'code': 0x01, 'text': "\"OFF\" is initiated"},
        {'code': 0x02, 'text': "Target length reached"},
        {'code': 0x03, 'text': " "},
        {'code': 0x04, 'text': " "},
        {'code': 0x05, 'text': " "},
        {'code': 0x06, 'text': " "},
        {'code': 0x07, 'text': " "}
    ]},
    {'id': 0x0A, 'text': 'Yarn break', 'substates': [
        {'code': 0x00, 'text': " "},
        {'code': 0x01, 'text': " "},
        {'code': 0x02, 'text': "Target length reached"},
        {'code': 0x03, 'text': " "},
        {'code': 0x04, 'text': " "},
        {'code': 0x05, 'text': " "},
        {'code': 0x06, 'text': " "},
        {'code': 0x07, 'text': " "}
    ]},
    {'id': 0x0B, 'text': 'Service', 'substates': [
        {'code': 0x00, 'text': " "},
        {'code': 0x01, 'text': "General"},
        {'code': 0x02, 'text': "Rotor"},
        {'code': 0x03, 'text': "WRD"},
        {'code': 0x04, 'text': "Page 4"},
        {'code': 0x05, 'text': "Page 5"},
        {'code': 0x06, 'text': "Page 6"},
        {'code': 0x07, 'text': "Page 7"}
    ]},
    {'id': 0x0C, 'text': 'OFF', 'substates': [
        {'code': 0x00, 'text': " "},
        {'code': 0x01, 'text': " "},
        {'code': 0x02, 'text': " "},
        {'code': 0x03, 'text': " "},
        {'code': 0x04, 'text': " "},
        {'code': 0x05, 'text': " "},
        {'code': 0x06, 'text': " "},
        {'code': 0x07, 'text': " "}
    ]},
    {'id': 0x0D, 'text': 'Process', 'substates': [
        {'code': 0x00, 'text': " "},
        {'code': 0x01, 'text': "\"OFF\" is initiated"},
        {'code': 0x02, 'text': " "},
        {'code': 0x03, 'text': "Homing is active"},
        {'code': 0x04, 'text': "Searching the yarn"},
        {'code': 0x05, 'text': "Transferring the yarn"},
        {'code': 0x06, 'text': "YEP is active"},
        {'code': 0x07, 'text': "Piecing is active"},
        {'code': 0x08, 'text': "Sync. acceleration"},
        {'code': 0x09, 'text': "Hand over to tube"},
        {'code': 0x0A, 'text': "Yarn is running"},
        {'code': 0x0B, 'text': "ROBOfeed is active"},
        {'code': 0x0C, 'text': "Avoid drag yarn"}
    ]},
    {'id': 0x0E, 'text': 'Cont. doffing', 'substates': [
        {'code': 0x00, 'text': " "},
        {'code': 0x01, 'text': " "},
        {'code': 0x02, 'text': " "},
        {'code': 0x03, 'text': " "},
        {'code': 0x04, 'text': " "},
        {'code': 0x05, 'text': " "},
        {'code': 0x06, 'text': " "},
        {'code': 0x07, 'text': " "}
    ]},
    {'id': 0x0F, 'text': 'VARIOspin', 'substates': [
        {'code': 0x00, 'text': " "},
        {'code': 0x01, 'text': " "},
        {'code': 0x02, 'text': "Target length reached"},
        {'code': 0x03, 'text': " "},
        {'code': 0x04, 'text': " "},
        {'code': 0x05, 'text': " "},
        {'code': 0x06, 'text': " "},
        {'code': 0x07, 'text': " "}
    ]},
    {'id': 0x10, 'text': 'TA', 'substates': [
        {'code': 0x00, 'text': " "},
        {'code': 0x01, 'text': "at the BC"},
        {'code': 0x02, 'text': "at the SUC"},
        {'code': 0x03, 'text': "at the RRD"},
        {'code': 0x04, 'text': "at the YC"},
        {'code': 0x05, 'text': "comm error to BC"},
        {'code': 0x06, 'text': "comm error to SUC"},
        {'code': 0x07, 'text': "comm error to RRD"},
        {'code': 0x08, 'text': "comm error to YC"},
        {'code': 0x09, 'text': " "},
        {'code': 0x0A, 'text': " "},
        {'code': 0x0B, 'text': " "}
    ]},
    {'id': 0x11, 'text': 'Reserve', 'substates': [
        {'code': 0x00, 'text': " "},
        {'code': 0x01, 'text': " "},
        {'code': 0x02, 'text': " "},
        {'code': 0x03, 'text': " "},
        {'code': 0x04, 'text': " "},
        {'code': 0x05, 'text': " "},
        {'code': 0x06, 'text': " "},
        {'code': 0x07, 'text': " "}
    ]}
]
