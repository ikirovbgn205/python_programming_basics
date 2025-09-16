number_one = int(input())
number_two = int(input())
operator = input()

result = ''

if operator == '+':
    result = f"{number_one} + {number_two} = {number_one + number_two} {'- even' if (number_one + number_two ) % 2 == 0 else '- odd'}"

elif operator == '-':
    result = f"{number_one} - {number_two} = {number_one - number_two} {'- even' if (number_one - number_two) % 2 == 0 else '- odd'}"

elif operator == '*':
    result = f"{number_one} * {number_two} = {number_one * number_two} {'- even' if (number_one * number_two) % 2 == 0 else '- odd'}"

elif number_two == 0:
    print(f"Cannot divide {number_one} by zero")

elif operator == '/':
    result = f"{number_one} / {number_two} = {number_one / number_two:.2f}"

elif operator == '%':
    result = f"{number_one} % {number_two} = {number_one % number_two}"

print(result)
