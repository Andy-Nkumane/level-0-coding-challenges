def common_characters(string1, string2):
    common = [char for char in string1 if char in string2]
    print(f'Common letters: {", ".join(common)}')

common_characters('house','computers')