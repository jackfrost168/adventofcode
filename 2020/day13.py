def part1(arrive_time, buses):
    arrived = [True for i in range(len(buses))]

    time = arrive_time
    while True:
        for i in range(len(buses)):
            if time % buses[i] == 0:
                arrived[i] = True
            else:
                arrived[i] = False
        if 1 in arrived:
            id = arrived.index(True)
            ans = (time-arrive_time) * buses[id]
            return ans
        time += 1


def EX_GCD(a,b,arr): #扩展欧几里得
    if b == 0:
        arr[0] = 1
        arr[1] = 0
        return a
    g = EX_GCD(b, a % b, arr)
    t = arr[0]
    arr[0] = arr[1]
    arr[1] = t - int(a / b) * arr[1]
    return g


def ModReverse(a,n): #ax=1(mod n) 求a模n的乘法逆x
    arr = [0,1,]
    gcd = EX_GCD(a,n,arr)
    if gcd == 1:
        return (arr[0] % n + n) % n
    else:
        return -1


def part2(a, m): #Chinese Remainder Theorem
    M = 1
    for mi in m:
        M = M * mi
    ans = 0
    for i in range(len(m)):
        ai = -a[i] #?
        bi = M // m[i]
        bi_ = ModReverse(bi, m[i]) #pow(bi, -1, m[i]) python3.8
        ans = ans + ai*bi*bi_

    return ans % M


def main():
    f = open('input13.txt', 'r')
    lines = f.readlines()
    arrive_time = int(lines[0].strip('\n'))
    line2 = lines[1].strip('\n')
    bus = line2.split(',')
    buses = []
    a = []
    for i, s in enumerate(bus):
        if s != 'x':
            buses.append(int(s))
            a.append(i)

    ans1 = part1(arrive_time, buses)
    print('part1:', ans1)
    ans2 = part2(a, buses)
    print('part2:', ans2)


main()