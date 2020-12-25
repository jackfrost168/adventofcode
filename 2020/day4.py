def part1(passports):
    ans = 0
    for passport in passports:
        passport = passport.split(' ')
        valid = {'byr': 0, 'iyr': 0, 'eyr': 0, 'ecl': 0, 'pid': 0, 'hcl': 0, 'hgt': 0}
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
        passport = passport.strip().split(' ')
        valid = {'byr': 0, 'iyr': 0, 'eyr': 0, 'ecl': 0, 'pid': 0, 'hcl': 0, 'hgt': 0}
        for fields in passport:
            field = fields[0:3]
            if field == 'byr':
                year = int(fields[4:])
                if 1920 <= year <= 2002:
                    valid[field] += 1
            if field == 'iyr':
                year = int(fields[4:])
                if 2010 <= year <= 2020:
                    valid[field] += 1
            if field == 'eyr':
                year = int(fields[4:])
                if 2020 <= year <= 2030:
                    valid[field] += 1
            if field == 'hgt':
                unit = fields[-2:]
                if unit == 'cm':
                    height = int(fields[4:-2])
                    if 150 <= height <= 193:
                        valid[field] += 1
                if unit == 'in':
                    height = int(fields[4:-2])
                    if 59 <= height <= 76:
                        valid[field] += 1
            if field == 'hcl':
                digit = 0
                if fields[4] == '#' and len(fields[5:]) == 6:
                    for h in range(5, len(fields)):
                        if ('0' <= fields[h] <= '9') or ('a' <= fields[h] <= 'f'):
                            digit = digit + 1
                if digit == 6:
                    valid[field] += 1
            if field == 'ecl':
                if len(fields[4:]) == 3:
                    if fields[4:] in ['amb','blu','brn','gry','grn','hzl','oth']:
                        valid[field] += 1
            if field == 'pid':
                if len(fields[4:]) == 9:
                    digit = 0
                    for s in fields[4:]:
                        if '0' <= s <= '9':
                            digit = digit + 1
                    if digit == 9:
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
            line = line.strip()
            if line:
                tmp = tmp + line + " "
            else:
                passports.append(tmp)
                tmp = ''
        passports.append(tmp)

    ans1 = part1(passports)
    print("part 1:", ans1)
    ans2 = part2(passports)
    print("part 2:", ans2)


main()
