def part1(nums):
    for n1 in nums:
        for n2 in nums:
            if n1 + n2 == 2020:
                return n1 * n2

def part2(nums):
    for n1 in nums:
        for n2 in nums:
            for n3 in nums:
                if n1 + n2 + n3 == 2020:
                    return n1 * n2 * n3



def main():

    file = 'day1.txt'
    with open(file, 'r') as in_f:
        nums = [int(l.strip()) for l in in_f.readlines()]

    print(part1(nums))
    print(part2(nums))



if __name__ == '__main__':
    main()