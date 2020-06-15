import re

with open('in.txt') as intxt:
    data = intxt.read()

x = re.findall('[aA-zZ]+', data)
print(x)

##which will produce
##
##['Hello', 'my', 'name', 'is', 'Gareth', 'and', 'in', 'this', 'video', 'I', 'm', 'going', 'to', 'talk', 'about', 'list', 'comprehensions', 'in', 'Python']
##
##You can now write x to a new file with:
##
##with open('out.txt', 'w') as outtxt:
##    outtxt.write('\n'.join(x))
##
##To get
##
##I'm
##
##instead of
