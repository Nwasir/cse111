from asyncio import futures
from sentences import get_prepositional_phrase,  get_preposition
from sentences import get_determiner, get_noun, get_verb
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners
 
 
def test_get_noun():
    # 1. Test the single noun.

    single_noun = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(11):

        # Call the get_determiner function which
        # should return a single noun.
        word = get_noun(1)

        # Verify that the word returned from get_noun
        # is one of the words in the single_nounlist.
        assert word in single_noun

    # 2. Test the plural verb.

    plural_noun = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(11):

        # Call the get_determiner function which
        # should return a plural verb.
        word = get_noun(2)

        # Verify that the word returned from get_verb
        # is one of the words in the plural_verb list.
        assert word in plural_noun
        
def test_get_verb():
    # 1. Test the single verb.

    past_tense = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single verb.
        word = get_verb(1, "past")

        # Verify that the word returned from get_determiner
        # is one of the words in the single_verblist.
        assert word in past_tense

    # 2. Test the present tense.

    present_single = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single present verb.
        word = get_verb(1, "present")

        # Verify that the word returned from get_determiner
        # is one of the words in the single present verb  list.
        assert word in present_single

    # 3. Test the plural present tense.

    present_plural = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural present verb.
        word = get_verb(2, "present")

        # Verify that the word returned from get_determiner
        # is one of the words in the plural present verb  list.
        assert word in present_plural        

    # 4. Test the future tense.

    future_tense =  [ "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a future verb.
        word = get_verb(2, "future")

        # Verify that the word returned from get_determiner
        # is one of the words in the future verb  list.
        assert word in future_tense   

def test_get_preposition():
    preposition = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

         # This loop will repeat the statements inside it 4 times.
    for _ in range(4):  

         # Call the get_preposition function which
        # should return a preposition.
        word = get_preposition()  

         # Verify that the word returned from get_proposition
        # is one of the words in the prepsition list.
        assert word in preposition   

def test_get_prepositional_phrase():
    preposition =  ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    determiner = ["a", "one", "the"]

    noun = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]    

    for _ in range(4):
        word =  get_prepositional_phrase(1).split(' ')
                
        assert len(word) == 3
        assert (word[0] in preposition and word[1] in determiner and word[2] in noun)
        
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])        