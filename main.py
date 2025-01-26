with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    
def word_count():
    total_words = len(file_contents.split())
    print(total_words)
    
def character_count():
    lower_case_book = file_contents.lower()
    characters = list(lower_case_book)
    char_count = {}
    
    for char in characters:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for char, count in char_count.items():
        print(f"'{char}': {count}")

def main():
    
    #print(file_contents) saved bc its annoying to see printed each time
    
    # word_count() temporarily not running this
    
    character_count()
    

if __name__ == "__main__":
    main()