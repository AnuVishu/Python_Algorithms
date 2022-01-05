def sum1(n):
    """
    Take an input of n and return the sum of the numbers from 0 to n
    """
    final_sum = 0

    for num in range(0,n+1):  #Bigo(n)
        final_sum += num

    return final_sum




def sum2(n):
    """
    :param n: n numbers input
    :return: sum of n numbers from 0 to n
    """
    return (n*(n+1))//2  #Bigo(1),O(1)


print(sum1(1000))
print(sum2(1000))