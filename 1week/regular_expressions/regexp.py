def calculate(data, findall):
    matches = findall(r"([abc])([+-]?=)([abc])?([+-]?\d+)?")  
    for v1, s, v2, n in matches:
        if '-' in s:
            data[v1] -= data.get(v2, 0) + int(n or 0)
        elif '+' in s:
            data[v1] += data.get(v2, 0) + int(n or 0)
        else:
            data[v1] = data.get(v2, 0) + int(n or 0)

    return data