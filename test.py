# http://stackoverflow.com/questions/4634317/excel-solver-in-python

print range(1,9)

for i in range(1,10):
    print i
    
repls = {'hello' : 'goodbye', 'bye' : 'moon' , 'world' : 'earth'}
s = 'hello, world'
print reduce(lambda a, kv: a.replace(*kv), repls.iteritems(), s)

if('Py' in 'Python'):
    print "true"



