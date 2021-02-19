import functools as ft

OPEN = '.'
TREE = '#'


def part1(trees_map: list):
    return recorre(trees_map, 3, 1)


def part2(trees_map: list):
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    return ft.reduce(lambda a,b:a*b, [recorre(trees_map, r, d) for r,d in slopes])

def recorre(trees_map: list, r: int, d: int):
    trees = 0
    x = 0
    n = len(trees_map[0])
    for l in trees_map[d::d]:
        x = (x+r) % n
        trees += l[x] == TREE
    return trees

def main():
    file = 'day3.txt'
    with open(file, 'r') as in_f:
        trees_map = [l.strip() for l in in_f.readlines()]
    
    print(part1(trees_map))
    print(part2(trees_map))



if __name__ == '__main__':
    main()