def get_longest_string(input_strs: list[str]) -> str:
    if not input_strs:
        return ""

    return max(input_strs, key=len)


print(get_longest_string(["cat", "dog", "bird", "lizard"]))
print(get_longest_string(["cat", "dog", "bird", "wolf"]))
print(get_longest_string(["a", "b", "c", "d"]))
