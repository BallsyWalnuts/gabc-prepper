from hyphenate import hyphenate_word


def prep_text(text_to_prep: str):
    """Prep a block of text for conversion into .gabc format.

    Details about .gabc can be found at http://gregorio-project.github.io/gabc/index.html
    """
    # Split the text into lines, but only take non-empty strings
    # This filters out empty lines
    orig_lines = [s for s in text_to_prep.split("\n") if s]
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
    return "\n".join(new_lines)


if __name__ == '__main__':
    import sys

    text = sys.stdin.read()
    print(prep_text(text))
