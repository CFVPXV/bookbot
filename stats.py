def word_count(bookdata):
    return len(bookdata.split())

def char_count(bookdata):
    char_counts = {}

    for char in bookdata:
        if char.lower() not in char_counts:
            char_counts[char.lower()] = 1
        else:
            char_counts[char.lower()] += 1
    
    return char_counts

def keyVal(e):
    return e["num"]

def sort_char_count(char_dict):
    char_sort = []

    for i in char_dict:
        char_sort.append({"char": i, "num": char_dict[i]})
    
    char_sort.sort(key=keyVal, reverse=True)

    return char_sort

