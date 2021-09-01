#! python3
# madLibs.py - Reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

def madLibs(fileNameAndSuffix):
    oriFile = open(fileNameAndSuffix)
    content = oriFile.read()
    oriFile.close()

    contentList = content.split(' ')
    exists = []
    for i in range(len(contentList)):
        if 'ADJECTIVE' in contentList[i]:
            exists.append('ADJECTIVE')
        elif 'NOUN' in contentList[i]:
            exists.append('NOUN')
        elif 'ADVERB' in contentList[i]:
            exists.append('ADVERB')
        elif 'VERB' in contentList[i]:
            exists.append('VERB')

    replacements = []
    for i in range(len(exists)):
        if exists[i] == 'ADJECTIVE' or exists[i] == 'ADVERB':
            rep = input('Enter an ' + exists[i].lower() + ':\n')
            replacements.append(rep)
        else:
            rep = input('Enter a ' + exists[i].lower() + ':\n')
            replacements.append(rep)

    for i in range(len(replacements)):
        content = content.replace(exists[i], replacements[i], 1)

    finalFile = open('result.txt', 'w')
    finalFile.write(content)
    finalFile.close()

    print(content)

    return content
