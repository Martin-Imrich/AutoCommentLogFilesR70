# Map file for a machine log file
#
# @author: Martin Imrich (martin.imrich@rieter.com) Version: 1.0.0
# @modified: your_name () Version: 1.0.1
#
# Debug shortcuts:
# - AS(automatic service), PY(piecing to yarn), SY(seed yarn),
# - MSL(Machine side left), MSR(Machine side right),
# - ??
# - BA? = AS: PY piecing failed with BA,
#
# Example:
# Nov 13 16: 28: 58 [INF] MEH LP: MEvt Info 17000(67) SI.3 SpP.61 Debug 0x00  0x2D 0x01 0x00 0x00
# Nov 13 15: 39: 52 [INF] MEH LP: MEvt Info 20100(69) SUC.61 Debug 0x01  0x10 0x16 0x00 0x00 << < Technical Alarms >> >
# Nov 13 16: 17: 41 [INF] MEH LP: MEvt Info 20100(69) SUC.61 Debug 0x02  0x1B 0x22 0x00 0x00
# Nov 13 16: 20: 21 [INF] MEH LP: MEvt Info 17000(67) SI.3 SpP.61 Debug 0x03  0x02 0x00 0x01 0x2A
# Nov 13 16: 28: 58 [INF] MEH LP: MEvt Info 20100(69) SUC.61 Debug 0x04  0x02 0x04 0x00 0x00

# Definition files:
# C:\Users\urimrm\Projekty\Rx\R70\SC_newAPI\SW\Common\ASW\MEH_DEF.h

# Explanation:
# Numbers:
# - 17000(67) = MEH_SI_BASE
# - 20100(69) = MEH_SUC_BASE

"""
Example:
Line 450: Nov 13 15:40:10 [INF] McCtrl BE: 33F03006 SC3>MC:   Emergency event! Code 0x30 0x06 // EMCY invalidate transition=(0x30), Transition ?? = 0x06
Line 452: Nov 13 15:40:10 [INF] McCtrl BE: 33F03008 SC3>MC:   Emergency event! Code 0x30 0x08
Line 453: Nov 13 15:40:10 [INF] McCtrl BE: 33F03008 SC3>MC:   Emergency event! Code 0x30 0x08
Line 467: Nov 13 15:41:04 [INF] McCtrl BE: 33F03006 SC3>MC:   Emergency event! Code 0x30 0x06
Line 468: Nov 13 15:41:04 [INF] McCtrl BE: 33F03008 SC3>MC:   Emergency event! Code 0x30 0x08 //
Line 469: Nov 13 15:41:04 [INF] McCtrl BE: 33F03010 SC3>MC:   Emergency event! Code 0x30 0x10

Emergency event! Code 0x30 0x06 // EMCY invalidate transition=(0x30), Transition 0x06 =  ??
Emergency event! Code 0x30 0x08 // EMCY invalidate transition=(0x30), Transition 0x08 =  (neso s yarn run)
Emergency event! Code 0x30 0x08
Emergency event! Code 0x30 0x06
Emergency event! Code 0x30 0x08 //
Emergency event! Code 0x30 0x10 // EMCY invalidate transition=(0x30), State 0x10 = slave TA
"""

