from NENV import *

class RegloDC_NodeBase(Node):

    style = 'normal'
    color = '#3283a8'


class DeviceServicer_GetLog(RegloDC_NodeBase):
    title = 'RegloDC - Device Servicer'

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

    title = 'Set Pump Address'
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

    title = 'Get Pump Status'
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

    title = 'Get Version Type'
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

    title = 'Current Version Software'
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

    title = 'Get Pump ID'
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

    title = 'Set Pump ID'
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

    title = 'Reset To Default'
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

    title = 'Get Total Volume'
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

    title = 'Lock Control Panel'
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


class DeviceServicer_LockControlPanel(RegloDC_NodeBase):
    """Set control panel to inactive (Input via control keys is not possible)."""

    title = 'Lock Control Panel'
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

    title = 'Set Display Numbers'
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

    title = 'Set Display Letters'
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

    title = 'Set Pump ID'
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

    title = 'Connect Device'
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

    title = 'Reset Overload'
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

    title = 'Properties'
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
    DeviceServicer_SetDisplayNumbers,
    DeviceServicer_SetDisplayLetters,
    DeviceServicer_SetCommunicationPort,
    DeviceServicer_ConnectDevice,
    DeviceServicer_ResetOverload,
    DeviceServicer_Properties,
]


class DriveControlServicer_SetDirectionClockwise(RegloDC_NodeBase):
    """Set the rotation direction of the pump to clockwise"""

    title = 'Set Direction to clockwise'
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


driveControlServicer_nodes = [
    DriveControlServicer_SetDirectionClockwise,
]

nodes = [
    *deviceServicer_nodes,
    *driveControlServicer_nodes,
]