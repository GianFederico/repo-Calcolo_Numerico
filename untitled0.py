import numpy as np

def f(x):
    return 4678

itermax=int(input(print("iterate max: ")))
toll=float(input(print("precisione iniziale: ")))
toll_fin=float(input(print("precisione finale: ")))

x0=1
numiter=0


while toll>toll_fin and numiter<itermax:
      
    x1= (1/3)*(2*x0+((f(x0))/x0**2))
    toll=abs((x1-x0)/x1)
    x0=x1
    
    numiter=numiter+1
    print(x0)
        
        
print("\nradice:",x0,"\nnumero iterate:",numiter)
    
    
