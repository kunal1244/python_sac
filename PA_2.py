T=int(input())                                               # input no. of test cases
if T>=1 and T<=100:
    top = -1              
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}         #setting up precedence orders
    def pop(arr,top):                                        #defining the pop function
        if top!=-1:
            return arr.pop()
        else:
            return "UNDERFLOW"                               #returns underflow if array empty
     
    def push(array,op):                                      #defining the push function
        array.append(op)
        return 
   
    def check_pre(i,array):                                  #comparing precedence orders of operators
        precedence = {'+':1, '-':1, '*':2, '/':2, '^':3} 
        try:
            a = precedence[i]
            b = precedence[array[-1]]
            return True if a  <= b else False
        except KeyError: 
            return False
             

    def inpos(exp):
        top = -1              
        final = []                                           #defining an output and stack array
     
        stack=[]
        for i in exp:
            if i.isalpha():
                final.append(i)
            elif i  == '(':                                  #pushing every element after the '(' to the stack
                push(stack,i)
                top+=1
            elif i == ')':                                   #popping every element at end of bracket
                while(top!=-1 and stack[-1] != '('):
                    a = pop(stack,top)
                    top-=1
                    final.append(a)
                if (top!=-1 and stack[-1] != '('):
                    return -1                                #ensuring sequence does not end at '('
                else:
                    pop(stack,top)
                    if top!=-1:
                        top-=1
            else:
                while(top!=-1 and check_pre(i,stack)):
                    final.append(pop(stack,top))
                    top-=1
                push(stack,i)
                top+=1
 
        
        while not isEmpty(top):                              #popping out remaining operators
            final.append(pop(stack,top))
            if top!=-1:
                top-=1
 
        return "".join(final)     
    l=[]   
    for i in range(T):
        exp=input()
        if len(exp)>=1 and len(exp)<=30:                     #checking constraint for length of infix expression
            l.append(exp)
    for i in l:
        print(inpos(i))
