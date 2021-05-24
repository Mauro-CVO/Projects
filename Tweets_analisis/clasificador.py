import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

excluded_words = ['el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 
                'al', 'del', 'lo', 'le', 'y', 'e', 'o', 'u', 'de', 'a', 
                'en', 'que', 'es', 'por', 'para', 'con', 'se', 'su', 'les', 
                'me', 'q', 'te', 'pero', 'mi', 'ya', 'cuando', 'como', 'estoy',
                'voy', 'porque', 'he', 'son', 'solo', 'tengo', 'muy'
                ]

def count_words(arr):
    lst = [arr[i][0] for i in range(len(arr))]
    total = np.sum(np.array(lst))
    return total

def run():
    top_words = {}
    tweets = open('./tweets.txt', encoding='utf-8')
    for line in tweets:
        words = line.strip().lower().split()
        for word in words:
            if word not in excluded_words:
                top_words[word] = top_words.get(word,0) + 1
    most_used_words = sorted(top_words, key=top_words.get, reverse=True)

    # count_u = 0
    # for word in most_used_words:
    #     if count_u < 10 and word.startswith('@'):
    #         print(top_words[word], word)
    #         count_u += 1
    #         print('*'*40)
    

    # count = 0
    venta = []
    compra = []
    for word in most_used_words:
        if 'vend' in word:
            venta.append([top_words[word], word])
        elif 'compr' in word:
            compra.append([top_words[word], word])
        #print('*'*40)

    # print('venta:', venta)
    # print('compra:', compra)
    total_venta = count_words(venta)
    total_compra = count_words(compra)
    print(total_venta)
    print(total_compra)


if __name__ == '__main__':
    run()