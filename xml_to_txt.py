
#ф-ция вычитывает текст и отдает строку
def ReadFile(html_file):
    with open('html/' + html_file,'rb') as file:
        print('opening' + html_file)
        text = file.read()
        text = text.decode("cp1251")
        return(text)
    
#очищаем от тегов
def CleanText(text):
    import re
    list_of_speech = re.findall('<speach.*?>(.*?)</speach>', text)
    text = " ".join(list_of_speech)
    text = re.sub('(<(?P<tag>[a-z]+).*?(?P=tag)>)','', text)
    text = text.replace('&#769;', "'").replace("/", "")
    return(text)

def CleanTextFromAccent(text):
    text = text.replace("'", "")
    return(text)

def WritingFile(text, filename):
    h = open(filename + '.txt', 'w', encoding = 'utf-8')
    h.write(text)
    h.close()
#для каждого html создаем очищенный txt c ударениями и без
def main():
    import os
    files = os.listdir('C:/hse_compling/stress/mp_corpus_html_to_txt/html')
    for file in files:
        text = ReadFile(file)
        clean_text = CleanText(text)
        without_accent = CleanTextFromAccent(clean_text)
        WritingFile(clean_text, 'txt_acc/' + file + '.acc')
        WritingFile(without_accent, 'txt_unacc/' + file)
        
    
if __name__ == '__main__':
    main()
