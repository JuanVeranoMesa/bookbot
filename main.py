with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    
def word_count():
    total_words = len(file_contents.split())
    print(total_words)

def main():
    word_count()

if __name__ == "__main__":
    main()