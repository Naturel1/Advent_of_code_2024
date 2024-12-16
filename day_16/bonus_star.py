import numpy as np
from queue import PriorityQueue

WALL = 1

def read_input(filename: str) -> (np.ndarray, tuple, tuple):
    f = open(filename)
    lines = f.readlines()
    start, end = None, None
    grid = np.zeros((len(lines), len(lines[0])-1),dtype=int)
    for r,l in enumerate(lines):
        for c,v in enumerate(l.strip()):
            if v=="#":
                grid[r][c] = WALL
            if v=="S":
                start = (r,c)
            if v=="E":
                end = (r,c)
    return grid, start, end


def best_score(grid,start,end):
    dirs = [(0,+1), (+1,0), (0,-1), (-1,0)]
    queue = PriorityQueue()
    queue.put((0,start,0,[start]))
    visited = set()
    bestscore = 1_000_000
    seats = {start}
    while True:
        pos = queue.get()
        score, p, d, path = pos
        if score > bestscore:
            return len(seats)
        visited.add((p,d))
        for i in [0,-1,+1,+2]:
            dnew = (d+i)%4
            dr,dc = dirs[dnew]
            r,c = p
            r1,c1 = r+dr,c+dc
            if grid[r1][c1]==WALL:
                continue
            if ((r1,c1), dnew) in visited:
                continue
            scorenew = score+abs(i)*1000+1
            if (r1,c1)==end:
                bestscore = scorenew
                seats.update(path+[(r1,c1)])
            else:
                pathnew = path + [(r1,c1)]
                queue.put((scorenew,(r1,c1),dnew,pathnew))


def main():
    data = read_input("input.txt")
    result = best_score(data[0], data[1], data[2])
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()