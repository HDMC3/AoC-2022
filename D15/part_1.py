import re
from typing import List, Tuple


def get_manhattan_distance(sensor_coord: Tuple[int, int], closest_beacon_coord: Tuple[int, int]):
    x1 = sensor_coord[0]
    y1 = sensor_coord[1]
    x2 = closest_beacon_coord[0]
    y2 = closest_beacon_coord[1]
    return abs(x2 - x1) + abs(y2 - y1)


def get_not_available_range(sensor_coord: Tuple[int, int], closest_beacon_coord: Tuple[int, int]):
    manhattan = get_manhattan_distance(sensor_coord, closest_beacon_coord)
    sensor_x = sensor_coord[0]
    sensor_y = sensor_coord[1]

    x_offset = manhattan

    if sensor_y == ROW_TO_EVALUATE:
        x_offset = manhattan

    elif ROW_TO_EVALUATE > sensor_y and ROW_TO_EVALUATE <= sensor_y + manhattan:
        x_offset = (sensor_y + manhattan) - ROW_TO_EVALUATE

    elif ROW_TO_EVALUATE < sensor_y and ROW_TO_EVALUATE >= sensor_y - manhattan:
        x_offset = ROW_TO_EVALUATE - (sensor_y - manhattan)
    else:
        return

    return (sensor_x - x_offset, sensor_x + x_offset)


def join_ranges(ranges: List[Tuple[int, int]]):
    ranges.sort(key=lambda r: r[0])
    merged_ranges = [ranges[0]]
    for current in ranges[1:]:
        last = merged_ranges[-1]
        if current[1] < last[1]:
            continue

        if current[0] <= last[1] + 1:
            merged_ranges[-1] = (last[0], current[1])
            continue
        merged_ranges.append(current)

    return merged_ranges


input_file = open("input.txt")

ROW_TO_EVALUATE = 2000000

beacons_in_ranges: List[Tuple[int, int]] = []
sensors_in_ranges: List[Tuple[int, int]] = []
not_available_ranges: List[Tuple[int, int]] = []

for line in input_file:
    str_coords = re.findall(r"-?[0-9]+", line.strip())
    sensor_x = int(str_coords[0])
    sensor_y = int(str_coords[1])
    sensor = (sensor_x, sensor_y)

    beacon_x = int(str_coords[2])
    beacon_y = int(str_coords[3])
    beacon = (beacon_x, beacon_y)

    sensor_range = get_not_available_range(sensor, beacon)
    if sensor_range == None:
        continue

    if sensor not in sensors_in_ranges and sensor_y == ROW_TO_EVALUATE \
            and (sensor_range[0] <= sensor_x <= sensor_range[1]):

        sensors_in_ranges.append(sensor)

    if beacon not in beacons_in_ranges and beacon_y == ROW_TO_EVALUATE \
            and (sensor_range[0] <= beacon_x <= sensor_range[1]):

        beacons_in_ranges.append(beacon)

    not_available_ranges.append(sensor_range)


merged_ranges = join_ranges(not_available_ranges)

total = 0
for r in merged_ranges:
    total += (r[1] - r[0] + 1)

# Solution: 5112034
print(total - len(sensors_in_ranges) - len(beacons_in_ranges))
