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


divider_packets = [[[2]], [[6]]]
packets: List = [divider_packets[0], divider_packets[1]]

input_file = open('input.txt')

for line in input_file:
    packet_str = line.strip()
    if packet_str == "":
        continue

    packet = json.loads(packet_str)
    packets.append(packet)

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


for i in range(0, len(packets)):
    for j in range(i+1, len(packets)):
        result = compare(packets[i], packets[j])

        if result == PairOrder.INCORRECT:
            tmp = packets[j]
            packets[j] = packets[i]
            packets[i] = tmp


indexes = []
for i, packet in enumerate(packets):
    if packet in divider_packets:
        indexes.append(i + 1)

# Solution: 26200
print(indexes[0] * indexes[1])
