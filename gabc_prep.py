import sys

from hyphenate import hyphenate_word

text = sys.stdin.read()

# Split the text into lines, but only take non-empty strings
# This filters out empty lines
orig_lines = [s for s in text.split("\n") if s]
new_lines = []

for line in orig_lines:
    # Split each line into constituent words
    words = line.split(" ")

    # Split each word into syllables, at least the best approximation
    # using the Frank Liang algorithm for TeX.
    #
    # Each "syllable" is then joined with (), which is a placeholder
    # for the chant pointing notation used by Gregorio. Then, since
    # even words that have one syllable need the placeholder, a () is
    # appended to the end of the new word.
    new_words = ["()".join(hyphenate_word(word))+"()" for word in words]

    # Connect all the words with spaces again
    new_lines.append(" ".join(new_words))

# Join all the prepped lines with newline chars and print
print("\n".join(new_lines))
