class Instruction:
    def __init__(self, cycles: int, action, args) -> None:
        self.cycles = cycles
        self.action = action
        self.args = args

    def complete(self):
        if self.cycles > 0:
            return False

        self.action(*self.args)
        return True


def addx(value):
    global X
    X += value

def noop():
    pass

ins_actions = {
    'addx': addx,
    'noop': noop 
}

ins_cycles = {
    'addx': 2,
    'noop': 1 
}

def map_to_instuction(ins: str):
    ins = ins.strip()
    action = ins_actions[ins.split(' ')[0]]
    cycles = ins_cycles[ins.split(' ')[0]]

    if len(ins.split(' ')) > 1:
        add_value = int(ins.split(' ')[1])
        return Instruction(cycles, action, [add_value])

    return Instruction(cycles, action, [])


input_file = open('input.txt')
instructions = list(map(map_to_instuction, input_file))

X = 1
cycles_count = 0
signal_strengths = []

while(len(instructions) > 0):
    # START CYCLE
    cycles_count += 1
    current = instructions[0]


    # DURING CYCLE
    if cycles_count <= 220 and (cycles_count == 20 or (cycles_count+20)%40 == 0):
        signal_strengths.append(cycles_count * X)

    
    # END CYCLE
    current.cycles -= 1

    if current.complete():
        instructions.pop(0)
    

from functools import reduce

result = reduce(lambda a, b: a + b, signal_strengths, 0)

# Solution: 14780
print(result)