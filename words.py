def print_upper_words(words):
    """Print each word on a seperate line, but in all uppercase"""

    for word in words:
        print(word.upper()) 

print_upper_words(["easy", "home", "quick", "Elephant", "run"])
#Should print: EASY, HOME, QUICK, ELEPHANT, RUN

def print_upper_e_words(words):
    """Only print words that start with letter 'e' as Capital"""

    for word in words: 
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())

print_upper_e_words(["easy", "home", "quick", "Elephant", "run"])
#Should print: EASY, ELEPHANT

def print_upper(words, letter):
    for word in words:
        if word.startswith(letter):
            print(word.upper())

print_upper(["alpha", "john", "hello", "pick"], "a")
#Should print: ALPHA