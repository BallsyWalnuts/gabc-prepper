# gabc-prepper
Script to prep blocks of English tex for conversion into .gabc files

## Impetus
This script was created to make creation of .gabc files for the use by [The Gregorio Project](http://gregorio-project.github.io/index.html)
as simple as possible. For Gregorio to work, each syllable of the word needs to be pointed with the proper neum. However,
manually splitting words into syllables is tedious in the extreme, so this script was created to take out much of that 
work.

## How does it work?
It uses the [hyphenate python library](https://github.com/jfinkels/hyphenate) to implement an [algorithm devised by Frank
Liang](https://tug.org/docs/liang/) to hyphenate words for TeX ages ago. It is not a perfect algorithm, but it gets close 
enough for government work.

## Usage
```shell
$ echo "some text to split on syllables" | python gabc_prep.py
some() text() to() split() on() syl()la()bles()

$ echo "some text to split on syllables
across multiple lines" | python .\gabc_prep.py
some() text() to() split() on() syl()la()bles()
across() mul()ti()ple() lines()
```