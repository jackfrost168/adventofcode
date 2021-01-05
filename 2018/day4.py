with open('input/input4.txt', 'r') as f:
    f = f.readlines()
    date_shift_records = {}
    date_guard = {}
    for line in f:
        line = line.strip().split(' ')
        date = line[0].replace('[', '').split('-')
        time = line[1].replace(']', '').split(':')
        info = line[2]
        if info == 'Guard':
            if int(time[0]) == 0:
                key = (int(date[0]), int(date[1]), int(date[2]))
                date_guard[key] = [int(line[3][1:]), (int(time[0]), int(time[1]))]
            else:
                key = (int(date[0]), int(date[1]), int(date[2]) + 1)
                date_guard[key] = [int(line[3][1:]), (0, 0)]
        else:
            key = (int(date[0]), int(date[1]), int(date[2]))
            date_shift_records[key] = []
            date_shift_records[key].append(info)

print(date_shift_records)
print(date_guard)
