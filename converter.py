"""
переводим выдачу тритона в наш формат
1,3,S;4,3,U;7,1,U;11,2,?;15,2,S; --> 0,14,23,30
"""

#имена файла с текстом и файла с результатом
def NameCreation(file_name):
    txt_file = file_name + ".txt"
    poliakov_formatted_file = file_name +'.acc.txt.sstr'
    treeton_file  = file_name + ".txt.syll"
    treeton_formatted_file  = file_name + ".acc.txt.sstr2"
    return(txt_file, treeton_file, treeton_formatted_file)

#ф-ция вычитывает текст и отдает строку
def GiveMeText(txt_file):
    txt_file = open(txt_file, 'r', encoding = 'utf-8')
    text = txt_file.read()
    txt_file.close()
    return(text)

#ф-ция пишет в файл элементы списка
def ListToFile(txt_file, stressed_vowel_position):
    txt_file = open(txt_file, 'w', encoding = 'utf-8')
    txt_file.write(str(stressed_vowel_position).replace(" ","")[1:-1])
    txt_file.close()


#ф-ция делает список списков из разметки тритона
def TreetonToList(treeton_str):
    treeton_list = treeton_str.split(';')[:-1]
    treeton_tripples = []
    for tripple in treeton_list:
        tripple = tripple.split(',')
        tripple[0] = int(tripple[0])
        tripple[1] = int(tripple[1])
        treeton_tripples.append(tripple)
    return(treeton_tripples)

#ф-ция достает индекс гласной в ударном слоге в тексте
def FindingVowels(treeton_tripples, text):
# и в Тритоне, и у Полякова длина строки "\n" = 2. чтобы не съезжал индекс,
#делаем замену при обработке
    text = text.lower().replace("\n", "**")
    print('FindingVowels in :' + text)
    vowels = 'аеиоуэюяыё'
    stressed_vowel_position = []
    for tripple in treeton_tripples:
        if tripple[2] == 'S':
            index = tripple[0] - 1
            length = tripple[1]
            while length>0:
                if text[index] in vowels:
                    stressed_vowel_position.append(index)
                    #print('stressed vowel: ' + text[index] + str(index))
                    break
                else:
                    #print('unstressed vowel: ' + text[index]+ str(index))
                    length -= 1
                    index += 1
        #else: print ('this is unstressed tripple: ' +  str(tripple[0]))
    return(stressed_vowel_position)
def main ():
    file_name = input("file_name:\n")
    txt_file, treeton_file, treeton_formatted_file = NameCreation(file_name)
    text = GiveMeText(txt_file)
    treeton_tripples = TreetonToList(GiveMeText(treeton_file))
    stressed_positions = FindingVowels(treeton_tripples, text)
    ListToFile(treeton_formatted_file,stressed_positions)

if __name__ == '__main__':
    main()





















