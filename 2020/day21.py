def part1(input, appeared, f):
    final_allergens = {}
    while True:
        if len(final_allergens.keys()) == len(input.keys()):
            break
        for key in input.keys():
            if key in final_allergens.keys():
                continue
            num_allergens = 0
            ingres = []
            for ingredient in set(input[key]):
                num_ingredient = input[key].count(ingredient)
                if num_ingredient == appeared[key]:
                    num_allergens += 1
                    ingres.append(ingredient)
            if num_allergens == 1:
                final_allergens[key] = ingres[0]
                for key in input.keys():
                    while ingres[0] in input[key]:
                        input[key].remove(ingres[0])
                break

    #print(final_allergens)

    items = []
    for key in final_allergens.keys():
        items.append(final_allergens[key])
    #print(items)
    ans = 0
    for line in f:
        line = line.strip().split('(contains')
        ingredients = line[0].strip().split(' ')
        allergens = line[1].strip().split(',')
        allergens[-1] = allergens[-1].replace(')', '')
        no_aller_ingre = 0
        copy_ingredients = ingredients[:]
        for ingre in ingredients:
            if ingre in items:
                copy_ingredients.remove(ingre)
        ans = ans + len(copy_ingredients)

    return ans, final_allergens


def part2(final_allergens):
    ans2 = ''
    for key in sorted(final_allergens.keys()):
        ans2 = ans2 + final_allergens[key] + ','
    return ans2[0:-1]

def main():
    with open('input/input21.txt', 'r') as f:
        # with open('test.txt', 'r') as f:
        f = f.readlines()
        input = {}
        appeared = {}
        for line in f:
            line = line.strip()
            line = line.split('(contains')
            ingredients = line[0].strip().split(' ')
            allergens = line[1].strip().split(',')
            allergens[-1] = allergens[-1].replace(')', '')
            for allergen in allergens:
                allergen = allergen.strip()
                if allergen not in input.keys():
                    input[allergen] = ingredients[:]
                    appeared[allergen] = 1
                else:
                    input[allergen] += ingredients
                    appeared[allergen] += 1
        # print(input)
        # for key in input.keys():
        #     print(key, input[key])
    ans1, final_allergens = part1(input, appeared, f)
    print('part1:', ans1)
    ans2 = part2(final_allergens)
    print('part2:', ans2)


main()

