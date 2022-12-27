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
sprite_positions = [0, 1, 2]
pixels = []

while(len(instructions) > 0):
    # START CYCLE
    cycles_count += 1
    current = instructions[0]


    # DURING CYCLE
    sprite_positions = [X-1, X, X+1]
    current_pixel_id = (cycles_count-1) % 40
    if current_pixel_id in sprite_positions:
        pixels.append('#')
    else:
        pixels.append('.')
    

    # END CYCLE
    current.cycles -= 1

    if current.complete():
        instructions.pop(0)
    

rows = []
row = ''
for i, pixel in enumerate(pixels):
    if (i+1)%40 == 0:
        row += pixel
        rows.append(row)
        row = ''
    else:
        row += pixel + ' '

if len(row) > 0:
    rows.append(row)

# Solution: ELPLZGZL
[print(r) for r in rows]
