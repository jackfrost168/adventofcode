def part1(ingredients_map, appeared, list_of_foods):
    final_allergens = {}
    while ingredients_map.keys():
        allergens = ingredients_map.keys()
        for allergen in allergens:
            ingredients_related_to_allergen = ingredients_map[allergen]
            count_valid_allergens = 0
            valid_ingredients = []
            for ingredient in set(ingredients_related_to_allergen):
                same_ingredient = ingredients_related_to_allergen.count(ingredient)
                if same_ingredient == appeared[allergen]:
                    count_valid_allergens += 1
                    valid_ingredients.append(ingredient)

            if count_valid_allergens == 1:
                final_allergens[allergen] = valid_ingredients[0]
                del ingredients_map[allergen]
                for key in allergens:
                    while valid_ingredients[0] in ingredients_map[key]:
                        ingredients_map[key].remove(valid_ingredients[0])
                break

    cleared_ingredients = [final_allergens[key] for key in final_allergens.keys()]

    ans = 0
    for line in list_of_foods:
        ingredients = line[:]
        for ingredient in line:
            if ingredient in cleared_ingredients:
                ingredients.remove(ingredient)
        ans = ans + len(ingredients)

    return ans, final_allergens


def part2(final_allergens):
    ans = ''
    for key in sorted(final_allergens.keys()):
        ans = ans + final_allergens[key] + ','
    return ans[0:-1]


def main():
    with open('input/input21.txt', 'r') as f:
        list_of_foods = []
        ingredients_map = {}
        appeared = {}
        for line in f:
            line = line.strip().split('(contains')
            ingredients = line[0].strip().split(' ')
            list_of_foods.append(ingredients)
            allergens = line[1].strip().split(',')
            allergens[-1] = allergens[-1].replace(')', '')
            for allergen in allergens:
                allergen = allergen.strip()
                if allergen not in ingredients_map.keys():
                    ingredients_map[allergen] = ingredients[:]
                    appeared[allergen] = 1
                else:
                    ingredients_map[allergen] += ingredients
                    appeared[allergen] += 1

    ans1, final_allergens = part1(ingredients_map, appeared, list_of_foods)
    print('part1:', ans1)
    ans2 = part2(final_allergens)
    print('part2:', ans2)


main()
