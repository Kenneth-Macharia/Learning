def pig_latin_converter(word):
    VOWELS = 'aeiou'
    CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

    clean_word = word.lower().strip()

    if clean_word != '' and word[0] in VOWELS or word[0] in CONSONANTS:
        if word[0] in VOWELS:
            return f'{word}way'
        else:
            index = 0
            for i in range(len(word)):
                if word[i] in VOWELS:
                    index = i
                    break

            return f'{word[index:]}{word[:index]}ay'

    return ''