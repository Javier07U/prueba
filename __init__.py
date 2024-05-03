def add(num_1, num_2):
    result = num_1 + num_2
    return result

def subtract(num_1, num_2):
    result = num_1 - num_2
    return result

def multiply(num_1, num_2):
    result = num_1 * num_2
    return result

def divide(num_1, num_2):
    if num_2 == 0:
        print("Error: División por cero no está permitida.")
        return None
    result = num_1 / num_2
    return result

def power(base, exponent):
    result = base ** exponent
    return result

def modulus(num_1, num_2):
    if num_2 == 0:
        print("Error: Módulo por cero no está permitido.")
        return None
    result = num_1 % num_2
    return result

def game():
    score = 0
    operations = {
        1: add,
        2: subtract,
        3: multiply,
        4: divide,
        5: power,
        6: modulus
    }

    while True:
        print('======== Menu ========')
        print('1. Add')
        print('2. Subtract')
        print('3. Multiply')
        print('4. Divide')
        print('5. Power')
        print('6. Modulus')
        print('0. Exit')
        option = int(input('\nChoose an option: '))

        if option == 0:
            break

        if option not in operations:
            print('Invalid option. Try again.')
            continue

        num_1 = int(input('Enter first number: '))
        num_2 = int(input('Enter second number: '))
        answer = int(input('Enter your answer: '))

        operation = operations[option]
        if option == 5:
            result = operation(num_1, int(num_2))
        else:
            result = operation(num_1, num_2)

        if result is not None and result == answer:
            score += 1
            print('Correct!!')
        else:
            print('Incorrect')

    print(f'======== Game Over ========')
    print(f'Your score is {score}')
    print('Keep going!')

game()