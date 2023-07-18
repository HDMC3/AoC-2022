import re
from typing import Dict, List, Tuple


def get_manhattan_distance(sensor_coord: Tuple[int, int], closest_beacon_coord: Tuple[int, int]):
    x1 = sensor_coord[0]
    y1 = sensor_coord[1]
    x2 = closest_beacon_coord[0]
    y2 = closest_beacon_coord[1]
    return abs(x2 - x1) + abs(y2 - y1)


def evaluate_sensor(sensor_coord: Tuple[int, int], closest_beacon_coord: Tuple[int, int]):
    global not_available_ranges
    manhattan = get_manhattan_distance(sensor_coord, closest_beacon_coord)
    sensor_x = sensor_coord[0]
    sensor_y = sensor_coord[1]

    for y_offset in range(0, manhattan + 1):

        x1 = sensor_x - (manhattan - y_offset)
        x2 = sensor_x + (manhattan - y_offset)

        r = (X_MIN if x1 < X_MIN else x1,
             X_MAX if x2 > X_MAX else x2)

        if y_offset == 0:
            if Y_MIN <= sensor_y <= Y_MAX:
                not_available_ranges[sensor_y].append(r)
            continue

        top_y = sensor_y - y_offset
        if Y_MIN <= top_y <= Y_MAX:
            not_available_ranges[top_y].append(r)

        bottom_y = sensor_y + y_offset
        if Y_MIN <= bottom_y <= Y_MAX:
            not_available_ranges[bottom_y].append(r)


def join_ranges(ranges: List[Tuple[int, int]]):
    merged_ranges = [ranges[0]]
    for current in ranges[1:]:
        last = merged_ranges[-1]
        if current[1] < last[1]:
            continue

        if current[0] <= last[1]+1:
            merged_ranges[-1] = (last[0], current[1])
            continue
        merged_ranges.append(current)

    return merged_ranges


input_file = open("input.txt")

Y_MIN = 0
Y_MAX = 4000000
X_MIN = 0
X_MAX = 4000000

beacons: List[Tuple[int, int]] = []
sensors: List[Tuple[int, int]] = []
not_available_ranges: Dict[int, List[Tuple[int, int]]] = {}

for key in range(0, 4000000 + 1):
    not_available_ranges[key] = []

for line in input_file:
    str_coords = re.findall(r"-?[0-9]+", line.strip())
    sensor_x = int(str_coords[0])
    sensor_y = int(str_coords[1])
    sensor = (sensor_x, sensor_y)
    beacon_x = int(str_coords[2])
    beacon_y = int(str_coords[3])
    beacon = (beacon_x, beacon_y)

    sensors.append(sensor)
    beacons.append(beacon)


for i, sensor in enumerate(sensors):
    beacon = beacons[i]
    evaluate_sensor(sensor, beacon)

solution = 0
for y in range(0, 4000000 + 1):
    row_ranges = not_available_ranges[y]
    row_ranges.sort(key=lambda r: r[0])
    union = join_ranges(row_ranges)
    if len(union) > 1:
        range_1 = union[0]
        x = range_1[1] + 1
        solution = (x * X_MAX) + y
        break

# Solution: 13172087230812
print(solution)
