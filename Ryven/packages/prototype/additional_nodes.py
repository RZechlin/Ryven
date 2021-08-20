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
        self.set_output_val(0, data)


class SplitInput(NodeBase):
    """Split the input into outputs"""

    title = 'Split'
    init_inputs = [
        NodeInputBP(type_='data'),
    ]
    init_outputs = [
        NodeOutputBP('', type_='data'),
    ]

    def __init__(self, params):
        super().__init__(params)

        # initial actions
        self.actions['add output'] = {
            'method': self.add_output
        }
        self.actions['remove output'] = {
            '0': {'method': self.remove_output, 'data': 0}
        }

    def update_event(self, inp=-1):
        data = self.input(0)
        for i in range(len(self.outputs)):
            self.set_output_val(i, data[i])

    def add_output(self):
        index = len(self.outputs)
        self.create_output(type_='data')
        self.actions['remove output'][str(index)] = {
            'method': self.remove_output,
            'data': index,
        }

    def remove_output(self, index):
        self.delete_output(index)

        del self.actions['remove output'][str(len(self.outputs))]

nodes = [
    EnumNode,
    ForEachLoop_Node,
    GetElement,
    SplitInput
]