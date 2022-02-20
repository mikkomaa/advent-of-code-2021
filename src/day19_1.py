import collections
import itertools
import queue


class Scanner:
    def __init__(self, beacons):
        self.normalized = False  # True, if beacon coordinates are viewed
        self.beacons = beacons   # from (0, 0, 0).
        self.position = None  # Needed in day19_2.py.

    def normalize(self, position):
        """Given Scanner position, convert beacons into viewed from origo."""
        self.beacons = [tuple(sum(x) for x in zip(position, beacon))
                        for beacon in self.beacons]
        self.normalized = True


# Possible scanner rotations.
rotations = (lambda x, y, z: (x, y, z), lambda x, y, z: (x, -z, y),
             lambda x, y, z: (x, -y, -z), lambda x, y, z: (x, z, -y),
             lambda x, y, z: (-x, y, -z), lambda x, y, z: (-x, z, y),
             lambda x, y, z: (-x, -y, z), lambda x, y, z: (-x, -z, -y),
             lambda x, y, z: (z, y, -x), lambda x, y, z: (z, x, y),
             lambda x, y, z: (z, -y, x), lambda x, y, z: (z, -x, -y),
             lambda x, y, z: (-z, y, x), lambda x, y, z: (-z, -x, y),
             lambda x, y, z: (-z, -y, -x), lambda x, y, z: (-z, x, -y),
             lambda x, y, z: (y, -z, -x), lambda x, y, z: (y, x, -z),
             lambda x, y, z: (y, z, x), lambda x, y, z: (y, -x, z),
             lambda x, y, z: (-y, -z, x), lambda x, y, z: (-y, x, z),
             lambda x, y, z: (-y, z, -x), lambda x, y, z: (-y, -x, -z))


def find_common_beacons(scanner_1, scanner_2):
    """If enough common beacons exist, return scanner_2 normalized."""
    for rotate in rotations:
        rotated_beacons = [rotate(*beacon) for beacon in scanner_2.beacons]
        positions = collections.defaultdict(int)
        for beacon_1 in scanner_1.beacons:
            for beacon_2 in rotated_beacons:
                pos = tuple(map(lambda a, b: a - b, beacon_1, beacon_2))
                positions[pos] += 1

        position = max(positions, key=positions.get)
        if positions[position] > 11:  # Position is scanner_2 position.
            scanner_2.beacons = rotated_beacons
            if not scanner_2.normalized:
                scanner_2.normalize(position)
            return scanner_2
    return None  # Not enough common beacons found.


def process_scanners(scanners):
    """Find beacons by processing a scanner at a time."""
    scanners_to_process = queue.Queue()
    scanners[0].normalized = True
    scanners_to_process.put(scanners[0])
    scanners_processed = set()

    while not scanners_to_process.empty():
        scanner_1 = scanners_to_process.get()
        scanners_processed.add(scanner_1)
        for scanner_2 in scanners:
            if scanner_2 not in scanners_processed:
                scanner_result = find_common_beacons(scanner_1, scanner_2)
                if scanner_result:
                    scanners_to_process.put(scanner_result)


def parse():
    """Parse input. Return a list of Scanners."""
    scanners = []
    with open('../data/day19.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    for line in lines:
        if line.startswith('---'):
            scanners.append(Scanner([]))
        elif line:
            scanners[-1].beacons.append(tuple(map(int, line.split(','))))
    return scanners


if __name__ == '__main__':
    scanners = parse()
    process_scanners(scanners)
    beacons = set(itertools.chain(*(scanner.beacons for scanner in scanners)))
    print(len(beacons))
