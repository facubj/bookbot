def count_words(raw_text):
   return len(raw_text.split())

def count_characters(text):
    lowered_text = text.lower()
    characters = {}
    for character in lowered_text:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1

    return characters

def print_report(text):
    char_count = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    char_list = []
    for char, count in char_count.items():
        char_list.append({"char": char, "num": count})
    
    def sort_on(entry):
        return entry["num"]

    char_list.sort(key=sort_on, reverse=True)

    print("--- Begin report ---")
    print(f"{sum(char_count.values())} words found in the document\n")
    for entry in char_list:
        print(f"The '{entry['char']}' character was found {entry['num']} times")
    print("--- End report ---")

def main():
    with open("books/frankenstein.txt") as f:
        frankenstein_txt = f.read()
        word_count = count_words(frankenstein_txt)
        print(f"The book has {word_count} words")
        character_count = count_characters(frankenstein_txt)
        print(f"These are the characters {character_count}")
        print_report(frankenstein_txt)

if __name__ == "__main__":
    main()