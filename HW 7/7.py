#Прочитати вкладений текстовий файл, порахувати та вивести на екран:*
#       - кількість рядків
#       - кількість слів
#       - кількість унікальних слів
#       - кількість голосних та приголосних букв
#Зверніть увагу що в тексті є багато символів які потрібно відфільтрувати, щоб правильно порахувати кількості входжень. І числа також потрібно відфільтрувати*



punctuation = ['.', ',', ':', ';', '!', '?', '(', ')']
try:
    with open('The_Everest_Story.txt') as file:
        count_rows = 0
        sstr = ''
        for line in file:
            sstr += line
            count_rows += 1
        print('Number of lines in the file: ', count_rows)  
except IOError:
    print('An IOError has occurred!')
    
wordList = sstr.split()
i = 0
for word in wordList:
    if word[-1] in punctuation:
        wordList[i] = word[:-1]
        word = wordList[i]
    if word[0] in punctuation:
        wordList[i] = word[1:]
    i += 1
    
count_words = 0    
i = 0
while i < len(wordList):
    i += 1
    count_words += 1

print('Number of words in the file: ', count_words)        


























