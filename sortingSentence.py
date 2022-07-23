def sortSentence(self, s):

    word_list = s.split()
    word = {}
    sorted_sen = ''

    for i in word_list:
        word[i[-1]]= i[:-1]
        
    for i in sorted(word):
        sorted_sen = sorted_sen+''.join(word[i]) + ' '
        
    sorted_sen = sorted_sen[:-1]
    
    return sorted_sen