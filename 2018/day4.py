def part1(guard_map):
    longest_sleep = 0
    longest_sleep_guard_id = 0
    for guard in guard_map.keys():
        sleep_time = 0
        sleep_ranges = guard_map[guard]
        for (begin, end) in sleep_ranges:
            sleep_time += end - begin
        if sleep_time > longest_sleep:
            longest_sleep = sleep_time
            longest_sleep_guard_id = guard

    sleep_ranges = guard_map[longest_sleep_guard_id]
    frequent_minute = -1
    most_frequent_count = 0
    for i in range(60):
        count = 0
        for (start, end) in sleep_ranges:
            if start <= i < end:
                count += 1
        if count > most_frequent_count:
            most_frequent_count = count
            frequent_minute = i

    id = int(longest_sleep_guard_id[1:])

    return frequent_minute * id


def part2(guard_map):
    most_frequent_minute = -1
    most_frequent_sleep_guard = ''
    most_frequent = 0
    for guard in guard_map.keys():
        sleep_ranges = guard_map[guard]
        minute_count = 0
        frequent_minute = -1
        for i in range(60):
            count = 0
            for (start, end) in sleep_ranges:
                if start <= i < end:
                    count += 1
            if count > minute_count:
                minute_count = count
                frequent_minute = i
        if minute_count > most_frequent:
            most_frequent_minute = frequent_minute
            most_frequent_sleep_guard = guard
            most_frequent = minute_count

    id = int(most_frequent_sleep_guard[1:])

    return most_frequent_minute * id


def main():
    with open('input/input4.txt', 'r') as f:
        time_map = {}
        f = f.readlines()
        for line in f:
            line = line.strip().replace('[', '').replace(']', '').split(' ')
            year, month, day = line[0].split('-')
            hour, minute = line[1].split(':')
            info = line[3]
            time_map[(year, month, day, hour, minute)] = info

    guard_map = {}
    sleep_range = []
    for key in sorted(time_map.keys()):
        if time_map[key].startswith('#'):
            if len(sleep_range) == 1:
                sleep_range.append(60)
                guard_map[guard].append(sleep_range)
            guard = time_map[key]
            if guard not in guard_map.keys():
                guard_map[guard] = []
            continue
        elif time_map[key].startswith('asleep'):
            sleep_range = [int(key[4])]
        elif time_map[key].startswith('up'):
            sleep_range.append(int(key[4]))
            guard_map[guard].append(sleep_range)  # {guard: [[0, 21], [45, 49]}

    ans1 = part1(guard_map)
    print('part 1:', ans1)
    ans2 = part2(guard_map)
    print('part 2:', ans2)


main()
