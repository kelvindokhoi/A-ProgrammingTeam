# 12250 - Language Detection

i=0
languages={"HELLO":"ENGLISH","HOLA":"SPANISH","HALLO":"GERMAN","BONJOUR":"FRENCH","CIAO":"ITALIAN","ZDRAVSTVUJTE":"RUSSIAN"}
while (n:=input())!="#":
    i+=1
    try:
        print(f"Case {i}:",languages[n])
    except KeyError:
        print(f"Case {i}:","UNKNOWN")