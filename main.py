def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for i in text:
        lowered = i.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def sort_on(d):
    return d["num"]
        
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for x in num_chars_dict:
        sorted_list.append({"char": x, "num": num_chars_dict[x]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list 
          
main()