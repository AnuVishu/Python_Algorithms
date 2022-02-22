
#list should be in sorted order
def Binary_Search(lst,number_to_find):
    left_index = 0
    right_index = len(lst)-1
    mid_index =0
    while left_index <= right_index:
        mid_index = (left_index+right_index)//2
        mid_number = lst[mid_index]

        if mid_number == number_to_find:
            return mid_index
        elif mid_number < number_to_find:
            left_index = mid_index+1
        else:
            right_index = mid_index -1
    return -1


print(Binary_Search([12, 15, 17, 19, 21, 24, 45, 67],45))
