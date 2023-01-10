def strange_function(n):

    if n % 2 == 0:

        return True


print(strange_function(2))

print(strange_function(1))


# otro
def list_sum(lst):

    s = 0

    for elem in lst:

        s += elem

    return s


print(list_sum([5, 4, 3]))
