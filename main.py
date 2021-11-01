def find3Numbers(A, arr_size, search_num):
    # Виправити перший елемент як A[i]F
    for i in range(0, arr_size - 2):

        # Виправте другий елемент як A[j]
        for j in range(i + 1, arr_size - 1):

            # Тепер шукайте третє число
            for k in range(j + 1, arr_size):
                if A[i] + A[j] + A[k] == search_num:
                    print("Triplet is", A[i],
                          ", ", A[j], ", ", A[k])
                    return True

    # Якщо ми доберемося сюди, то ні
    # була знайдена трійня
    return 'False'


# Driver program to test above function
A = list(range(1, 1000))
search_num = 15
arr_size = len(A)
find3Numbers(A, arr_size, search_num)

