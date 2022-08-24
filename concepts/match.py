# available in python 3.10 >

role = 'standard'

match role:
    case 'standard':
        print('Standard role')
    case 'admin':
        print('Admin role')
    case 'superAdmin':
        print('Super admin role')
    # default
    case _:
        print('Not valid role')

client = {
    'name': 'Jane',
    'age': 21,
    'occupation': 'Actress'
}

movie = {
    'title': 'Bastardos sin gloria',
    'technical_data': {
        'protagonist': 'Brad Pitt',
        'director': 'Tarantino'
    }
}

elements = [client, movie, 'book']

for e in elements:
    match e:
        case {'name': name, 'age': age, 'occupation': occupation}:
            print(f'Is client: {name}, {age} years, {occupation}')
        case {'title': title, 'technical_data': {
            'protagonist': protagonist,
            'director': director
        }}:
            print(f'Is movie: {title}, {protagonist}, {director}')
        case _:
            print('Other value')
