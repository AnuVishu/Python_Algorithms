
def func_quad(lst):
    """
    prints pairs of every item in list
    :param lst:
    :return:
    """
    for item_1 in lst:
        for item2 in lst:
            print(item_1,item2)

print(func_quad([1,2,3,4,5,6]))