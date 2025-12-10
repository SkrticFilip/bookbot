from stats import get_num_words
from stats import num_of_chars
from stats import orderd
import sys

def get_book_text(path_to_file):
    num = 0
    with open(path_to_file) as f:
        file_contents = f.read()
        for word in file_contents.split():
            num += 1
        print(f"Found {num} total words")

def main():
    
    #get_num_words(sys.argv[1])

    #get_book_text(sys.argv[1])

    #num_of_chars(sys.argv[1])

    #print("============ BOOKBOT ============")
    #print(f"Analyzing book found at {sys.argv[1]}")
    #print("----------- Word Count ----------")
    #get_num_words(sys.argv[1])
    #print("--------- Character Count -------")
    
    #print("============= END ===============")

    #books/frankenstein.txt
    
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        return{sys.exit(1)} 
    orderd(sys.argv[1])

main()
