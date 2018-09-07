def print_function(exampleName, content):
    print('{} {}'.format(exampleName, content))
def newLine():
    print('')

def my_function():
    a = 2
    return a
print_function("Function:", my_function())

newLine()

b = 5
c = 7
if b > c:
    print_function('If Statement:', 'b is more than c')
else:
    print_function('If Statement:','c is more than b')

newLine()

import math
newMath = math.sqrt(16)
print_function('Math Import:', newMath)

newLine()

int_list = [1, 2, 3]
string_list = ['test', '123']
nested_list = [['nest', 'two'], [100, 200]]
print_function('Int List:', int_list)
print_function('Int List, Single Value:', int_list[1])
newLine()
print_function('String List:', string_list)
print_function('String List, Negative Counting ([-2]):',string_list[-2])
newLine()
print_function('Nested List:', nested_list)
print_function('Nested List, Single Value:', nested_list[0][1])
nested_list[0][1] = 'New Stuff'
print_function('Nested List, Mutated Value', nested_list)
int_list.insert(3, 4)
newLine()
print_function('Int List, Insert:', int_list)
int_list.remove(2)
print_function('Int List, Remove', int_list)
print_function('Int List, Len(gth):', len(int_list))
print_function('String List, Index Location:', string_list.index('123'))

newLine()

print('-----For Loop')
for element in int_list:
    print (element)
print('-----For Loop END')

newLine()

newTuple = ('127.0.0.1', '443')
print_function('Tuple (Fixed list):', newTuple)
singleMemeberTuple = tuple(['Single Member'])
print_function('Tuple (Single entry):', singleMemeberTuple)