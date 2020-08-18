  
def reverseArray(alist):
    alist.reverse()
    print(alist)

list1=[1, 2, 3, 4, 5, 6]
list2=[89, 2354, 3546, 23, 10, -923, 823, -12]
list3=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

reverseArray(list1)
reverseArray(list2)
reverseArray(list3)

def reverseArray2(alist):
    new=alist.copy()
    anew=new[::-1]
    print(new,"saassaaasda")
    print(anew,"sdsd")

reverseArray2(list1)
reverseArray2(list2)
reverseArray2(list3)