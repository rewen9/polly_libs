
def lists_wrapper(lst, rng_each_list):
    """ 
        Wrapper for lists 
        lst is the list original
        rng_each_list is the number of items in each list
    """
    lists = []
    wrapper_list = []
    for item in lst:
        wrapper_list.append(item)
        
        if len(wrapper_list) >= rng_each_list:
            lists.append(wrapper_list.copy())
            wrapper_list = []
    if wrapper_list:
        lists.append(wrapper_list.copy())