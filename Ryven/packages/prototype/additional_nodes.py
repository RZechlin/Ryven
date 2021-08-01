from NENV import *

class NodeBase(Node):
    style = 'normal'
    color = '#6d32a8'

class EnumNode(NodeBase):

    title = 'Enum Node'
    init_inputs = [
        NodeInputBP(type_='exec'),
        NodeInputBP(type_='data', label='elements'),
    ]
    init_outputs = [
        NodeOutputBP('loop', type_='exec'),
        NodeOutputBP('e', type_='data'),
        NodeOutputBP('finished', type_='exec'),
    ]

    def update_event(self, inp=-1):
        for e in self.input(0):
            self.set_output_val(1, e)
            self.exec_output(0)

        self.exec_output(2)

nodes = [
    EnumNode
]