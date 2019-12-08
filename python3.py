import numpy as np
import ast

astr = input('Create an array with two columns: ')
alist = ast.literal_eval(astr)

e = np.asarray(alist)
l = len(e)
e1 = e[0:,0]
e2 = e[0:,1]


polyfit = []
polyval = []
error = []
leastnorm = []

def python3(e):
    
    for n in range(l):
        
        if n <=10:
        
            q = np.polyfit(e1,e2,n)
            polyfit.append(q)
            
            t = np.polyval(q,e1)
            polyval.append(t)
            
            p = np.linalg.norm(e2 - t)
            error.append(p)
            
            ln =np.min(p)
            leastnorm.append(ln)
            
        elif n > 10:
            
            quit('You exceeded the maximum degree.')
    print('')
    print('')
    print('The Coefficients are: ',t,'')
    print('')
    print('')
    print('e(x): ',ln,'')
    
python3(e)
        