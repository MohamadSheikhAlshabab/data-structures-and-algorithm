
def symmetry(input):
    a=input 
    n = len(a) 
    flag = 0
    if n%2: 
        mid = n//2 +1
    else: 
        mid = n//2
    start1 = 0
    start2 = mid 
    while(start1 < mid and start2 < n): 
        if (a[start1]== a[start2]): 
            start1 = start1 + 1
            start2 = start2 + 1
        else: 
            flag = 1
            break
    if flag == 0: 
        # print(False,input,"1") 
        return False

    else: 
        # print(True,input,"1") 
        return True

def palindrome(input): 
    a=input
    mid = (len(a)-1)//2
    start = 0
    last = len(a)-1
    flag = 0
    while(start<mid): 
        if (a[start]== a[last]): 
            start += 1
            last -= 1
        else:
            flag = 1
            break; 
    if flag == 0: 
        # print(False,input,"2") 
        return False

    else: 
        # print(True,input,"2") 
        return True

def multi_bracket_validation(input):

    if (input.count("{") != input.count("}")) :
        print(False,input,"3")
        return False
            
    if (input.count("[") != input.count("]")) :
        print(False,input,"4")
        return False   

    if (input.count("(") != input.count(")")) :
        print(False,input,"5")
        return False

    elif (input.count("(") == 0 ) and (input.count(")") == 0 )and (input.count("[") == 0 ) and (input.count("]") == 0 )and(input.count("{") == 0 ) and (input.count("}") == 0 ):
        print(False,input,"6")
        return False

    elif (input.count("{") == input.count("}")) :
        print(True,input,"7")
        return True
        # if symmetry(input) and  palindrome(input):
        #     print(True,input,"7")
        #     return True
        # else:
        #     print(False,input,"7")
        #     return False

    else:
        print(True,input,"8") 
        return True
if __name__ == "__main__":
   multi_bracket_validation("{}")
   multi_bracket_validation("{}(){}")
   multi_bracket_validation("(){}[[]]")
   multi_bracket_validation("{}{Code}[Fellows](())")
   multi_bracket_validation("(){}[[]]")
   multi_bracket_validation("(](")
   multi_bracket_validation("{(})")
   multi_bracket_validation("{")
   multi_bracket_validation(")")
   multi_bracket_validation("[}")
   multi_bracket_validation("[ff}")
   multi_bracket_validation("g9(")
   multi_bracket_validation("ff")
   multi_bracket_validation("}f}{f{")
   multi_bracket_validation("}f[][]{")
