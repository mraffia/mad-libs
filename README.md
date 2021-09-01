# Mad Libs
This is an implementation of the **Mad Libs** practice project from [Chapter 9 – Reading and Writing Files](https://automatetheboringstuff.com/2e/chapter9/) of the book [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) by Al Sweigart.

## Project Description
A Mad Libs program that reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file. For example, a text file (in this repo *panda.txt*) may look like this:

> The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.

The program would find these occurrences and prompt the user to replace them.

> Enter an adjective:
> **silly**
> Enter a noun:
> **chandelier**
> Enter a verb:
> **screamed**
> Enter a noun:
> **pickup truck**

The following text file would then be created:

> The silly panda walked to the chandelier and then screamed. A nearby pickup truck was unaffected by these events.

The results will be printed to the screen and saved to a new text file (*result.txt*).
