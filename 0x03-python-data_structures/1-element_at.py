def element_at(my_list, idx):
    if isinstance(idx, int) and idx < len(my_list):
        return my_list[idx]
    return None

