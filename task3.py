import math


# 1.print_pairs
def print_pairs(text):
    l = [text[i:i + 2] for i in range(len(text) - 1)]
    print(*l, ' ')


# 2.is_prime
def is_prime(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


# 3.interleave_lists
def interleave_lists(l1, l2):
    short_list_length = min(len(l1), len(l2))
    inter_list = []
    for i in range(short_list_length):
        inter_list.append(l1[i])
        inter_list.append(l2[i])
    longer_list = l1 if len(l1) > len(l2) else l2
    return inter_list + longer_list[short_list_length::]


# 4.log10_list_comprehension
def log10_list_comprehension(l):
    if not l:
        return []
    return [math.log10(i) for i in l]


# 5.log10_inplace
def log10_inplace(l):
    for i in range(len(l)):
        l[i] = math.log10(l[i])


# 6.get_highest_average_column
def get_highest_average_column(mat):
    sum_array = []
    for row in mat:
        for i, item in enumerate(row):
            if len(sum_array) == i:
                sum_array.append(item)
            else:
                sum_array[i] += item
    max_number = sum_array[0]
    max_index = 1
    for i, number in enumerate(sum_array):
        if number >= max_number:
            max_number = number
            max_index = i + 1
    print(max_index)


# Challenge
def get_longest_increasing_subsequence_length(mat):
    subsequence_length = []
    for row in mat:
        print(subsequence_length)
        subsequence = 1
        for i, item in enumerate(row):
            if i > 0 and row[i - 1] < item:
                subsequence += 1
            else:
                subsequence_length.append(subsequence)
                subsequence = 1
        subsequence_length.append(subsequence)
    print(max(subsequence_length))
    print(subsequence_length)
    return max(subsequence_length)

