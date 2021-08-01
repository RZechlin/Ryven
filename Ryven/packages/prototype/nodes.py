from NENV import *

import sys
import os
sys.path.append(os.path.dirname(__file__))

from RegloDC import nodes as RegloDC_nodes
from MT_Viper_SW import nodes as MT_Viper_SW_nodes
from additional_nodes import nodes as additional_nodes


# This node is still here in order to not break the prototype
class SiLANodeBase(Node):

    style = 'normal'
    color = '#b33a27'

class PumpNode(SiLANodeBase):
    title = 'Pump'

    init_inputs = [
        NodeInputBP(type_='exec'),
        NodeInputBP(dtype=dtypes.Integer(), label='RPM'),
        NodeInputBP(dtype=dtypes.Boolean(), label='Direction')
    ]

    init_outputs = [
        NodeOutputBP(type_='exec'),
        NodeOutputBP('RPM', type_='data'),
    ]



export_nodes(
    PumpNode,
    *RegloDC_nodes,
    *MT_Viper_SW_nodes,
    *additional_nodes
)