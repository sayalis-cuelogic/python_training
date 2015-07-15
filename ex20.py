from sys import argv

script , file_name = argv

def print_all(data):
	print "Data from file : ", file_name
	print data.read()

def rewind(f):
	f.seek(0)

def print_line(line_count,f):
	print line_count,f.readline()

input_data = open(file_name)
print_all(input_data)

print "Let's rewind, kind of like a tape."
rewind(input_data)

print "Let's read line by line "
line_no = 1
print_line(line_no,input_data)

line_no = line_no + 1
print_line(line_no,input_data)

line_no = line_no + 1
print_line(line_no,input_data)

line_no = line_no + 1
print_line(line_no,input_data)
