def replace_in_list(my_list, idx, element):
    if isinstance(idx, int) and idx > 0 and idx < len(my_list):
        my_list[idx] = element
        return my_list
    return my_list
