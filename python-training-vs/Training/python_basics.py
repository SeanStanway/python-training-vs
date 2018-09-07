import customFunctions as func
def my_function():
    a = 2
    return a
func.print_function("Function:", my_function())

func.newLine()

b = 5
c = 7
if b > c:
    func.print_function('If Statement:', 'b is more than c')
else:
    func.print_function('If Statement:','c is more than b')

func.newLine()

import math
newMath = math.sqrt(16)
func.print_function('Math Import:', newMath)

func.newLine()

int_list = [1, 2, 3]
string_list = ['test', '123']
nested_list = [['nest', 'two'], [100, 200]]
func.print_function('Int List:', int_list)
func.print_function('Int List, Single Value:', int_list[1])
func.newLine()
func.print_function('String List:', string_list)
func.print_function('String List, Negative Counting ([-2]):',string_list[-2])
func.newLine()
func.print_function('Nested List:', nested_list)
func.print_function('Nested List, Single Value:', nested_list[0][1])
nested_list[0][1] = 'New Stuff'
func.print_function('Nested List, Mutated Value', nested_list)
int_list.insert(3, 4)
func.newLine()
func.print_function('Int List, Insert:', int_list)
int_list.remove(2)
func.print_function('Int List, Remove', int_list)
func.print_function('Int List, Len(gth):', len(int_list))
func.print_function('String List, Index Location:', string_list.index('123'))

func.newLine()

print('-----For Loop')
for element in int_list:
    print (element)
print('-----For Loop END')

func.newLine()

newTuple = ('127.0.0.1', '443')
func.print_function('Tuple (Fixed list):', newTuple)
singleMemeberTuple = tuple(['Single Member'])
func.print_function('Tuple (Single entry):', singleMemeberTuple)

func.newLine()

newDictionary = {
    'firstEntry': 'value one',
    'secondEntry': 'value two',
    'thirdEntry': 'value three',
    'fourthEntry': 'value four'
}
func.print_function('Dictionary:', newDictionary)
func.print_function('Dictionary, Single Entry:', newDictionary['thirdEntry'])
print('------For Loop')
print('Dictionary, For Loop for all Keys:')
for key in newDictionary.keys():
    print(key)
print('-----For Loop END')

func.newLine()

newSet = {'Charlie','Jon','Tony'}
func.print_function('Set, Sorted List-No Repeats:', newSet)
int_setList = set(int_list)
func.print_function('Set, from old list:', int_setList)
func.newLine()
name = 'Charles'
print('Name to look for in set: {}'.format(name))
if name in newSet:
    print(name)
else:
    print('not found')
name = 'Jon'
print('Name to look for in set: {}'.format(name))
if name in newSet:
    print(name)
else:
    print('not found')

func.newLine()

from collections import defaultdict
newDictionary = defaultdict(lambda: 'Key does not exist')
newDictionary['firstEntry'] = 'value one'
newDictionary['secondEntry'] = 'value two'
newDictionary['thirdEntry'] = 'value three'
newDictionary['fourthEntry'] = 'value four'
func.print_function('Default Dict, adds default for dictionary (no key present):', newDictionary['randomValue'])
func.print_function('Default Dict, using key that is present:', newDictionary['firstEntry'])