from itertools import combinations

# def dec_to_bin(n):
#     bin_list = []

#     while n > 0:
#         bin_list.append(n%2)
#         n = n // 2

#     return bin_list[::-1]

# def bin_to_dec(arr):
#     sum = 0
#     n_arr = arr[::-1]

#     for i in range(len(n_arr)):
#         sum += (n_arr[i] * (2**i))

#     return sum

# def bin_search(c_arr, k, p_arr=[]):
#     if c_arr[0] < k and c_arr[-1] > k:
#         p_arr = c_arr
#         mid = len(c_arr)//2

#         if c_arr[mid] < k:
#             return bin_search(c_arr[mid+1:], k, p_arr)
#         else:
#             return bin_search(c_arr[:mid], k, p_arr)

#     print(p_arr)

#     while p_arr[-1] > k:
#         p_arr.pop()

#     return p_arr[0]

def bitwise_and(n, k):
    # Generate a set S of all tuple combinations (a, b) in the range(1, n+1),       such that (a < b)
    l = [i for i in range(1, n+1)]
    S = list(combinations(l, 2))
    # S = set()
    # for i in range(1, n + 1):
    #     for j in range(1, n + 1):
    #         if i != j:
    #             if i < j:
    #                 S.add((i, j))
    #             else:
    #                 S.add((j, i))

    # For each tuple in S, determine the bitwise (a & b) and store in set S2
    S2 = set()

    for tup in S:
        # bin_compare = []
        # a_bin = dec_to_bin(tup[0])
        # b_bin = dec_to_bin(tup[1])
        # len_diff = abs(len(a_bin) - len(b_bin))

        # # Make the binary lists, same length
        # if len(a_bin) > len(b_bin):
        #     for i in range(len_diff):
        #         b_bin.insert(0, 0)
        #     # b_bin.extend([0 for i in range(len(a_bin) - len(b_bin))])
        # else:
        #     for i in range(len_diff):
        #         a_bin.insert(0, 0)
        #     # a_bin.extend([0 for i in range(len(b_bin) - len(a_bin))])

        # # Perform bitwise AND comparison
        # for i in range(len(a_bin)):
        #     if a_bin[i] == 1 and b_bin[i] == 1:
        #         bin_compare.append(1)
        #     else:
        #         bin_compare.append(0)

        # Convert resulting bitwise compare binary to decimal & save in L
        # S2.add(bin_to_dec(bin_compare))
        S2.add(tup[0]&tup[1])

    # Find and return the maximum value in L that is also less than k
    L = list(S2)
    L.sort()
    if k in L:
        return L[L.index(k) - 1]
    elif L[-1] < k:
        return L[-1]


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    print(bitwise_and(n, k))


from itertools import combinations

def bitwise_and(n, k):
    # Generate a list S of all tuple combinations (a, b) in the
    # range(1, n+1) such that (a < b)
    l = [i for i in range(1, n+1)]
    S = list(combinations(l, 2))

    # For each tuple in S, determine the bitwise (a & b) and store in set S2
    S2 = set()
    for tup in S:
        S2.add(tup[0]&tup[1])

    # Find and return the maximum value in L that is also less than k
    L = list(S2)
    L.sort()
    if k in L:
        print(L[L.index(k) - 1])
    elif L[-1] < k:
        print(L[-1])

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        bitwise_and(n, k)