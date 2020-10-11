from py_thesaurus import Thesaurus

input_word = "dream"

new_instance = Thesaurus(input_word)

# Get the synonyms according to part of speech
# Default part of speech is noun

print(new_instance.get_synonym())

print(new_instance.get_synonym(pos='verb'))

print(new_instance.get_synonym(pos='adj'))

# Get the definitions

print(new_instance.get_definition())

# Get the antonyms

print(new_instance.get_antonym())