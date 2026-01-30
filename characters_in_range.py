def ascii_border(start: str, end: str) -> list:
    list_of_characters = []

    for idx in range(ord(start) + 1, ord(end)):
        list_of_characters.append(chr(idx))
    return list_of_characters

start_idx = input()
end_idx = input()
result = ascii_border(start_idx, end_idx)

print(" ". join(result))