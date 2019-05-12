def in_list(list,s):
    min=0
    max=len(list)-1
    while(min<=max):
        mid = (min+max) // 2
        if(list[mid] == s):
            return True
        if list[mid] < s:
            min = mid+1
        else:
            max = mid-1
            return False

print (in_list([1,2,3,4,5,8],4))
print (in_list([1,2,3,4,5,8],10))
print (in_list([1,2,3,4,5,8],0))
print (in_list([1,2,3,4,5,8],7))

input("Press Enter to exit")