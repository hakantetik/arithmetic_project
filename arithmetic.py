from random import randint, choice


def calculator(x, y, operator):
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "*":
        return x * y
    elif operator == "/":
        return x / y


def check_answer(answer_, result_):
    if answer_ == result_:
        return True
    else:
        return False


while True:
    operators = ["*", "-", "+"]

    correct = 0

    while True:
        level = int(input("Which level do you want? Enter a number:"))
        if level == 1 or level == 2:
            break
        else:
            print("Incorrect format.")
            continue

    for i in range(5):
        if level == 1:
            random_num1, random_num2, random_operator = randint(2, 9), randint(2, 9), choice(operators)
            result = calculator(random_num1, random_num2, random_operator)

            entry = f"{random_num1} {random_operator} {random_num2}"
        elif level == 2:
            random_num = randint(11, 29)
            result = random_num ** 2

            entry = random_num

        while True:
            try:
                print(entry)
                answer = int(input(""))
            except ValueError:
                print("Wrong format! Try again.")
                continue
            break

        if check_answer(answer, result):
            print("Right!")
            correct += 1
        else:
            print("Wrong!")

    print(f"Your mark is {correct}/5. Would you like to save the result? Enter yes or no.")

    response = input()

    if level == 1:
        description = "simple operations with numbers 2-9"
    elif level == 2:
        description = "integral squares 11-29"

    if response in ["yes", "YES", "y", "Yes"]:
        name = input("What is your name?")
        text = f"{name}: {correct}/5 in level {level} ({description})."
        with open("results.txt", "a+") as file:
            file.write(text)
        print('The results are saved in "results.txt".')
    else:
        break
    break
