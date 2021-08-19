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

class ForEachLoop_Node(NodeBase):
    title = 'for each2'
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


class GetElement(NodeBase):
    """Get element of provided list, array, etc. at position pos"""

    title = 'Get Element'
    init_inputs = [
       # NodeInputBP(type_='exec'),
        NodeInputBP(label='list'),
        NodeInputBP(dtype=dtypes.Integer(), label='pos'),
    ]
    init_outputs = [
        NodeOutputBP('', type_='data'),
    ]

    def __init__(self, params):
        super().__init__(params)

    def update_event(self, inp=-1):
        pos = self.input(1)
        lst = self.input(0)
        data = lst[pos]
        self.set_outpu_val(0, data)


nodes = [
    EnumNode,
    ForEachLoop_Node,
    GetElement
]