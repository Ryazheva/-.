import math

def get_index_from_x(num, x):
    parameter = 0
    while math.pow(num, parameter) <= x:
        parameter += 1
    return parameter

def print_all_satisfying_nums(k_num, l_num, m_num, x):
    k_index = get_index_from_x(k_num, x)
    l_index = get_index_from_x(l_num, x)
    m_index = get_index_from_x(m_num, x)

    unique_nums = set()

    for k_idx in range(k_index):
        for l_idx in range(l_index):
            for m_idx in range(m_index):
                num = (int(math.pow(k_num, k_idx)) +
                        int(math.pow(l_num, l_idx)) +
                        int(math.pow(m_num, m_idx)))
                if num <= x:
                    unique_nums.add(num)

    for num in sorted(unique_nums):
        print(num, end=" ")

def main():
    x = int(input("Введите x: "))
    k_num = 3
    l_num = 5
    m_num = 7

    print_all_satisfying_nums(k_num, l_num, m_num, x)

if __name__ == "__main__":
    main()
