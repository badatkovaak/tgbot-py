def format_dict(dictionary, level=0, tabs=1):
    res = '\n'+level*(' '*4*tabs) + '{\n'
    s = (level+1)*(' '*4*tabs)
    for k, v in dictionary.items():
        if isinstance(v, dict):
            res += f'{s}{k}: {format_dict(v,level=level+1)}'
        elif isinstance(v, list):
            res += f'{s}{k}: {format_list(v,level=level+1)}'
        else:
            res += f'{s}{k}: {str(v)},\n'
    res += level*(' '*4*tabs)+'},\n'
    return res


def format_list(array, level=0, tabs=1):
    res = '\n'+level*(' '*4*tabs) + '[\n'
    s = (level+1)*(' '*4*tabs)
    for i in range(len(array)):
        if isinstance(array[i], dict):
            res += f'{s}{i}: {format_dict(array[i],level=level+1)}'
        elif isinstance(array[i], list):
            res += f'{s}{i}: {format_list(array[i],level=level+1)}'
        else:
            res += f'{s}{i}: {str(array[i])},\n'
    res += level*(' '*4*tabs)+'],\n'
    return res


def formatted(obj, level=0, tabs=1):
    if isinstance(obj, list):
        return format_list(obj, level, tabs)
    if isinstance(obj, dict):
        return format_dict(obj, level, tabs)
    return str(obj)
