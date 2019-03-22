import sys
import fileinput

# replace all occurrences of 'sit' with 'SIT' and insert a line after the 5th
for line in fileinput.input('out_test11.txt', inplace=1):
    sys.stdout.write(line.replace('------', '---\n---'))  # replace 'sit' and write