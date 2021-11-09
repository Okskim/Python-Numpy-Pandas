import os
cwd = os.getcwd()
print (cwd)

os.path.exists('my_file')
os.listdir(path)

def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
    if os.path.isfile(path):
       print (path)
    else:
       walk(path)
walk(path)

import sys
def getlocaldata(sms,dr,flst):
    for f in flst:
        fullf = os.path.join(dr,f)
        if os.path.islink(fullf): 
             continue
        if os.path.isfile(fullf):
             sms[0] += os.path.getsize(fullf)
             sms[1] += 1
        else:
             sms[2] += 1

def dtstat(dtroot):
    sums = [0,0,1] 
    os.path.walk(dtroot,getlocaldata,sums)
    return sums
    report = dtstat('.')
    print (report)

import fnmatch
mask = '*.py'
pattern = 'import os'
def walk(arg,dir,files):
    for file in files:
        if fnmatch.fnmatch(file,mask):
            name = os.path.join(dir,file)
    try:
        data = open(name,'rb').read()
        if data.find(pattern) != -1:
            print (name)
    except:
        pass
    os.path.walk('.',walk,[])
