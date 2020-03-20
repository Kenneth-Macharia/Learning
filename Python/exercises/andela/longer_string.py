def longer_str_compare(str1, str2):
    result = []

    if isinstance(str1, str) and isinstance(str2, str):
        if len(str1) > len(str2):
            result.append(str1)
        elif len(str1) < len(str2):
            result.append(str2)
        elif len(str1) == len(str2):
            result.append(str1)
            result.append(str2)
    else:
        result.append('')

    return result
