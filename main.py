with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    
def word_count():
    total_words = len(file_contents.split())
    
    return total_words
    
def character_count():
    lower_case_book = file_contents.lower()
    characters = list(lower_case_book)
    char_count = {}
    
    for char in characters:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    for char, count in char_count.items():
        print(f"The letter '{char}' was found in this text {count} time(s)")

def main():
    
    #print(file_contents) saved bc its annoying to see printed each time
    print("Welcome to this report on frankenstein.txt.\n")
    
    print(f"There are a total of {word_count()} words in this book.\n")
    
    character_count()
    

if __name__ == "__main__":
    main()