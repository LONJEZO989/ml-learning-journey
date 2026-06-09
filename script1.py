def check_age(age):
    if not isinstance(age, (int, float)):
        return "The age should be a number"

    if age <= 0:
        return "Age must be greator than 0"

    if age < 18:
        return "Too young"

    else:
        return "You are allowed"

age = int( input('Enter your age: '))
print(check_age(age))