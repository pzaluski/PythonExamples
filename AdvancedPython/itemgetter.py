import operator

get_second_item = operator.itemgetter(1)

ls = ['a', 'b', 'c', 'd']
print(get_second_item(ls))
print(operator.itemgetter(1,3,5,)('abcdefg'))