#Thu Aug 6, 2026

numbers = range(10)
new_dict_for = {}

# Add values to `new_dict` using for loop
for n in numbers:
    if n%2==0:
        new_dict_for[n] = n**2

print(new_dict_for)


# Use dictionary comprehension
new_dict_comp = {n:n**2 for n in numbers if n%2 == 0}

print(new_dict_comp)


a = {'apple': 'fruit', 'beetroot': 'vegetable', 'cake': 'dessert'}
a['doughnut'] = 'snack'
print(a['apple'])
