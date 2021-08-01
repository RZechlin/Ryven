from NENV import *

class RegloDCNodeBase(Node):

    style = 'normal'
    color = '#3283a8'


class DeviceServicer_GetLog(RegloDCNodeBase):
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


class DeviceServicer_SetPumpAddress(RegloDCNodeBase):
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


class DeviceServicer_GetPumpSatus(RegloDCNodeBase):
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


class DeviceServicer_GetVersionType(RegloDCNodeBase):
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


class DeviceServicer_GetVersionSoftware(RegloDCNodeBase):
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


class DeviceServicer_GetPumpID(RegloDCNodeBase):
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


class DeviceServicer_SetPumpID(RegloDCNodeBase):
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


class DeviceServicer_ResetToDefault(RegloDCNodeBase):
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


class DeviceServicer_GetTotalVolume(RegloDCNodeBase):
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

class DeviceServicer_UnlockControlPanel(RegloDCNodeBase):
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


class DeviceServicer_LockControlPanel(RegloDCNodeBase):
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


class DeviceServicer_SetDisplayNumbers(RegloDCNodeBase):
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


class DeviceServicer_SetDisplayLetters(RegloDCNodeBase):
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


class DeviceServicer_SetCommunicationPort(RegloDCNodeBase):
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


class DeviceServicer_ConnectDevice(RegloDCNodeBase):
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


class DeviceServicer_ResetOverload(RegloDCNodeBase):
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


class DeviceServicer_Properties(RegloDCNodeBase):
    """All properties"""

    title = ''
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

nodes = [
    *deviceServicer_nodes,
]