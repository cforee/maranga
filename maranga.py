#!/usr/bin/python
import sys, itertools

words_file = "./words.txt"

# get a lookup-table of words
with open (words_file, "r") as fh:
  words = [ word.strip() for word in fh.readlines() ]


# find all permutations of entered characters,
# and for each permutation, match against words list;
# finally, return the list of matches
def permutate_and_search(original_word):
  matched_anagrams = []
  permutations = itertools.permutations(original_word)
  for permutation in permutations:
    permutation = ''.join(map(str,permutation)) # convert tuple to string
    if permutation in words:
      # we found a match!  add it to the list of anagrams
      matched_anagrams.append(permutation)
  return matched_anagrams


# get user input from command line
def get_input_from_user():
  return raw_input("\nenter a single word (no spaces):")


# let's do this!
print permutate_and_search(get_input_from_user())