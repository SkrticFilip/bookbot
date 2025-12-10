def get_num_words(path_to_file):
    num = 0
    with open(path_to_file) as f:
        file_contents = f.read()
        for word in file_contents.split():
            num += 1
        print(f"Found {num} total words")

def num_of_chars(path_to_file):
    num = {}
    with open(path_to_file)as f:
        file_contents = f.read()
        for word in file_contents:
            for char in word.lower():
                if char.isalpha():
                    num[char] = num.get(char, 0) + 1
    print(num)

def orderd(path_to_file):
    dic = {}
    with open(path_to_file) as f:
        file_contents = f.read()
        for word in file_contents:
            for char in word.lower():
                if char.isalpha():
                    dic[char] = dic.get(char, 0) + 1
    dic_sorted = sorted(dic.items(), key= lambda item: item[-1], reverse=True)
    for key, value in dic_sorted:
        if key == "e" or key == "t":
            print(f"{key}: {value}")
    #print(dic_sorted)