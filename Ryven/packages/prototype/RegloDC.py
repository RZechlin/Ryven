from NENV import *

class RegloDC_NodeBase(Node):

    style = 'normal'
    color = '#3283a8'


class DeviceServicer_GetLog(RegloDC_NodeBase):
    """"""
    title = 'SiLA//RegloDC - Get Log'
    init_inputs = [
        NodeInputBP(type_='exec', label='GetLog'),
        #NodeInputBP(dtype=dtypes.Integer(), label='RPM'),
        #NodeInputBP(dtype=dtypes.Boolean(), label='Direction')
    ]

    init_outputs = [
        NodeOutputBP(label='GetLog', type_='data'),
        NodeOutputBP(label='CurrentStatus', type_='data'),
        #NodeOutputBP(type_='exec'),
        #NodeOutputBP('RPM', type_='data'),
    ]

    def __init__(self, params):
        super().__init__(params)

    # Outputs CurrentStatus parameter
    def getCurrentStatus(self):
        return


class DeviceServicer_SetPumpAddress(RegloDC_NodeBase):
    """Set the address of the pump (1-8)."""

    title = 'SiLA//RegloDC - Set Pump Address'
    init_inputs = [
        NodeInputBP(type_='exec'),
        NodeInputBP(dtype=dtypes.Integer(), label=''),
    ]
    init_outputs = [
        NodeOutputBP('', type_='exec'),
        NodeOutputBP('', type_='data'),
    ]

    def __init__(self, params):
        super().__init__(params)

    def update_event(self, inp=-1):
        if inp == 0:
            self.exec_output(0)


class DeviceServicer_GetPumpSatus(RegloDC_NodeBase):
    """Get pump status. +=running, -=stopped/standby."""

    title = 'SiLA//RegloDC - Get Pump Status'
    init_inputs = [
        NodeInputBP(type_='exec'),
        NodeInputBP(dtype=dtypes.Integer(), label=''),
    ]
    init_outputs = [
        NodeOutputBP('', type_='exec'),
        NodeOutputBP('', type_='data'),
    ]

    def __init__(self, params):
        super().__init__(params)

    def update_event(self, inp=-1):
        if inp == 0:
            self.exec_output(0)


class DeviceServicer_GetVersionType(RegloDC_NodeBase):
    """Get pump information. Response is string of model description (variable length), software version (3 digits) 
    and pump head model type code (3 digits)."""

    title = 'SiLA//RegloDC - Get Version Type'
    init_inputs = [
        NodeInputBP(type_='exec'),
        NodeInputBP(dtype=dtypes.Integer(), label=''),
    ]
    init_outputs = [
        NodeOutputBP('', type_='exec'),
        NodeOutputBP('', type_='data'),
    ]

    def __init__(self, params):
        super().__init__(params)

    def update_event(self, inp=-1):
        if inp == 0:
            self.exec_output(0)


class DeviceServicer_GetVersionSoftware(RegloDC_NodeBase):
    """Get pump software version. Response is string."""

    title = 'SiLA//RegloDC - Current Version Software'
    init_inputs = [
        NodeInputBP(type_='exec'),
        NodeInputBP(dtype=dtypes.Integer(), label=''),
    ]
    init_outputs = [
        NodeOutputBP('', type_='exec'),
        NodeOutputBP('', type_='data'),
    ]

    def __init__(self, params):
        super().__init__(params)

    def update_event(self, inp=-1):
        if inp == 0:
            self.exec_output(0)


class DeviceServicer_GetPumpID(RegloDC_NodeBase):
    """Get pump head identification number."""

    title = 'SiLA//RegloDC - Get Pump ID'
    init_inputs = [
        NodeInputBP(type_='exec'),
        NodeInputBP(dtype=dtypes.Integer(), label=''),
    ]
    init_outputs = [
        NodeOutputBP('', type_='exec'),
        NodeOutputBP('', type_='data'),
    ]

    def __init__(self, params):
        super().__init__(params)

    def update_event(self, inp=-1):
        if inp == 0:
            self.exec_output(0)


class DeviceServicer_SetPumpID(RegloDC_NodeBase):
    """Set pump head identification number"""

    title = 'SiLA//RegloDC - Set Pump ID'
    init_inputs = [
        NodeInputBP(type_='exec'),
        NodeInputBP(dtype=dtypes.Integer(), label=''),
    ]
    init_outputs = [
        NodeOutputBP('', type_='exec'),
        NodeOutputBP('', type_='data'),
    ]

    def __init__(self, params):
        super().__init__(params)

    def update_event(self, inp=-1):
        if inp == 0:
            self.exec_output(0)


