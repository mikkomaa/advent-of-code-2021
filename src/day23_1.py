import collections
import itertools


class Spot:
    """We store the map of the burrow as a linked list of Spots."""

    def __init__(self, goal, state):
        self.goal = goal  # End configuration (., A, B, C, or D).
        self.state = state  # ., A, B, C, or D.
        self.never_stop = False  # True if spot is immediately outside a room.
        self.neighbors = None  # A list of neighboring spots.


# The amphipod, the destination spot, and the number of steps needed.
Move = collections.namedtuple('Move', 'amphipod spot steps')
energies = dict(A=1, B=10, C=100, D=1000)  # Energies used in one step.
least_energy = float('Infinity')  # The least energy to organize amphipods.
seen_states = dict()  # We store seen states to avoid needless searches.
room_backs = dict()  # Spots at the back of each room.


class Amphipod:
    def __init__(self, name, spot):
        self.name = name  # A, B, C, or D.
        self.spot = spot  # The spot where the amphipod is located in.
        self.home = False  # True if the amphipod is in its final spot.

    def move(self, move):
        """Move the amphipod into another spot."""
        self.spot.state = '.'
        _, self.spot, steps = move
        self.home = is_free_home(self.spot, self)
        self.spot.state = self.name

    def get_moves(self):
        """Return spots where the amphipod can move and needed steps."""

        def search(spot, steps, visited):
            """Return free spots to move from spot and needed steps."""
            moves = set()
            for neighbor in spot.neighbors:
                if neighbor not in visited and neighbor.state == '.':
                    moves.add(Move(self, neighbor, steps + 1))
                    moves |= search(neighbor, steps + 1, visited | {spot})
            return moves

        # The amphipod is already in the final spot.
        if self.home:
            return []
        moves = search(self.spot, 0, set())
        # The amphipod is in the hallway.
        if self.spot.goal == '.':
            return [m for m in moves if is_free_home(m.spot, self)]
        # The amphipod is in a room.
        moves = [m for m in moves if not m.spot.never_stop]
        return [m for m in moves if m.spot.goal == '.'
                                    or is_free_home(m.spot, self)]


def is_free_home(spot, amphipod):
    """Return True if spot is an available home for amphipod."""
    # The method is overly complex for day23_1 but is needed for day23_2.
    if amphipod.name == spot.goal and spot.state == '.':
        room_spot = room_backs[amphipod.name]
        # Check if spot is at the back of a room.
        if room_spot is spot:
            return True
        # Check if amphipod would block the way.
        if room_spot.state != amphipod.name:
            return False
        room_spot = room_spot.neighbors[0]
        # Check if spot is next to the back room.
        if room_spot is spot:
            return True
        # Check if amphipod would block the way.
        if room_spot.state != amphipod.name:
            return False
        room_spot = [n for n in room_spot.neighbors if len(n.neighbors) == 2][0]
        # Check if spot is the third from the back.
        if room_spot is spot:
            return True
        # Check if amphipod would block the way.
        if room_spot.state != amphipod.name:
            return False
        # Spot is next to the hallway.
        return True
    return False


def parse_input(strings):
    """Return the map of the burrow, the amphipods, and the back rooms."""
    spots = []
    amphipods = []
    # Create spots, and set their goals and states. Create amphipods.
    for string in strings:
        row = []
        types = ['D', 'C', 'B', 'A']
        for c in string:
            if c == '.':
                row.append(Spot('.', '.'))
            elif c in 'ABCD':
                spot = Spot(types.pop(), c)
                row.append(spot)
                amphipods.append(Amphipod(c, spot))
            else:
                row.append(None)  # Makes it easier to set neighbors.
        spots.append(row)

    # Set neighbors, and mark the spots in the hallway next to the rooms.
    for i, row in enumerate(spots):
        for j, spot in enumerate(row):
            if spot is None:
                continue
            spot.neighbors = [s for s in (row[j - 1], row[j + 1],
                                          spots[i - 1][j], spots[i + 1][j])
                              if isinstance(s, Spot)]
            if spot.state == '.' and spots[i + 1][j] in spot.neighbors:
                spot.never_stop = True

    spots = list(itertools.chain(*(row for row in spots)))
    spots = [spot for spot in spots if isinstance(spot, Spot)]
    room_backs = {spot.goal: spot for spot in spots
                  if spot.goal != '.' and len(spot.neighbors) == 1}
    return spots, amphipods, room_backs


def is_organized(spots):
    """Return True if the ending configuration is reached, else False."""
    return all(s.state == s.goal for s in spots)


def get_organized(amphipods, spots, energy):
    """Move amphipods to get them organized. Find out the least energy."""
    global least_energy, seen_states
    if energy >= least_energy:
        return
    if is_organized(spots):
        least_energy = energy
        return
    state = ''.join(spot.state for spot in spots)
    if state in seen_states and seen_states[state] <= energy:
        return
    seen_states[state] = energy

    moves = get_moves(amphipods)
    for m in moves:
        current_spot = m.amphipod.spot
        m.amphipod.move(m)
        get_organized(amphipods, spots,
                      energy + m.steps * energies[m.amphipod.name])
        m.amphipod.move(Move(m.amphipod, current_spot, 0))


def get_moves(amphipods):
    """Return moves for amphipods."""
    all_moves = []
    for amphipod in amphipods:
        moves = amphipod.get_moves()
        for move in moves:
            if is_free_home(move.spot, amphipod):
                return [move]  # Always move to a free home spot.
        all_moves += moves
    return all_moves


def main(filename):
    """Return the least energy needed to organize amphipods."""
    with open(filename) as f:
        lines = [line.rstrip() for line in f.readlines()]

    global room_backs, least_energy
    spots, amphipods, room_backs = parse_input(lines)
    get_organized(amphipods, spots, 0)
    return least_energy


if __name__ == '__main__':
    print(main('../data/day23.txt'))
