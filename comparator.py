#имена файла с текстом и файла с результатом
def NameCreation(file_name):
    result_file = file_name + '.result.txt'
    poliakov_result = "pol_" + file_name +'.xml.acc.txt.sstr'
    treeton_result  = "treeton_" + file_name + ".xml.acc.txt.sstr2"
    corpora_result  = "corp_" + file_name + ".xml.acc.txt.sstr"
    return(result_file, poliakov_result, treeton_result, corpora_result)

def ResultAccToList(file_name):
    txt_file = open(file_name, 'r', encoding = 'utf-8')
    accent_str = txt_file.read()
    accent_list = list(map(int,accent_str.split(',')))
    txt_file.close()
    print(str(len(accent_list)))
    print(str(accent_list[:10]))
    return(accent_list)

def ComparingLists(corp_list, acc_list):
    corp_index = 0
    acc_index = 0
    TP = 0
    FP = 0
    FN = 0
    while corp_index  + 1 < len(corp_list) or acc_index  + 1 < len(acc_list):
        if corp_list[corp_index] == acc_list[acc_index]:
            #print(str(corp_list[corp_index])+ ' equals ' + str(acc_list[acc_index]))
            TP += 1
            if corp_index + 1 < len(corp_list): corp_index += 1
            if acc_index + 1 < len(acc_list): acc_index += 1
        elif corp_list[corp_index] < acc_list[acc_index]:
            #print(str(corp_list[corp_index])+ ' is lower then ' + str(acc_list[acc_index]))
            FN += 1
            if corp_index + 1 < len(corp_list): corp_index += 1
            else:   acc_index += 1
        else:
            #print(str(corp_list[corp_index])+ ' is bigger then ' + str(acc_list[acc_index]))
            FP += 1
            if acc_index + 1 < len(acc_list): acc_index += 1
            else:   corp_index += 1
        #print('TP: ' + str(TP) +' FN: ' + str(FN) + ' FP: ' + str(FP))
    return(TP,FN,FP)

def QualityMeasure(TP,FN,FP):
    #сколько выбранных релевантны
    precision = TP / (TP + FP)
    #сколько релевантных выбрано
    recall = TP / (FN + TP)
    f_measure = 2 * precision * recall / (precision + recall)
    return(precision, recall, f_measure)


def main():
    #берет название без префиксов и постфиксов
    file_name = input("file_name:\n")
    result_file, poliakov_result, treeton_result, corpora_result = NameCreation(file_name)
    poliakov_list = ResultAccToList(poliakov_result)
    treeton_list = ResultAccToList(treeton_result)
    corpora_list = ResultAccToList(corpora_result)
    p_TP,p_FN,p_FP = ComparingLists(corpora_list, poliakov_list)
    poliakov_result = QualityMeasure(p_TP,p_FN,p_FP)
    t_TP,t_FN,t_FP = ComparingLists(corpora_list, treeton_list)
    treeton_result = QualityMeasure(t_TP,t_FN,t_FP)
    print(poliakov_result)
    print(treeton_result)
    file = open( result_file, 'w', encoding = 'utf-8')
    file.write("Поляков:\n" + "\tprecision:\t\t"+(str(poliakov_result[0])) + "\n")
    file.write("\trecall:\t\t\t"+(str(poliakov_result[1])) + "\n")
    file.write("\tf_measure:\t\t"+(str(poliakov_result[2])) + "\n")
    file.write("\taccent_count:\t"+str(len(poliakov_list)) + "\n")
    file.write("Тритон:\n" + "\tprecision:\t\t"+(str(treeton_result[0])) + "\n")
    file.write("\trecall:\t\t\t"+(str(treeton_result[1])) + "\n")
    file.write("\tf_measure:\t\t"+(str(treeton_result[2])) + "\n")
    file.write("\taccent_count:\t"+str(len(treeton_list)) + "\n")
    file.write("Корпус:\n\taccent_count:\t" +  str(len(corpora_list)) + '\n')

    file.close()
    
    
if __name__ == '__main__':
    main()
