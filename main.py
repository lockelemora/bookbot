def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    num_words = word_counter(file_contents)
    chars_dict = char_counter(file_contents)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)


    print("--- Begin report of books/frankenstein.txt ---")
    print("")
    print(f"{word_counter(file_contents)} words found in this document")
    print("")

    for item in chars_sorted_list:
        if item['char'].isalpha():
            print(f"The {item['char']} character was found {item['num']} times")
        else:
            continue
    
    print("--- End report ---")

def char_counter(text):
    lower_text = text.lower()
    char_dict = {}
    for char in lower_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def word_counter(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()