import time


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
    test_list = [x for x in range(500)]
    test_range = 50
    start_time_one = time.perf_counter()
    vander_output = vander_matrix_lists(test_list, test_range)
    for row in vander_output:
        print(row)
    end_time_one = time.perf_counter()

    start_time_two = time.perf_counter()
    vander_output = vander_matrix_loops(test_list, test_range)
    for row in vander_output:
        print(row)
    end_time_two = time.perf_counter()

    print(end_time_one - start_time_one)
    print(end_time_two - start_time_two)


if __name__ == '__main__':
    main()
