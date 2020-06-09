def palindrome(word):
    word_1=word.lower()                             #перевод в нижний регистр
    if word_1[::-1]==word_1:                        #[::-1] - перевернуть наоборот
        print("\"", word, "\" является палиндромом")
    else:
        print("\"", word, "\" не является палиндромом")
              
palindrome("saippuakivikauppias")                   #продавец мыла (фин.)
palindrome("кошка")
