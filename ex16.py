from sys import argv
script , file_name = argv

print "I am going to delete the contents of the %s file" % file_name
print "Hit Ctrl + c if you don't want"

print "If you do want that, hit RETURN."
raw_input("?")

print "Opening File ", file_name
txt = open(file_name,'w')

print "deleting contents...."
txt.truncate()

print "Now, Enter new 3 lines "

line1 = raw_input("Line1 : ")
line2 = raw_input("Line2 : ")
line3 = raw_input("Line3 : ")

print "Writing contents to the file...."
txt.write(line1)
txt.write("\n")
txt.write(line2)
txt.write("\n")
txt.write(line3)
txt.write("\n")

print "Closing file..."
txt.close()