class DeviceServicer_ResetToDefault(RegloDC_NodeBase):
    """Resets all user configurable data to default values."""

    title = 'SiLA//RegloDC - Reset To Default'
    init_inputs = [
        NodeInputBP(type_='exec'),
        NodeInputBP(dtype=dtypes.Integer(), label=''),
    ]
    init_outputs = [
        NodeOutputBP('', type_='exec'),
        NodeOutputBP('', type_='data'),
    ]

    def __init__(self, params):
        super().__init__(params)

    def update_event(self, inp=-1):
        if inp == 0:
            self.exec_output(0)


class DeviceServicer_GetTotalVolume(RegloDC_NodeBase):
    """Get total volume pumped since last reset, in muL, mL, or L."""

    title = 'SiLA//RegloDC - Get Total Volume'
    init_inputs = [
        NodeInputBP(type_='exec'),
        NodeInputBP(dtype=dtypes.Integer(), label=''),
    ]
    init_outputs = [
        NodeOutputBP('', type_='exec'),
        NodeOutputBP('', type_='data'),
    ]

    def __init__(self, params):
        super().__init__(params)

    def update_event(self, inp=-1):
        if inp == 0:
            self.exec_output(0)

class DeviceServicer_UnlockControlPanel(RegloDC_NodeBase):
    """Switch control panel to manual operation."""

    title = 'SiLA//RegloDC - Unlock Control Panel'
    init_inputs = [
        NodeInputBP(type_='exec'),
    ]
    init_outputs = [
        NodeOutputBP('', type_='exec'),
        NodeOutputBP('Response', type_='data'),
    ]

    def __init__(self, params):
        super().__init__(params)

    def update_event(self, inp=-1):
        if inp == 0:
            response = "Control panel switched to manual operation."
            self.exec_output(0)
            self.set_output_val(1, response)


class DeviceServicer_LockControlPanel(RegloDC_NodeBase):
    """Set control panel to inactive (Input via control keys is not possible)."""

    title = 'SiLA//RegloDC - Lock Control Panel'
    init_inputs = [
        NodeInputBP(type_='exec'),
    ]
    init_outputs = [
        NodeOutputBP('', type_='exec'),
        NodeOutputBP('Response', type_='data'),
    ]

    def __init__(self, params):
        super().__init__(params)

    def update_event(self, inp=-1):
        if inp == 0:
            response = "The control panel has been locked"
            self.exec_output(0)
            self.set_output_val(1, response)


class DeviceServicer_SetDisplayNumbers(RegloDC_NodeBase):
    """Write numbers to the pump to display while under external control 
    - float of length 5 including +/- and decimal points."""

    title = 'SiLA//RegloDC - Set Display Numbers'
    init_inputs = [
        NodeInputBP(type_='exec'),
        NodeInputBP(dtype=dtypes.Integer(), label=''),
    ]
    init_outputs = [
        NodeOutputBP('', type_='exec'),
        NodeOutputBP('', type_='data'),
    ]

    def __init__(self, params):
        super().__init__(params)

    def update_event(self, inp=-1):
        if inp == 0:
            self.exec_output(0)


class DeviceServicer_SetDisplayLetters(RegloDC_NodeBase):
    """Write letters to the pump to display while under external control - 
    string of length 4."""

    title = 'SiLA//RegloDC - Set Display Letters'
    init_inputs = [
        NodeInputBP(type_='exec'),
        NodeInputBP(dtype=dtypes.Integer(), label=''),
    ]
    init_outputs = [
        NodeOutputBP('', type_='exec'),
        NodeOutputBP('', type_='data'),
    ]

    def __init__(self, params):
        super().__init__(params)

    def update_event(self, inp=-1):
        if inp == 0:
            self.exec_output(0)


class DeviceServicer_SetCommunicationPort(RegloDC_NodeBase):
    """Set pump head identification number."""

    title = 'SiLA//RegloDC - Set Pump ID'
    init_inputs = [
        NodeInputBP(type_='exec'),
        NodeInputBP(dtype=dtypes.Integer(), label=''),
    ]
    init_outputs = [
        NodeOutputBP('', type_='exec'),
        NodeOutputBP('', type_='data'),
    ]

    def __init__(self, params):
        super().__init__(params)

    def update_event(self, inp=-1):
        if inp == 0:
            self.exec_output(0)


class DeviceServicer_ConnectDevice(RegloDC_NodeBase):
    """Sets up a serial connection with the device using the specified connection details."""

    title = 'SiLA//RegloDC - Connect Device'
    init_inputs = [
        NodeInputBP(type_='exec'),
        NodeInputBP(dtype=dtypes.Integer(), label=''),
    ]
    init_outputs = [
        NodeOutputBP('', type_='exec'),
        NodeOutputBP('', type_='data'),
    ]

    def __init__(self, params):
        super().__init__(params)

    def update_event(self, inp=-1):
        if inp == 0:
            self.exec_output(0)


