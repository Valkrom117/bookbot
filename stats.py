def count_words(contents):
    words = contents.split()
    return len(words)


def charcter_count(contents):
    contents = contents.lower()
    characters = {}
    for char in contents:
        if not char.isalnum():
            continue
        if char in characters :
            characters[char] += 1
        else:
            characters[char] = 1
    
    return characters


def sort_on(items):
    return items["num"]

def sort_stats(character_stats):
    character_list = []
    character_list= [{"char":char,"num": character_stats[char]} for char in character_stats]
    character_list.sort(reverse=True, key=sort_on)
    return character_list
