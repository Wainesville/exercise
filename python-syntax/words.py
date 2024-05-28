def print_upper_words(words):
    """Each word return as all caps, seperatly"""

    for word in words:
        print(word.upper())

def e_words(words):
    """returns only words that start with 'e' or 'E' """
    
    
    for word in words:
        if word.startswith('e') or word.startswith("E"):
            print(word.upper())

def must_start_with(words, must_start_with):
    """return each word uppercased if it begins with letter given
    """

    
    for word in words:
        for letter in must_start_with:
            if word.startwith(letter):
                print(word.upper(0))
                break
