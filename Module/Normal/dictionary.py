from nltk.corpus import wordnet

def get_definitions_en2en(word):
    synsets = wordnet.synsets(word)
    if not synsets:
        return None
    definitions = [syn.definition() for syn in synsets]
    return definitions