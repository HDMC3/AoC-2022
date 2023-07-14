from typing import List
from enum import Enum
import json


class PairOrder(Enum):
    CORRECT = 0
    INCORRECT = 1
    UNDEFINED = 2


class PacketPair:
    def __init__(self, index, left, right) -> None:
        self.index = index
        self.left_value = left
        self.right_value = right


input_file = open('input.txt')

packet_pairs: List[PacketPair] = []
tmp_str_pair = []
idx = 1
c = 1
for line in input_file:
    packet_str = line.strip()
    if packet_str == "":
        continue

    tmp_str_pair.append(packet_str)
    if len(tmp_str_pair) == 2:
        left_packet = json.loads(tmp_str_pair[0])
        right_packet = json.loads(tmp_str_pair[1])
        packet_pairs.append(PacketPair(idx, left_packet, right_packet))
        idx += 1
        tmp_str_pair.clear()


input_file.close()


def compare(left, right):
    if type(left) == int and type(right) == int:
        return PairOrder.INCORRECT if left > right \
            else PairOrder.CORRECT if right > left \
            else PairOrder.UNDEFINED

    if type(left) == int and type(right) == list:
        list_from_int = [left]
        return compare(list_from_int, right)

    if type(left) == list and type(right) == int:
        list_from_int = [right]
        return compare(left, list_from_int)

    if type(left) == list and type(right) == list:
        smaller_len = min(len(left), len(right))
        for i in range(0, smaller_len):
            result = compare(left[i], right[i])
            if result == PairOrder.UNDEFINED:
                continue

            return result

        return PairOrder.INCORRECT if len(left) > len(right) \
            else PairOrder.CORRECT if len(right) > len(left) \
            else PairOrder.UNDEFINED


indexes = []
for p in packet_pairs:
    result = compare(p.left_value, p.right_value)
    print(f"{p.index}")
    print(f"{result}\n")
    if result == PairOrder.CORRECT:
        indexes.append(p.index)

# Solution: 5580
print(sum(indexes))
