import collections
import queue

from day19_1 import parse, rotations


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
        if positions[position] > 11:
            if position in (s.position for s in scanners):
                continue  # The resulted position is used already.
            scanner_2.position = position
            scanner_2.beacons = rotated_beacons
            if not scanner_2.normalized:
                scanner_2.normalize(position)
            return scanner_2
    return None  # Not enough common beacons found.


def process_scanners(scanners):
    """Find beacons by processing a scanner at a time."""
    scanners[0].normalized = True
    scanners[0].position = (0, 0, 0)
    scanners_to_process = queue.Queue()
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


def get_distances(scanners):
    """Return a list of distances between scanners."""
    distances = []
    for i, s1 in enumerate(scanners):
        for s2 in scanners[i+1:]:
            distances.append(sum(abs(a - b)
                                 for a, b in zip(s1.position, s2.position)))
    return distances


if __name__ == '__main__':
    scanners = parse()
    process_scanners(scanners)
    print(max(get_distances(scanners)))
