words="Na obiad beda pierogi ale co z tego".split()

#my idea
lista=[]
for word in words:
    lista.append(len(word))
print(lista)


#better idea
# [expr(item) for item in iterable]
print(type([len(word) for word in words]))

# { key_expr:value_expr for item in iterable }
# example:
from pprint import pprint as pp 

country_to_capital = {'UK': 'London',
                      'Poland': 'Warsaw',
                      'Ukraine': 'Kiev'
}

print(type(country_to_capital))
print(type(country_to_capital.items()))


capital_to_country={capital: country for country,capital in country_to_capital.items()}
print(capital_to_country)

print(type(range(5)))