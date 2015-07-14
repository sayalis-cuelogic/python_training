from sys import argv

script , file_name = argv

txt = open(file_name)

print "Your File name is ", file_name
print txt.read()

print "Enter next file name which you want read "
file_name1=raw_input(">")

txt1 = open(file_name1)
print txt1.read()
