def no_c(my_string):
    for i in my_string:
        new_string = "".join(i for i in my_string if i not in 'cC')
    return new_string
