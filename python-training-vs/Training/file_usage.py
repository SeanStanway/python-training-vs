import customFunctions as func

with open('TestFile.txt', 'w') as fileobj:
    fileobj.write('New line in file\nThis is confusing to write like this\nWhat the heck')

with open('TestFile.txt', 'r') as fileobj:
    lines = fileobj.readlines()
    func.print_function("File content:", lines)
    
func.newLine()

with open('TestFile.txt', 'r') as fileobj:
    content = fileobj.read()
    split_lines = content.split('\n')
    func.print_function(r"Split file content (\n):",split_lines)

func.newLine()

fileobj = open('TestFile.txt', 'r')
position = fileobj.tell()
func.print_function("Find position in file (.tell):", position)

fileobj.read()
end_position = fileobj.tell()
func.print_function("Find position in file (after read):", end_position)
print('Close object')
fileobj.close()

func.newLine()

fileobj = open('TestFile.txt', 'r')
fileobj.seek(10)
position = fileobj.tell()
func.print_function("Use .seek to move to specific position (i.e. 10th):", position)

func.newLine()

print('Start file again')
fileobj.seek(0)
firstTen = fileobj.read(10)
func.print_function("Read next 10 characters using .read:", firstTen)
position = fileobj.tell()
func.print_function("Find position:", position)
print('Close object')
fileobj.close()

func.newLine()

with open('TestFile.txt', 'rb') as fileobj:
    func.print_function('Read file bytes using \'rb\' instead of \'r\':', type(fileobj.read()))
    fileobj.close()