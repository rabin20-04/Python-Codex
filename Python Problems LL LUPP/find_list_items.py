def find_list(search_list, search_item):
    index_list = []
    for index, values in enumerate(search_list):
        if values == search_item:
            index_list.append([index])
        elif isinstance(search_list[index], list):
            for i in find_list(search_list[index], search_item):
                index_list.append([index] + i)
    return index_list


listss = [
    ["apple", "samsung", "lenovo"],
    ["dell", "apple", "samsung", "lenovo"],
    "apple",
    ["apple", "acer"],
]
print(find_list(listss, "apple"))
