#!/usr/bin/env python3
"https://adventofcode.com/2020/day/12"

class Ship:
    def __init__(self):
        self.position = [0, 0]
        self.direction = [1, 0]

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def turn(self, direction, degree):
        degrees = {90: 1, 180: 2, 270: 3}
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        if degree == 180:
            self.direction = [-i for i in self.direction]
        else:
            if direction == 'L':
                self.direction = dirs[dirs.index(
                    self.direction)-degrees[degree]]
            elif direction == 'R':
                if dirs.index(self.direction)+degrees[degree] >= len(dirs):
                    self.direction = dirs[dirs.index(
                        self.direction)+degrees[degree]-len(dirs)]
                else:
                    self.direction = dirs[dirs.index(
                        self.direction)+degrees[degree]]

    def move(self, direction, length):
        dirs = {'N': [0, 1], 'E': [1, 0], 'S': [
            0, -1], 'W': [-1, 0], 'F': self.direction}
        tmp_dir = dirs[direction]
        x, y = self.position
        x += tmp_dir[0]*length
        y += tmp_dir[1]*length
        self.position = [x, y]


def number_one():
    ship = Ship()

    with open("input.txt", 'r') as f:
        dirs = [line for line in f.readlines()]

    for d in dirs:
        direction = d[0]
        length = int(d[1:])
        if direction == 'R' or direction == 'L':
            ship.turn(direction, length)
        else:
            ship.move(direction, length)
    return abs(ship.position[0]) + abs(ship.position[1])


def number_two():
    ship = Ship()
    waypoint = Ship()
    waypoint.set_position([10, 1])

    with open("input.txt", 'r') as f:
        dirs = [line for line in f.readlines()]

    for d in dirs:
        direction = d[0]
        length = int(d[1:])
        rel = [waypoint.position[0] - ship.position[0],
               waypoint.position[1] - ship.position[1]]
        if direction == 'R' or direction == 'L':
            if length == 180:  # turn around
                x = -rel[0]
                y = -rel[1]
            else:  # 270 or 90
                if length == 270:  # 270R -> 90L, etc
                    dirs = {'R': 'L', 'L': 'R'}
                    rel_dir = dirs[direction]
                else:
                    rel_dir = direction
                if rel_dir == 'R':
                    y = -rel[0]
                    x = rel[1]
                elif rel_dir == 'L':
                    y = rel[0]
                    x = -rel[1]
            waypoint.set_position([ship.position[0] + x, ship.position[1] + y])
        elif direction in ['N', 'E', 'S', 'W']:
            waypoint.move(direction, length)
        else:  # dir = F
            pos = [length*rel[0], length*rel[1]]
            x, y = ship.get_position()
            x += pos[0]
            y += pos[1]
            ship.set_position([x, y])
            waypoint.set_position([x + rel[0], y + rel[1]])

    return abs(ship.position[0]) + abs(ship.position[1])


print('Ans 1: ', number_one())
print('Ans 2: ', number_two())
