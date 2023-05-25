# Problem Seti 2, adamAsmaca.py
# Ä°sim:  Şule Aktaş 193405004
# Ortak Ã§alÄ±Åanlar: İrem Nur Kızılca 203405043
# Harcanan zaman:

# Adam Asmaca Oyunu
#------------------------------------
# YardÄ±mcÄ± kod
# Bu yardÄ±mcÄ± kodu anlamanÄ±za gerek yok,
# ama fonksiyonlarÄ± nasÄ±l kullanacaÄÄ±nÄ± bilmeniz gerekecek
# (dÃ¶kÃ¼manlarÄ± okuduÄunuzdan emin olun!)
import random
import string

WORDLIST_FILENAME = "kelimeler.txt"


def load_words():
    """
    GeÃ§erli kelimelerin bir listesini dÃ¶ndÃ¼rÃ¼r.
    Kelimeler kÃ¼Ã§Ã¼k harf dizileridir.
    
     Kelime listesinin boyutuna baÄlÄ± olarak,
     bu fonksiyonun tamamlanmasÄ± biraz zaman alabilir.
    """
    print("Dosyadan kelime listesi yÃ¼kleniyor...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "kelimeler yÃ¼klendi.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): kelime listesi(strings)
    
    Kelime listesinden rastgele bir kelime dÃ¶ndÃ¼rÃ¼r
    """
    return random.choice(wordlist)

# yardÄ±mcÄ± kodun sonu

#------------------------------------

# Programdaki herhangi bir yerden eriÅilebilmesi iÃ§in
# kelime listesini deÄiÅken kelime listesine yÃ¼kleyin
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    print("'",secret_word,"'")
    harfler2 = list(letters_guessed)
    harfler =  list(secret_word)    
    print(harfler2)
    a = []
    i = 0
    for eleman in harfler:   
        if eleman in harfler2: 
            a.insert(i, eleman)
            i+=1

    if len(a) == len(harfler):
        return True
    else:
        return False



def get_guessed_word(secret_word, letters_guessed):
    harfler =  list(secret_word)
    yenilist = []
    b = 0
    for eleman in harfler:   
        if eleman in letters_guessed: 
            yenilist.insert(b,eleman)      
    a = []
    i = 0
    while i < len(harfler):
        
        if harfler[i] in yenilist:
            a.insert(i, harfler[i])  
        else:
            a.insert(i,'_ ')
        i+=1
        

    str1 = ""
    for ele in a:
        str1+=ele
    return str1



def get_available_letters(letters_guessed):
    alfabe = list(string.ascii_lowercase)
    z=[]
    i=0
    for eleman in alfabe:
        if eleman in letters_guessed:
            pass
        else:
            z.insert(i, eleman)
            i+=1   
    str1 = ""
    for ele in z:
        str1+=ele
    return str1
    
    

def adamAsmaca(secret_word):
    print("Adam Asmaca oyununa hoş geldiniz!")
    print(len(secret_word) , "harf uzunluğunda bir kelime düşünüyorum.") 
    Kul_harfler=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    guesses_remaining=6
    print(guesses_remaining, "tahmininiz kaldı.\nKullanılabilir harfler:", get_available_letters(""))
    word=[]
    k=""
    warnings_remaining=3
    symbol="0123456789@#$%&^-_+=<>?/,.\|[]{}!~`()"
    vowels="aeuio"

    x = []
    while guesses_remaining>-1:

       print("--------------------------------------") 
       print(warnings_remaining, "uyarınız kaldı.")   
      
       letter_guessed= str.lower(input("\nLütfen bir harf tahmin edin:")) 
       x.append(letter_guessed)
    
       print(guesses_remaining, "tahmininiz kaldı.\nKullanılabilir harfler:", get_available_letters(x))
           
       word.append(letter_guessed)

       if letter_guessed in symbol:
              if warnings_remaining == 0:
                  print("Hiçbir uyarınız kalmadığından bir tahmininizi kaybedersiniz:")
                  guesses_remaining -=1
                
                  if guesses_remaining == 0:
                      print("--------------------------------------") 
                      print("Üzgünüm, tahminleriniz tükendi. Kelime başkaydı.KAYBETTINIZ!")
                      print("Kelime: ", secret_word)
                      break
                  continue 
              warnings_remaining -=1
              print("Hata! Bu geçerli bir harf değil.",warnings_remaining," uyarınız kaldı" )

       elif letter_guessed in secret_word:
              print("İyi tahmin: ", get_guessed_word(secret_word,x ) , "\n")
              if secret_word == get_guessed_word(secret_word,x ):
                      print("Tebrikler Kazandın!")
                      break
              elif letter_guessed in Kul_harfler:
                 Kul_harfler.remove(letter_guessed)  
              elif letter_guessed != Kul_harfler:
                  print("Hata! Bu harfi zaten tahmin ettin.")
                  if warnings_remaining == 0:
                      print("Hiçbir uyarınız kalmadığından bir tahmininizi kaybedersiniz:")
                      guesses_remaining -=1
                      
                      if guesses_remaining == 0:
                         print("\n--------------------------------------") 
                         print("Üzgünüm, tahminleriniz tükendi. Kelime başkaydı.KAYBETTINIZ!")
                         print("Kelime: ", secret_word)
                         break
                      continue
                  warnings_remaining -=1
                  print("Hata! Bu geçerli bir harf değil.",warnings_remaining," uyarınız kaldı" )
       else:  
              print("Hata! O harf bu kelimede yok:",get_guessed_word(secret_word,x ) , "\n")
              if letter_guessed in Kul_harfler:
                 Kul_harfler.remove(letter_guessed) 
              elif letter_guessed != Kul_harfler:
                  print("Hata! Bu harfi zaten tahmin ettin.")
                  if warnings_remaining == 0:
                      print("Hiçbir uyarınız kalmadığından bir tahmininizi kaybedersiniz:")
                      guesses_remaining -=1
     
                      if guesses_remaining == 0:
                         print("--------------------------------------") 
                         print("Üzgünüm, tahminleriniz tükendi. Kelime başkaydı.KAYBETTINIZ!")
                         print("Kelime: ", secret_word)
                         break
                      continue
                  warnings_remaining -=1
              elif letter_guessed in vowels:
                 guesses_remaining -=2
              else:
                 guesses_remaining -=1



# Adam asmaca iÅlevinizi tamamladÄ±ÄÄ±nÄ±zda, dosyanÄ±n
#en altÄ±na gidin ve test edilecek ilk iki satÄ±rÄ±n yorumunu kaldÄ±rÄ±n
# (ipucu: kendi testinizi yaparken kendi secret_word'Ã¼nÃ¼zÃ¼
# seÃ§mek isteyebilirsiniz)

# -----------------------------------






if __name__ == "__main__":
    # pass

    # 2. bÃ¶lÃ¼mÃ¼ test etmek iÃ§in yukarÄ±daki pass satÄ±rÄ±nda # iÅaretini kullanÄ±n ve aÅaÄÄ±daki iki satÄ±rda # iÅaretini silin
    
    secret_word = choose_word(wordlist)
    adamAsmaca(secret_word)

###############
    
# 3. bÃ¶lÃ¼mÃ¼ test etmek iÃ§in yukarÄ±daki satÄ±rlarlarda yeniden # iÅaretini kullanÄ±n ve aÅaÄÄ±daki iki satÄ±rda # iÅaretini silin

    #secret_word = choose_word(wordlist)
    #adamAsmaca_ipuclu(secret_word)