Debug_0x00 = {
    "Debug_id": 0x00,
    "description": "None",
    "const": "MEH___SI_STATE_CHG",
    "text": "SUSI_STATE",  # SUSI_SUMA_STATE__
    "substates": [
            {'code': 0x00, 'text': "OK"},
            {'code': 0x01, 'text': "UNIT_OPEN"},
            {'code': 0x02, 'text': "YR"},
            {'code': 0x03, 'text': "CUT_CONFIRM"},
            {'code': 0x04, 'text': "REF_STARTPIECING"},
            {'code': 0x05, 'text': "Unknown"},
            #
            {'code': 0x06, 'text': "Unknown"},
            #
            {'code': 0x20, 'text': "OFFS"},
            {'code': 0x23, 'text': "HOMING"},
            {'code': 0x24, 'text': "YARN_SEARCH"},
            {'code': 0x25, 'text': "YARN_TRANSFER"},
            {'code': 0x26, 'text': "YARN_PREPARATION"},
            {'code': 0x27, 'text': "PIECING"},
            {'code': 0x28, 'text': "SYNC"},
            {'code': 0x29, 'text': "HANDOVER"},
            {'code': 0x2A, 'text': "SPINNING"},
            {'code': 0x2B, 'text': "ROBOFEED"},  # SUSI_SUMA_STATE__ROBOFEED
            {'code': 0x2D, 'text': "CLEANING"},  # SUSI_SUMA_STATE__CLEANING
            # 01: CLEANING_STARTED
            # 02: CLEANING_ALMOST_FINISHED
            # 03: CLEANING_READY
            {'code': 0x2C, 'text': "DRAG_YARN_SEQ"},
            {'code': 0x2E, 'text': "REDIpac"},
            # SUSI_SUMA_STATE__MAN_SLIV_PREP
            {'code': 0x2F, 'text': "MAN_SLIV_PREP"},
            # 01: MAN_SLIV_PREP_STARTED
            # 02: MAN_SLIV_PREP_ALMOST_FINISHED
            # 03: MAN_SLIV_PREP_READY
            {'code': 0x30, 'text': "SERVICE"},
            # SUSI_SUMA_STATE__MEC_ROTOR_CLEAN -  Mechanical Rotor cleaning
            {'code': 0x31, 'text': "Rotor cleaning - Without Robot"},
            # 01: MEC_ROTOR_CLEAN_STARTED
            # 02: MEC_ROTOR_CLEAN_ALMOST_FINISHED
            # 03: MEC_ROTOR_CLEAN_READY
            # SUSI_SUMA_STATE__WUF_CLEAN_SEQ
            {'code': 0x32, 'text': "WUF_CLEAN_SEQ"},
            {'code': 0x33, 'text': "MomMa Ready"},
            {'code': 0x34, 'text': "SuMa Ready"},  # SuMa ready
            {'code': 0x93, 'text': "STARTUP_PREPARED"},
            {'code': 0x94, 'text': "STARTED_UP"},
            {'code': 0x95, 'text': "OD_SWITCHED"},
    ]
}

Debug_0x01 = {
    'Debug_id': 0x01,
    'description': "Automatically Confirmed Errors (messages in SI defined)",
    'const': "MEH___SI_STATE_CHG",
    'text': 'Autoconfirm at',
    'substates': [
        {'code': 0x00, 'text': "None",
            'substates': [
                {'code': 0x00, 'text': "None"},
            ]
         },
        {'code': 0x01, 'text': "SUC",
            'substates': [
                {'code': 0x00, 'text': "Undefined"},
            ]
         },
        {'code': 0x10, 'text': "BC, ",
            'substates': [
                {'code': 0x00, 'text': "Undefined"},
                {'code': 0x16, 'text': "Sliver Feeding drive"},
            ]
         },
        {'code': 0x70, 'text': "Robot or Rotor",
            'substates': [
                {'code': 0x00, 'text': "Undefined"},
            ]
         },
        {'code': 0x90, 'text': "Robot Control",
            'substates': [
                {'code': 0x00, 'text': "Missing Signal from robot"},
            ]
         },
        {'code': 0xA0, 'text': "No Valid Parameter",
            'substates': [
                {'code': 0x00, 'text': "Undefined"},
            ]
         },
    ],
}

Debug_0x02 = {
    'Debug_id': 0x02,
    'description': "None",
    'const': "?",
    'text': 'None',
    'substates': [
            {'code': 0x00, 'text': "None",
             'substates': [
                 {'code': 0x00, 'text': "None"},
             ]
             },
    ],
}

Debug_0x03 = {
    'Debug_id': 0x03,
    'description': "Statistics 0x03, 0x01 trial, 0x24 phase(piecing ends in phaers 24), Additional info",
    'const': "?",
    'text': 'Statistics',
    'substates': [
        {'code': 0x00, 'text': "None",
            'substates': [
                {'code': 0x00, 'text': "Undefined"},
            ]
         },
    ],
}

Debug_0x04 = {
    'Debug_id': 0x04,
    'description': "?",
    'const': "?",
    'text': '?',
    'substates': [
        {'code': 0x00, 'text': "None",
            'substates': [
                {'code': 0x00, 'text': "Undefined"},
            ]
         },
    ],
}
