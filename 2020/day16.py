def part1(ticket_fileds, nearby_tickets):
    valid_tickets = []
    ans = 0
    for ticket in nearby_tickets:
        ticket_valid = True
        for value in ticket:
            value_valid = False
            for key in ticket_fileds:
                for (lower_bound, upper_bound) in ticket_fileds[key]:
                    if lower_bound <= value <= upper_bound:
                        value_valid = True
                        break
                if value_valid:
                    break

            if not value_valid:
                ans = ans + value
                ticket_valid = False
        if ticket_valid:
            valid_tickets.append(ticket)

    return ans, valid_tickets


def part2(ticket_fileds, valid_tickets, your_ticket):
    fields = [[] for _ in range(len(your_ticket))]
    for j in range(len(valid_tickets[0])):
        for key in ticket_fileds.keys():
            field_valid = True
            for i in range(len(valid_tickets)):
                value = valid_tickets[i][j]
                value_valid = False
                for (lower_bound, upper_bound) in ticket_fileds[key]:
                    if lower_bound <= value <= upper_bound:
                        value_valid = True
                        break

                if not value_valid:
                    field_valid = False
                    break

            if field_valid:
                fields[j].append(key)

    loop = True
    while loop:
        for target in fields:
            if len(target) == 1:
                for f in fields:
                    if f != target and target[0] in f:
                        f.remove(target[0])
        loop = False
        for field in fields:
            if len(field) > 1:
                loop = True

    ans = 1
    for i, field in enumerate(fields):
        field = field[0]
        if len(field) >= len('departure') and field[0: len('departure')] == 'departure':
            ans = ans * your_ticket[i]

    return ans


def main():
    with open('input/input16.txt', 'r') as f:
        lines = f.readlines()
    ticket_fileds = {}
    i = 0
    your_ticket = ''
    nearby_tickets = []

    def record_your_ticket(line, i):
        line = line.strip().split(',')
        your_ticket = [int(value) for value in line]
        return your_ticket, i+1

    def record_nearby_tickets(lines, i):
        for line in lines:
            line = line.strip().split(',')
            nearby_tickets.append([int(value) for value in line])
            i = i + 1
        return nearby_tickets, i

    def record_ticket_fileds(lines, i):
        for line in lines:
            line = line.split(':')
            ticket_fileds[line[0]] = []
            range_ = line[1].split('or')
            range1 = range_[0].replace(' ', '')
            range2 = range_[1].replace(' ', '')
            range1 = range1.split('-')
            range2 = range2.split('-')
            ticket_fileds[line[0]].append((int(range1[0]), int(range1[1])))
            ticket_fileds[line[0]].append((int(range2[0]), int(range2[1])))
        return ticket_fileds, len(lines)

    while i < len(lines):
        line = lines[i]
        line = line.strip()
        if line == 'your ticket:':
            your_ticket, i = record_your_ticket(lines[i+1], i+1)
        elif line == 'nearby tickets:':
            nearby_tickets, i = record_nearby_tickets(lines[i+1:], i+1)
        elif line == '':
            i = i + 1
        else:
            ticket_fileds, i = record_ticket_fileds(lines[i: 20], i)

    ans1, valid_tickets = part1(ticket_fileds, nearby_tickets)
    print('part1:', ans1)
    ans2 = part2(ticket_fileds, valid_tickets, your_ticket)
    print('part2:', ans2)


main()
