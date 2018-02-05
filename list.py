classmates = ['tom','jack','peter']
print(classmates[-1])

#add in the end
classmates.append('adam')
print(classmates)

#delete the end
classmates.pop()
print(classmates)

tpl = ('1','2', ['3','4'])
print(tpl)
tpl[2][0] = '9'
print(tpl)