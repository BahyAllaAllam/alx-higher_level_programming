def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if isinstance(idx, int) and idx > 0 and idx < len(new_list):
        new_list[idx] = element
        return new_list
    return my_list
