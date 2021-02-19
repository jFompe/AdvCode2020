def part1(lines):
    return sum([check_line1(l) for l in lines])

def check_line1(l: dict):
    count = 0
    for c in l['pass']:
        count += c == l['char']
        if count > l['max']:
            return False
    return count >= l['min'] 


def part2(lines):
    return sum([check_line2(l) for l in lines])

def check_line2(l: dict):
    low, high = l['min'], l['max']
    p = l['pass']
    c = l['char']
    return ((p[low-1] == c) + (p[high-1] == c)) == 1


def line_as_dict(l: str):
    d = {}
    limits, charc, passwd = l.split()
    d['min'], d['max'] = map(lambda x:int(x), limits.split("-"))
    d['char'] = charc[0]
    d['pass'] = passwd
    return d


def main():
    file = "day2.txt"
    with open(file, "r") as in_f:
        lines = [line_as_dict(l.strip()) for l in in_f.readlines()]
    
    print(part1(lines))
    print(part2(lines))
    


if __name__ == '__main__':
    main()