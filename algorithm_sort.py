from spellchecker import SpellChecker

spell = SpellChecker(language="en")

# Defines all the key words and to wchich route they belong to.
all_algorithms = {
    "/sorting/number_sort": {"sort", "number", "numbers", "sorting", "integers", "integer", "ints", "int", "decimals", "decimal", "floats", "float"},
    "/sorting/word_sort": {"sort", "word", "words", "sorting", "dictionary", "dictionaries", "alphabetical", "alphabet", "letters", "letter"},
    "/sorting/sentence_sort": {"alphabetical", "sort", "sorting", "sentences", "paragraph", "citation", "citing", "alphabet", "sentence", "letters", "letter"}
}

# Loads all the key words as valid words for the spell checking software.
for key, word_set in all_algorithms.items():
    spell.word_frequency.load_words(word_set);

def search_algorithms(key_words: list):
    # Corrects the grammar of the user inputed key words
    spell_checked_words = list()
    for word in key_words:
        spell_checked_words.append(spell.correction(word))

    # Creates a dictionary that has the route as the key, and the amount of matches as the item.
    ranking = dict()
    for key, word_set in all_algorithms.items():
        for user_word in spell_checked_words:
            if user_word in word_set:
                ranking[key] = ranking.get(key, 0) + 1;

    # Defines how many spaces in the ranking_list I will need.
    largest_match_rank = 0
    for key, rank in ranking.items():
        largest_match_rank = max(largest_match_rank, rank)

    # Creates a list where the higher the index the higher the ranking.
    ranking_list = list()
    for i in range(largest_match_rank + 1):
        ranking_list.append(list())

    for key, rank in ranking.items():
        ranking_list[rank].append(key)
        print(key, rank)

    return ranking_list
    
# print(search_algorithms(input(">").split()))