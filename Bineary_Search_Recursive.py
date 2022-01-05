
def Binary_Search_Recursive(lst,number_to_find,left_index,right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index)//2

    if mid_index < 0 or mid_index > len(lst):
        return -1

    if number_to_find == lst[mid_index]:
        return mid_index
    elif lst[mid_index] < number_to_find:
        left_index = mid_index +1
    else:
        right_index = mid_index -1

    return Binary_Search_Recursive(lst,number_to_find,left_index,right_index)

lst =[12, 15, 17, 19, 21, 24, 45, 67]
print(Binary_Search_Recursive(lst,67,0,len(lst)))
