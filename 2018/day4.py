with open('input/input4.txt', 'r') as f:
    time_map = {}
    f = f.readlines()
    for line in f:
        line = line.strip().replace('[', '').replace(']', '').split(' ')
        year, month, day = line[0].split('-')
        hour, minute = line[1].split(':')
        info = line[3]
        time_map[(year, month, day, hour, minute)] = info
print(time_map)
gaurd_map = {}
sleep_range = []
for key in sorted(time_map.keys()):
    print(key, time_map[key])
    if time_map[key].startswith('#'):
        if len(sleep_range) == 1:
            sleep_range.append(60)
            gaurd_map[guard].append(sleep_range)
        guard = time_map[key]
        if guard not in gaurd_map.keys():
            gaurd_map[guard] = []
        continue
    elif time_map[key].startswith('asleep'):
        sleep_range = [int(key[4])]
    elif time_map[key].startswith('up'):
        sleep_range.append(int(key[4]))
        gaurd_map[guard].append(sleep_range)
print(gaurd_map)

max_sleep = 0
max_sleep_guard_id = 0
for guard in gaurd_map.keys():
    total_sleep = 0
    sleep_ranges = gaurd_map[guard]
    for (begin, end) in sleep_ranges:
        total_sleep += end - begin
    if total_sleep > max_sleep:
        max_sleep = total_sleep
        max_sleep_guard_id = guard

print(max_sleep)
print(max_sleep_guard_id)
sleep_ranges = gaurd_map[max_sleep_guard_id]
max_minute = -1
max_count = 0
for i in range(60):
    count = 0
    for (start, end) in sleep_ranges:
        if start <= i < end:
            count += 1
    if count > max_count:
        max_count = count
        max_minute = i

id = int(max_sleep_guard_id[1:])
print(id)
print(max_minute*id)




frequent_sleep_minute = -1
frequent_sleep_guard = ''
frequent = 0
for guard in gaurd_map.keys():
    sleep_ranges = gaurd_map[guard]
    minute_count = 0
    max_minute = -1
    for i in range(60):
        count = 0
        for (start, end) in sleep_ranges:
            if start <= i < end:
                count += 1
        if count > minute_count:
            minute_count = count
            max_minute = i
    if minute_count > frequent:
        frequent_sleep_minute = max_minute
        frequent_sleep_guard = guard
        frequent = minute_count

id = int(frequent_sleep_guard[1:])
print(frequent_sleep_minute*id)