base_price =  float(input('Enter the base price: '))
age = int(input('Enter age: '))
seat_type = input('Enter seat type (Premium/Gold): ')
show_time = input('Enter show time (Evening/Morning): ')

if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

is_member = input('Are you a member? (yes/no): ') == 'yes'
is_weekend = input('Is it weekend? (yes/no): ') == 'yes'

discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    else:
        service_charges = 1
        print('Service charges:', service_charges)
else:
    print('Ticket booking failed due to restrictions')