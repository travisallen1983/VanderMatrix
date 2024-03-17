def vander_matrix_lists(input_list: list[int], input_range: int) -> list[list]:
    output_list = [[list_item ** x for x in range(input_range)][::-1] for list_item in input_list]
    return output_list


def vander_matrix_loops(input_list: list[int], input_range: int) -> list[list]:
    output_list = []
    for list_item in input_list:
        _list = []
        for i in range(input_range - 1, -1, -1):
            _list.append(list_item ** i)
        output_list.append(_list)
    return output_list


def main():
    vander_output = vander_matrix_lists([1, 2, 3, 4], 7)
    for row in vander_output:
        print(row)

    vander_output = vander_matrix_loops([1, 2, 3, 4], 7)
    for row in vander_output:
        print(row)


if __name__ == '__main__':
    main()
