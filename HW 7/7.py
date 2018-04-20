#Прочитати вкладений текстовий файл, порахувати та вивести на екран:*
#       - кількість рядків
#       - кількість слів
#       - кількість унікальних слів
#       - кількість голосних та приголосних букв
#Зверніть увагу що в тексті є багато символів які потрібно відфільтрувати, щоб правильно порахувати кількості входжень. І числа також потрібно відфільтрувати*


try:
    with open('The_Everest_Story.txt') as file:
        count_rows = 0
        for line in file:
            line
            count_rows += 1
        print('Number of lines in the file: ', count_rows)  
except IOError:
    print("An IOError has occurred!")