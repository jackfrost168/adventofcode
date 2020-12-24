def part1(passports):
    ans = 0
    for passport in passports:
        passport = passport.split(' ')
        valid = {'byr':0, 'iyr':0, 'eyr':0, 'ecl':0, 'pid':0, 'hcl': 0, 'hgt':0}
        for fields in passport:
            field = fields[0:3]
            if field in valid.keys():
                valid[field] += 1
        count = 0
        for key in valid.keys():
            if valid[key] == 1:
                count += 1
        if count == 7:
            ans = ans + 1
    return ans


def part2(passports):
    ans = 0
    for passport in passports:
        passport = passport.split(' ')
        valid = {'byr':0, 'iyr':0, 'eyr':0, 'ecl':0, 'pid':0, 'hcl': 0, 'hgt':0}
        for fields in passport:
            field = fields[0:3]
            if field == 'byr':
                year = fields[4:]
                if len(year) == 4:
                    year = int(year)
                    if year >= 1920 and year <= 2002:
                        valid[field] += 1
            if field == 'iyr':
                year = fields[4:]
                if len(year) == 4:
                    year = int(year)
                    if year >= 2010 and year <= 2020:
                        valid[field] += 1
            if field == 'eyr':
                year = fields[4:]
                if len(year) == 4:
                    year = int(year)
                    if year >= 2020 and year <= 2030:
                        valid[field] += 1
            if field == 'hgt':
                unit = fields[-2:]
                if unit == 'cm':
                    if int(fields[4:-2]) >= 150 and int(fields[4:-2]) <= 193:
                        valid[field] += 1
                if unit == 'in':
                    if int(fields[4:-2]) >= 59 and int(fields[4:-2]) <= 76:
                        valid[field] += 1
            if field == 'hcl':
                digit = 0
                if fields[4] == '#' and len(fields[5:]) == 6:
                    for h in range(5, len(fields)):
                        if (fields[h] >= '0' and fields[h] <= '9') or \
                            (fields[h] >= 'a' and fields[h] <= 'f'):
                            digit = digit + 1
                if digit == 6:
                    valid[field] += 1
            if field == 'ecl':
                if len(fields[4:]) == 3:
                    if fields[4:] in ['amb','blu','brn','gry','grn','hzl','oth']:
                        valid[field] += 1
            if field == 'pid':
                if len(fields[4:]) == 9:
                    p = 0
                    for s in fields[4:]:
                        if s >= '0' and s <= '9':
                            p = p + 1
                    if p == 9:
                        valid[field] += 1

        count = 0
        for key in valid.keys():
            if valid[key] == 1:
                count += 1
        if count == 7:
            ans = ans + 1
    return ans


def main():
    with open("input/input4.txt", "r") as f:
        lines = f.readlines()
        passports = []
        tmp = ""
        for line in lines:
            line = line.strip('\n')
            if len(line) != 0:
                tmp = tmp + line + " "
            else:
                passports.append(tmp)
                tmp = ''
        passports.append(tmp)

    ans1 = part1(passports)
    print("part1:", ans1)
    ans2 = part2(passports)
    print("part2:", ans2)


main()
