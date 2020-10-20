"""Try creating a program that opens file.txt. Read each line of the file and then prepend it with a line number."""

with open('file.txt') as file:
    line_nr = 1
    for line in file:
        print("{}".format(line.rstrip()))
        line_nr += 1
