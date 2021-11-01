def find3Numbers(A, arr_size, search_num):
    for i in range(0, arr_size - 2):

        for j in range(i + 1, arr_size - 1):

            for k in range(j + 1, arr_size):
                if A[i] + A[j] + A[k] == search_num:
                    print("Triplet is", A[i],
                          ", ", A[j], ", ", A[k])
                    return True

    return 'False'


A = list(range(1, 1000))
search_num = 15
arr_size = len(A)
find3Numbers(A, arr_size, search_num)

