def solution(after_recipes, part):
    target = [int(s) for s in after_recipes]
    recipes = [3, 7]
    first_Elf = 0
    second_Elf = 1

    while True:
        new_recipe = recipes[first_Elf] + recipes[second_Elf]
        if new_recipe >= 10:
            new1 = new_recipe // 10
            new2 = new_recipe % 10
            recipes.append(new1)
            recipes.append(new2)
        else:
            recipes.append(new_recipe)
        first_Elf = (first_Elf + 1 + recipes[first_Elf]) % len(recipes)
        second_Elf = (second_Elf + 1 + recipes[second_Elf]) % len(recipes)

        if part == 1:
            if len(recipes) > int(after_recipes) + 10:
                return recipes[int(after_recipes): int(after_recipes) + 10]
        elif part == 2:
            if recipes[-6:] == target[:]:
                return len(recipes) - 6
            if recipes[-7:-1] == target[:]:
                return len(recipes) - 7
        else:
            return


def main():
    with open('input/input14.txt', 'r') as f:
        after_recipes = f.read().strip()  # '074501'

    ten_recipes = solution(after_recipes, 1)
    ten_recipes = ''.join([str(num) for num in ten_recipes])
    print('part 1:', ten_recipes)
    left_recipes_of_input = solution(after_recipes, 2)  # need a few seconds
    print('part 2:', left_recipes_of_input)


main()
