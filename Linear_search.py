
def linear_search(lst,search_num):
    for index,value in enumerate(lst):
        if value == search_num:
            return index

    return -1



print(linear_search([12, 15, 17, 19, 21, 24, 45, 67],20))
