gh = ['lists']
#print(dir(gh))

print('----------------------------------------------------------------------------------')

cd = 'wfvjnkqwe'
#print(dir(cd))

#print(gh.upper())

#direct the file path into the string
file = ('/home/ubuser/Documents/mbox.txt')
#open the file
view = open(file)
"""for line in view:
    #showing txt file contents of each line
    print(line)"""

#for line in view:
    #showing contents exclude whitespace between lines
    #print(line.rstrip())
    # showing contents exclude whitespace with all capital words
    #print(line.rstrip().upper())
    # showing contents exclude whitespace with reverse case
    #print(line.rstrip().swapcase())

#for line in view:
    #   showing contents in the bracket of each line
    #print(line.rsplit())


#searching each specific words in the file
"""count = 0
for line in view:
    # filter specific words in the contents
    if line.startswith('From '):
        #select each line of contents
        v = line
        #   count every single specific word
        count = count + 1
        #   print each found result
        print(v)
        #   print each found result without whitespace
        #print(v.rstrip())
        #   print each found result without whitespace plus bracket
        #print(v.rstrip().rsplit())
print('There are ' + str(count) + ' lines.')"""


#create empty list
"""List = list()
view = open(file)
count = 0
for line in view:
    if not line in List:
        List.append(line)
print(List)"""

"""New_file = ('/home/ubuser/Documents/ntif.txt')
Open_file = open(New_file)
New_list = list()
count = 0
for line in Open_file:
    modify = line.rstrip().rsplit()
    for i in modify:
        #split each i start word and skip the word
        if not i in New_list:
            New_list.append(i)

#sort wirh each list stating words
New_list.sort()
print(New_list)"""

a = 'Puppy'
print(a)
print(type(a))
print()

b = b'Pussy'
print(b)
print(type(b))
print()

c = bytearray(b)
print(c)
print(type(c))
print()

d = list(a)
print(d)
print(type(d))
print()

e = tuple(a)
print(e)
print(type(e))
print()

f = range(10)
print(f)
print(type(f))
print()


