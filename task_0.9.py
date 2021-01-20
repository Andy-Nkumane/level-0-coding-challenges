def vowel_output(string):
    vowels = 'aeiou'
    result_list = [char for char in string if char.lower() in vowels]
    print(' '.join(result_list))