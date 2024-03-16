def vander_matrix(input_list: list[int], input_range: int) -> list:
    vander = [[list_item ** x for x in range(input_range)][::-1] for list_item in input_list]
    return vander


vander_matrix = vander_matrix([1, 2, 3, 4], 7)
for row in vander_matrix:
    print(row)
