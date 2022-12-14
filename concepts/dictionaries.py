user = {'name': 'Bruce', 'lastname': 'Wayne'}

user_name = user['name']  # out: 'Bruce'
# user['power']  # out: Error

user.get('name')  # out: 'Bruce'
user.get('power')  # out: None

user['power'] = 'Rich'

print(user.keys())
print(user.values())
print(user.items())

print(list(user.keys()))
print(list(user.values()))
print(list(user.items()))

# spread operator for dictionaries
my_dic_1 = {'name': 'Jane', 'lastname': 'Hope'}
new_user = {**my_dic_1, 'age': 35}  # {'name': 'Jane', 'lastname': 'Hope', 'age': 35}
