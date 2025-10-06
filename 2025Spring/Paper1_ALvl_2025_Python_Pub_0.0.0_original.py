import re
import random
import math
from collections import deque
from typing import List

def main() -> None:
    numbers_allowed: List[int] = []
    targets: List[int] = []
    max_number_of_targets = 20
    max_target = 0
    max_number = 0
    training_game = False
    choice = input("Enter y to play the training game, anything else to play a random game: ").lower()
    print()
    if choice == "y":
        max_number = 1000
        max_target = 1000
        training_game = True
        targets = [-1] * 4 + [-1, 23, 9, 140, 82, 121, 34, 45, 68, 75, 34, 23, 119, 43, 23, 119]
    else:
        max_number = 10
        max_target = 50
        targets = create_targets(max_number_of_targets, max_target)
    numbers_allowed = fill_numbers(numbers_allowed, training_game, max_number)
    play_game(targets, numbers_allowed, training_game, max_target, max_number)
    input()

def play_game(targets: List[int], numbers_allowed: List[int], training_game: bool, max_target: int, max_number: int) -> None:
    score = 0
    game_over = False
    while not game_over:
        display_state(targets, numbers_allowed, score)
        user_input = input("Enter an expression: ")
        print()
        if check_if_user_input_valid(user_input):
            user_input_in_rpn = convert_to_rpn(user_input)
            if check_numbers_used_are_all_in_numbers_allowed(numbers_allowed, user_input_in_rpn, max_number):
                is_target, score = check_if_user_input_evaluation_is_a_target(targets, user_input_in_rpn, score)
                if is_target:
                    numbers_allowed = remove_numbers_used(user_input_in_rpn, max_number, numbers_allowed)
                    numbers_allowed = fill_numbers(numbers_allowed, training_game, max_number)
        score -= 1
        if targets[0] != -1:
            game_over = True
        else:
            targets = update_targets(targets, training_game, max_target)
    print("Game over!")
    display_score(score)

def check_if_user_input_evaluation_is_a_target(targets: List[int], user_input_in_rpn: List[str], score: int) -> tuple[bool, int]:
    user_input_evaluation = evaluate_rpn(user_input_in_rpn)
    user_input_evaluation_is_a_target = False
    if user_input_evaluation != -1:
        for count in range(len(targets)):
            if targets[count] == user_input_evaluation:
                score += 2
                targets[count] = -1
                user_input_evaluation_is_a_target = True
                break  # Early exit once found
    return user_input_evaluation_is_a_target, score

def remove_numbers_used(user_input_in_rpn: List[str], max_number: int, numbers_allowed: List[int]) -> List[int]:
    for item in user_input_in_rpn:
        if check_valid_number(item, max_number):
            num = int(item)
            if num in numbers_allowed:
                numbers_allowed.remove(num)
    return numbers_allowed

def update_targets(targets: List[int], training_game: bool, max_target: int) -> List[int]:
    targets[:] = targets[1:]  # Shift left
    if training_game:
        targets.append(targets[-1])
    else:
        targets.append(get_target(max_target))
    return targets

def check_numbers_used_are_all_in_numbers_allowed(numbers_allowed: List[int], user_input_in_rpn: List[str], max_number: int) -> bool:
    temp = numbers_allowed[:]
    for item in user_input_in_rpn:
        if check_valid_number(item, max_number):
            num = int(item)
            if num in temp:
                temp.remove(num)
            else:
                return False
    return True

def check_valid_number(item: str, max_number: int) -> bool:
    return bool(re.match(r"^[0-9]+$", item)) and 0 < (item_int := int(item)) <= max_number

def display_state(targets: List[int], numbers_allowed: List[int], score: int) -> None:
    display_targets(targets)
    display_numbers_allowed(numbers_allowed)
    display_score(score)

def display_score(score: int) -> None:
    print(f"Current score: {score}")
    print()
    print()

def display_numbers_allowed(numbers_allowed: List[int]) -> None:
    print("Numbers available: ", end="")
    print("  ".join(map(str, numbers_allowed)), end="")
    print()
    print()

def display_targets(targets: List[int]) -> None:
    print("|", end="")
    for t in targets:
        print(" " if t == -1 else str(t), end="")
        print("|", end="")
    print()
    print()

def convert_to_rpn(user_input: str) -> List[str]:
    position = 0
    precedence = {"+": 2, "-": 2, "*": 4, "/": 4}
    operators = []
    user_input_in_rpn = []
    operand, position = get_number_from_user_input(user_input, position)
    if operand != -1:
        user_input_in_rpn.append(str(operand))
        if position < len(user_input):
            operators.append(user_input[position - 1])
    while position < len(user_input):
        operand, position = get_number_from_user_input(user_input, position)
        if operand != -1:
            user_input_in_rpn.append(str(operand))
            if position < len(user_input):
                current_operator = user_input[position - 1]
                while operators and precedence[operators[-1]] > precedence[current_operator]:
                    user_input_in_rpn.append(operators.pop())
                if operators and precedence[operators[-1]] == precedence[current_operator]:
                    user_input_in_rpn.append(operators.pop())
                operators.append(current_operator)
            else:
                while operators:
                    user_input_in_rpn.append(operators.pop())
    return user_input_in_rpn

def evaluate_rpn(user_input_in_rpn: List[str]) -> int:
    s = []
    rpn = deque(user_input_in_rpn)
    while rpn:
        if rpn[0] not in {"+", "-", "*", "/"}:
            s.append(rpn.popleft())
        else:
            if len(s) < 2:
                return -1
            num2 = float(s.pop())
            num1 = float(s.pop())
            op = rpn.popleft()
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                if num2 == 0:
                    return -1
                result = num1 / num2
            else:
                return -1
            s.append(str(result))
    if len(s) != 1:
        return -1
    result = float(s[0])
    return math.floor(result) if result.is_integer() else -1

def get_number_from_user_input(user_input: str, position: int) -> tuple[int, int]:
    number = ""
    more_digits = True
    while more_digits and position < len(user_input):
        if re.match(r"[0-9]", user_input[position]):
            number += user_input[position]
        else:
            more_digits = False
        position += 1
    return (int(number), position) if number else (-1, position)

def check_if_user_input_valid(user_input: str) -> bool:
    return bool(re.match(r"^([0-9]+[+\-*/])+[0-9]+$", user_input))

def get_target(max_target: int) -> int:
    return random.randint(1, max_target)

def get_number(max_number: int) -> int:
    return random.randint(1, max_number)

def create_targets(size_of_targets: int, max_target: int) -> List[int]:
    return [-1] * 4 + [get_target(max_target) for _ in range(size_of_targets - 4)]

def fill_numbers(numbers_allowed: List[int], training_game: bool, max_number: int) -> List[int]:
    if training_game:
        return [2, 3, 2, 8, 512]
    while len(numbers_allowed) < 5:
        numbers_allowed.append(get_number(max_number))
    return numbers_allowed

if __name__ == "__main__":
    main()
