# from search_list_file import search_list

search_list = [
    2,
    3,
    6,
    10,
    11,
    14,
    15,
    18,
    25,
    30,
    31,
    34,
    38,
    40,
    42,
    43,
    44,
    45,
    47,
    54,
    59,
    61,
    65,
    66,
    71,
    73,
    76,
    77,
    81,
    88,
    92,
    93,
    95,
    96,
    97,
    103,
    104,
    105,
    106,
    107,
    108,
    110,
    112,
    114,
    117,
    120,
    122,
    130,
    131,
    132,
    133,
    134,
    135,
    137,
    138,
    142,
    143,
    146,
    148,
    149,
    152,
    155,
    156,
    160,
    163,
    164,
    165,
    166,
    168,
    171,
    173,
    174,
    177,
    179,
    180,
    183,
    185,
    190,
    192,
    198,
]


def binary_search(user_input, search_list):
    left_side, right_side = 0, len(search_list) - 1
    while left_side <= right_side:
        mid = (left_side + right_side) // 2
        if user_input == search_list[mid]:
            return f"{user_input} is in index '{mid}'."
        elif search_list[mid] < user_input:
            left_side = mid + 1
        else:
            right_side = mid - 1
    return "Not in the list"


try:
    user_input = int(input("Enter a number: "))
    result = binary_search(user_input, search_list)
    print(result)
except ValueError:
    print("Please enter a valid integer.")
