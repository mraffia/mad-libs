#! python3
# madLibs.py - Reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

def madLibs(fileNameAndSuffix):
    oriFile = open(fileNameAndSuffix)
    content = oriFile.read()
    oriFile.close()

    exists = []

    if 'ADJECTIVE' in content:
        exists.append('ADJECTIVE')
    if 'NOUN' in content:
        exists.append('NOUN')
    if 'ADVERB' in content:
        exists.append('ADVERB')
    if 'VERB' in content:
        exists.append('VERB')

    replacements = {}

    for i in range(len(exists)):
        rep = input('Enter a/an ' + exists[i].lower() + ':\n')
        replacements[exists[i]] = rep

    for word, rep in replacements.items():
        content = content.replace(word, rep)

    finalFile = open('result.txt', 'w')
    finalFile.write(content)
    finalFile.close()

    print(content)

    return content
