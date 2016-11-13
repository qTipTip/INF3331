import sys

#This function takes two different files as input.
#It splits each file at '\n' and feeds them into a list.
#The functions then starts at original[0] to see if in modified
#If not it is popped and entered into out. Since supderdiff is pop-ing every
#element one never has to use any other index than 0. When both lists are empty
#the result is printed. If both lines in both files equals '' it is skipped.
def superdiff(input1, input2):
    file1 = open(input1, "r").read()
    file2 = open(input2, "r").read()
    original = file1.split('\n')
    modified = file2.split('\n')
    out = []
    while(len(original)>0 or len(modified)>0):
        if original[0] in modified:
            index = modified.index(original[0])
            for i in range(0, index):
                out.append('+ ' + modified.pop(0))
            remove = modified.pop(0)
            add = original.pop(0)
            if remove==add=='':
                continue
            else:
                out.append('0 ' + add)
        elif original[0]=='' or len(original)==0:
            add = modified.pop(0)
            out.append('+ ' + add)
        else:
            out.append('- ' + original.pop(0))

#The file is written. If a file with the the same name exist
#This file will be over written.
    file3 = open('diff_output.txt', 'w')
    for elem in out:
        file3.write(elem + '\n')
        print(elem)
    file3.close()

superdiff(sys.argv[1], sys.argv[2])
