def switcher(arr=None):
    if arr:
        if all(isinstance(item, int) for item in arr):
            return arr[::-1]
        elif all(isinstance(item, str) for item in arr) and all(
            item.isalpha() for item in arr) and all(len(item) > 1 for item in arr):
            return [item.upper() for item in arr]

    return arr