class DeviceServicer_ResetOverload(RegloDC_NodeBase):
    """Reset the device command input buffer overload."""

    title = 'SiLA//RegloDC - Reset Overload'
    init_inputs = [
        NodeInputBP(type_='exec'),
        NodeInputBP(dtype=dtypes.Integer(), label=''),
    ]
    init_outputs = [
        NodeOutputBP('', type_='exec'),
        NodeOutputBP('', type_='data'),
    ]

    def __init__(self, params):
        super().__init__(params)

    def update_event(self, inp=-1):
        if inp == 0:
            self.exec_output(0)


class DeviceServicer_Properties(RegloDC_NodeBase):
    """All properties"""

    title = 'SiLA//RegloDC - Properties'
    init_inputs = [
        #NodeInputBP(type_='exec'),
        #NodeInputBP(dtype=dtypes.Integer(), label=''),
    ]
    init_outputs = [
        NodeOutputBP('', type_='exec'),
        NodeOutputBP('', type_='data'),
    ]

    def __init__(self, params):
        super().__init__(params)

    def update_event(self, inp=-1):
        if inp == 0:
            self.exec_output(0)


deviceServicer_nodes = [
    DeviceServicer_GetLog,
    DeviceServicer_SetPumpAddress,
    DeviceServicer_GetPumpSatus,
    DeviceServicer_GetVersionType,
    DeviceServicer_GetVersionSoftware,
    DeviceServicer_GetPumpID,
    DeviceServicer_SetPumpID,
    DeviceServicer_ResetToDefault,
    DeviceServicer_GetTotalVolume,
    DeviceServicer_LockControlPanel,
    DeviceServicer_UnlockControlPanel,
    DeviceServicer_SetDisplayNumbers,
    DeviceServicer_SetDisplayLetters,
    DeviceServicer_SetCommunicationPort,
    DeviceServicer_ConnectDevice,
    DeviceServicer_ResetOverload,
    DeviceServicer_Properties,
]


class DriveControlServicer_SetDirectionClockwise(RegloDC_NodeBase):
    """Set the rotation direction of the pump to clockwise"""

    title = 'SiLA//RegloDC - Set Direction to clockwise'
    init_inputs = [
        NodeInputBP(type_='exec'),
    ]
    init_outputs = [
        NodeOutputBP('', type_='exec'),
        NodeOutputBP('Response', type_='data'),
    ]

    def __init__(self, params):
        super().__init__(params)

    def update_event(self, inp=-1):
        if inp == 0:
            response = "Set direction to clockwise succeeded to set."
            self.exec_output(0)
            self.set_output_val(1, response)


class DriveControlServicer_StartPump(RegloDC_NodeBase):
    """Starts the pump out of stand-by mode."""

    title = 'SiLA//RegloDC - Start Pump'
    init_inputs = [
        NodeInputBP(type_='exec'),
    ]
    init_outputs = [
        NodeOutputBP('', type_='exec'),
        NodeOutputBP('Start Status', type_='data'),
    ]

    def __init__(self, params):
        super().__init__(params)

    def update_event(self, inp=-1):
        if inp == 0:
            response = "Start of pump succeeded."
            self.exec_output(0)
            self.set_output_val(1, response)


class DriveControlServicer_StopPump(RegloDC_NodeBase):
    """Stops all channels of the pump."""

    title = 'SiLA//RegloDC - Stop Pump'
    init_inputs = [
        NodeInputBP(type_='exec'),
    ]
    init_outputs = [
        NodeOutputBP('', type_='exec'),
        NodeOutputBP('Stop Status', type_='data'),
    ]

    def __init__(self, params):
        super().__init__(params)

    def update_event(self, inp=-1):
        if inp == 0:
            response = "Shut-down of pump succeeded."
            self.exec_output(0)
            self.set_output_val(1, response)



driveControlServicer_nodes = [
    DriveControlServicer_SetDirectionClockwise,
    DriveControlServicer_StartPump,
    DriveControlServicer_StopPump,
]

class ParameterControlServicer_SetRPM(RegloDC_NodeBase):
    """Set pump speed in rpm (100 - 10000 (4 channel type); 160 - 16000 (2 channel type))."""

    title = 'SiLA//RegloDC - Set RPM'
    init_inputs = [
        NodeInputBP(type_='exec'),
        NodeInputBP(dtype=dtypes.Integer(), label='RPM'),
    ]
    init_outputs = [
        NodeOutputBP('', type_='exec'),
        NodeOutputBP('', type_='data'),
    ]

    def __init__(self, params):
        super().__init__(params)

    def update_event(self, inp=-1):
        if inp == 0:
            response = "RPM successfully set"
            self.exec_output(0)
            self.set_output_val(1, response)

parameterControlServicer_nodes = [
    ParameterControlServicer_SetRPM,
]

nodes = [
    *deviceServicer_nodes,
    *driveControlServicer_nodes,
    *parameterControlServicer_nodes,
]