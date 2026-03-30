factors = {
    "mm": 0.001,
    "cm": 0.01,
    "m":  1.0,
    "km": 1000.0,
    "in": 0.0254,
    'kg': 1.0,
    'g':0.001,
    'lbs': 0.4535924,
}

def convert(from_unit , amount , to_unit):
    base_val = amount * factors[from_unit]
    result = base_val / factors[to_unit]
    return f'{result}{to_unit}'



while True:
    print('1. Length')
    print('2. Weight')
    print('3. Exit')
    choice = int(input('Pick a choice: '))
    if choice ==1:
        print('Options: mm, cm, m, km, in')
        unit_from = input('Convert FROM: ')
        unit_to = input('Convert TO: ')
        amount = float(input('Enter amount: '))
    elif choice ==2:
        print('Options: kg , g , lbs')
        unit_from = input('Convert FROM: ')
        unit_to = input('Convert TO: ')
        amount = float(input('Enter amount: '))


    elif choice ==3:
        print('Closing...')
        break
    else:
        print('Type A Valid Number')
    converted =convert(unit_from, amount , unit_to)
    print(f'{amount}{unit_from} is {converted}')