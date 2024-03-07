from translate import Translator
from languages import langdict


def getTranslator():
    while True:
        print("Please select a language:")
        langlist = [*langdict.items()]

        for i, lang in enumerate(langlist):
            print(f'{i + 1}) {lang[1].capitalize()}')

        try:
            langInd = int(input("> "))
            if 1 <= langInd <= len(langlist):
                langKey = langlist[langInd - 1][0]
                return Translator(to_lang=langKey),langlist[langInd - 1][1]
            raise Exception
        except:
            print("Not Valid. Try Again.")
            continue


if __name__ == ("__main__"):
    print("\nHello! I will be your translator.\n")

    while True:        
        tl,lang = getTranslator();
        
        print(f"\n[{lang.upper()}]: What would you like me to say? (Type '[QUIT]' anytime)\n")
        while True:
            phrase = input("> ")
            
            if phrase == "[QUIT]":
                print()
                break;
            
            phrase_t = tl.translate(phrase)
            print(phrase_t + "\n")