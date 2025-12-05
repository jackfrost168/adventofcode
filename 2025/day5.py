def part1(ranges, ids):
    count = 0
    for id in ids:
        for r in ranges:
            start, end = r.split('-')
            start, end = int(start), int(end)
            if start <= int(id) <= end:
                count += 1
                break

    return count


def part2(ranges):
    intervals = []
    for r in ranges:
        start, end = r.split('-')
        start, end = int(start), int(end)
        intervals.append([start, end])

    intervals.sort(key=lambda x:x[0])
    print("Intervals:", intervals)

    merged = []
    prev = intervals[0]
    for r in intervals[1:]:
        if prev[1] >= r[0]:
            prev[1] = max(prev[1], r[1])
        else:
            merged.append(prev)
            prev = r[:]
    merged.append(prev)

    total = 0
    for [start, end] in merged:
        print(start, end)
        total += end - start + 1

    return total

def main():
    with open("input/input5.txt", "r") as f:
        inputs = f.read().split('\n\n')
        ranges, ids = inputs[0].strip().split(), inputs[1].strip().split()
        print(ranges)
        print("=========")
        print(ids)
    print("part 1:", part1(ranges[:], ids[:]))
    print("part 2:", part2(ranges[:]))

main()