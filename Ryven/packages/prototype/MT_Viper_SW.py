from NENV import *

class MT_Viper_SW_NodeBase(Node):

    style = 'normal'
    color = '#6d32a8'


class BalanceService_Properties(MT_Viper_SW_NodeBase):
    """All properties"""

    title = 'Properties'
    init_inputs = [
        #NodeInputBP(type_='exec'),
        #NodeInputBP(dtype=dtypes.Integer(), label=''),
    ]
    init_outputs = [
        #NodeOutputBP('', type_='exec'),
        NodeOutputBP('Stable Weight Value', type_='data'),
    ]

    def __init__(self, params):
        super().__init__(params)

    def update_event(self, inp=-1):
        if inp == 0:
            self.exec_output(0)

BalanceServicer_Nodes = [
    BalanceService_Properties,
]

nodes = [
    *BalanceServicer_Nodes,
]