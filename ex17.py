from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying file from %s to %s" % (from_file , to_file)

in_file = open(from_file)
in_data = in_file.read()

print "Length of file is ",  len(in_data)
print "Is file exists ?? " , exists(to_file)

print "Hit Return to continue or Ctrl-C to abort"
raw_input()

out_file=open(to_file,'w')
out_file.write(in_data)

print "Copying file is done.."

in_file.close()
out_file.close()