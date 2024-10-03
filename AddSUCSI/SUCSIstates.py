"""/*----------------------------------------------------------------------------
 *      Communication SU/SUC => SI <- ./SC_newAPI\SW\Specific\SUC\ASW\CAN\CAN_DEF_XXBC.h
 *---------------------------------------------------------------------------*/

 SISU_CTRL__ SI sends to SU

MM_fct_RC_PIECING_POS
DEB 17:04:08:850  Send_SUCSI_Ctrl_Msg: SUCSI msg 08, Data0 04, Data1 00 -> Send_SUCSI_Ctrl_Msg(SUSI_RCCTRL, SUSI_RCCTRL_PIECING_POSITIVE, UNDEF);
DEB 17:04:08:850  Send_SUCSI_Ctrl_Msg: SUCSI msg 08, Data0 06, Data1 00 -> Send_SUCSI_Ctrl_Msg(SUSI_RCCTRL, SUSI_RCCTRL_RDY_FOR_BUILD_TRANS_TAIL, UNDEF);
DEB 17:03:16:918  Send_SUCSI_Ctrl_Msg: SUCSI msg 02, Data0 04, Data1 00 <<< SUSI_STATE >, <   >>>
"""

SUCSIState = [
    {'id': 0x01, 'text': 'SUSI_DBG', 'substates': [
        {'code': 0x00, 'text': " "},
        {'code': 0x01, 'text': " "},
        {'code': 0x02, 'text': " "},
        {'code': 0x03, 'text': " "},
        {'code': 0x04, 'text': " "},
        {'code': 0x05, 'text': " "},
        {'code': 0x06, 'text': " "},
        {'code': 0x07, 'text': " "},
        {'code': 0x08, 'text': " "}
    ]},
    {'id': 0x02, 'text': 'SUSI_STATE', 'substates': [
        {'code': 0x00, 'text': "OK"},
        {'code': 0x01, 'text': "UNIT_OPEN"},
        {'code': 0x02, 'text': "YR"},
        {'code': 0x03, 'text': "CUT_CONFIRM"},
        {'code': 0x04, 'text': "REF_STARTPIECING"},
        {'code': 0x20, 'text': "OFFS"},
        {'code': 0x23, 'text': "HOMING"},
        {'code': 0x24, 'text': "YARNSEARCH"},
        {'code': 0x25, 'text': "YARNTRANSFER"},
        {'code': 0x26, 'text': "YARNPREP"},
        {'code': 0x27, 'text': "PIECING"},
        {'code': 0x28, 'text': "SYNC"},
        {'code': 0x29, 'text': "HANDOVER"},
        {'code': 0x2A, 'text': "SPINNING"},
        {'code': 0x2C, 'text': "DRAG_YARN_SEQ"},
        {'code': 0x2E, 'text': "REDIpac"},
        {'code': 0x30, 'text': "SERVICE"},
        {'code': 0x33, 'text': "READY"},
        {'code': 0x93, 'text': "STARTUP_PREPARED"},
        {'code': 0x94, 'text': "STARTED_UP"},
        {'code': 0x95, 'text': "OD_SWITCHED"},
    ]},
    {'id': 0x03, 'text': 'SUSI_HMI', 'substates': [
        {'code': 0x00, 'text': "OK"},
        {'code': 0x01, 'text': "OPERATOR_ACTION"},
        {'code': 0x02, 'text': "SERVICEMODEREQ"},
        {'code': 0x03, 'text': "OFFREQ"},
        {'code': 0x04, 'text': "POW_OFFREQ"},
        {'code': 0x05, 'text': "ADD_BUTTON_ACTION"},
        {'code': 0x06, 'text': "ADD_BUTTON_B_ACTION"},
        {'code': 0x07, 'text': "SERVICE_MODE_REQ"}
    ]},
    {'id': 0x04, 'text': 'SUSI_INFO', 'substates': [
        {'code': 0x00, 'text': " "},
        {'code': 0x01, 'text': " "},
        {'code': 0x02, 'text': " "},
        {'code': 0x03, 'text': " "},
        {'code': 0x04, 'text': " "},
        {'code': 0x05, 'text': " "},
        {'code': 0x06, 'text': " "},
        {'code': 0x07, 'text': " "},
        {'code': 0x08, 'text': " "}
    ]},
    {'id': 0x05, 'text': 'SUSI_ALARM_COMM', 'substates': [
        {'code': 0x00, 'text': " "},
        {'code': 0x01, 'text': " "},
        {'code': 0x02, 'text': " "},
        {'code': 0x03, 'text': " "},
        {'code': 0x04, 'text': " "},
        {'code': 0x05, 'text': " "},
        {'code': 0x06, 'text': " "},
        {'code': 0x07, 'text': " "},
        {'code': 0x08, 'text': " "}
    ]},
    {'id': 0x06, 'text': 'SUSI_ALARM_TECH_GEN', 'substates': [
        {'code': 0x00, 'text': " "},
        {'code': 0x01, 'text': " "},
        {'code': 0x02, 'text': " "},
        {'code': 0x03, 'text': " "},
        {'code': 0x04, 'text': " "},
        {'code': 0x05, 'text': " "},
        {'code': 0x06, 'text': " "},
        {'code': 0x07, 'text': " "},
        {'code': 0x08, 'text': " "}
    ]},
    {'id': 0x07, 'text': 'SUSI_ALARM_TECH_SPEC', 'substates': [
        {'code': 0x00, 'text': " "},
        {'code': 0x01, 'text': " "},
        {'code': 0x02, 'text': " "},
        {'code': 0x03, 'text': " "},
        {'code': 0x04, 'text': " "},
        {'code': 0x05, 'text': " "},
        {'code': 0x06, 'text': " "},
        {'code': 0x07, 'text': " "},
        {'code': 0x08, 'text': " "}
    ]},
    {'id': 0x08, 'text': ' < Robot > ', 'substates': [ # SUSI_RCCTRL
        {'code': 0x00, 'text': "CLEANING_READY"},
        {'code': 0x01, 'text': "CLEANING_UNDERPRESSURE_ON"},
        {'code': 0x02, 'text': "CLEANING_BOX_CLOSED"},
        {'code': 0x03, 'text': "RDY_FOR_PIECING"},
        {'code': 0x04, 'text': "PIECING_POSITIVE"},
        {'code': 0x05, 'text': "PIECING_NEGATIVE"},
        {'code': 0x06, 'text': "RDY_FOR_BUILD_TRANS_TAIL"},
        {'code': 0x07, 'text': "TRANS_TAIL_LEN_OK"},
        {'code': 0x08, 'text': "AVOID_DRAG_YARN"},
        {'code': 0x09, 'text': "START_BLOWING_OPEING_UNIT"},
        {'code': 0x0A, 'text': "SUCTION_UNIT_DOCK"},
        {'code': 0x0B, 'text': "SUCTION_UNIT_UNDOCK"},
        {'code': 0x0C, 'text': "PREPARE_SLIVER"},
        {'code': 0x0D, 'text': "SLIVER_TO_FUNNEL"},
        {'code': 0x0E, 'text': "SLIVER_TRANSFER"},
        {'code': 0x0F, 'text': "FEEDUNIT_HOME"},
        {'code': 0x10, 'text': "SWIVEL_GUID_RAIL"},
        {'code': 0x11, 'text': "GUID_UNITS_HOMEPOS"},
        {'code': 0x80, 'text': "TERMINATE_HANGUP_SU"},
        {'code': 0x81, 'text': "TERMINATE_HANGUP_RC"},
        {'code': 0x82, 'text': "TERMINATE_TA"}
    ]},
    {'id': 0x09, 'text': 'YMS', 'substates': [ # SUSI_YR_CTRL_CHANNEL
        {'code': 0x00, 'text': "yarn break signal"},
        {'code': 0x01, 'text': "yarn run signal"},
    ]},
    {'id': 0x0a, 'text': 'SUSI_SUMA_STATE', 'substates': [
        {'code': 0x00, 'text': " "},
        {'code': 0x01, 'text': " "},
        {'code': 0x02, 'text': " "},
        {'code': 0x03, 'text': " "},
        {'code': 0x04, 'text': " "},
        {'code': 0x05, 'text': " "},
        {'code': 0x06, 'text': " "},
        {'code': 0x07, 'text': " "},
        {'code': 0x08, 'text': " "}
    ]},
    {'id': 0x0b, 'text': 'SUSI_RESOURCE_REQUEST', 'substates': [
        {'code': 0x00, 'text': " "},
        {'code': 0x01, 'text': " "},
        {'code': 0x02, 'text': " "},
        {'code': 0x03, 'text': " "},
        {'code': 0x04, 'text': " "},
        {'code': 0x05, 'text': " "},
        {'code': 0x06, 'text': " "},
        {'code': 0x07, 'text': " "},
        {'code': 0x08, 'text': " "}
    ]},
    {'id': 0x0c, 'text': 'SUSI_LAST', 'substates': [
        {'code': 0x00, 'text': " "},
        {'code': 0x01, 'text': " "},
        {'code': 0x02, 'text': " "},
        {'code': 0x03, 'text': " "},
        {'code': 0x04, 'text': " "},
        {'code': 0x05, 'text': " "},
        {'code': 0x06, 'text': " "},
        {'code': 0x07, 'text': " "},
        {'code': 0x08, 'text': " "}
    ]}
]

