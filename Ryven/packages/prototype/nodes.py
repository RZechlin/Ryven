from NENV import *

class SiLANodeBase(Node):

    style = 'normal'
    color = '#b33a27'


class PumpNode(SiLANodeBase):
    title = 'Pump'

    init_inputs = [
        NodeInputBP(type_='exec'),
        NodeInputBP(dtype=dtypes.Integer(), label='RPM'),
    ]

    init_outputs = [
        NodeOutputBP(type_='exec'),
        NodeOutputBP('RPM', type_='data'),
    ]

export_nodes(
    PumpNode,
)