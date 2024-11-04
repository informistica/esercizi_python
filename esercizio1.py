#esercizio1.py 8 ottobre 2014
s=input("inserisci una stringa lunga almeno tre caratteri: ")
if len(s)>2:
    print(s[1:len(s)-1]) #oppure print(s[1:-1]) solo in python
else:
    print("la stringa è troppo corta")
          
