import sys
import pdb

from os import walk, remove
from pathlib import Path

from languages import langdict
from translate import Translator


if __name__ == "__main__":
    '''
    Program will translate contents from the textfile located at the
     provided location. The language to which the file is translated
     is determined by the provided language key. Language keys can
     be found at https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes
    '''

    _, *args = sys.argv

    try:

        # Verify arguments
        if len(args) < 2:
            raise ValueError("FileName and LanguageCode(s) are required")
        if not (lang_set := {*langdict.keys()}).issuperset(arg_set := {*args[1:]}):
            raise ValueError(f"LanguageCode(s) provided is not valid {[*arg_set.difference(lang_set)]}")


        # Get contents to be translated
        contents = ""
        with open(f'./files/in/{args[0]}', "r") as file:
            contents = file.read()

        output_file = Path(f'./files/out/temp.txt')
        output_file.parent.mkdir(exist_ok=True, parents=True)
        
        # Delete existing files in output directory
        iter = walk("./files/out/")
        dirpath, dirname, files = next(iter)
        for file in files:
            remove(f'{dirpath}/{file}')
                
        # Generate translated files
        newFiles = []
        for lang in args[1:]:
            tl = Translator(to_lang=lang)
            print(f"Translating into {langdict[lang].capitalize()}...")
            contents_t = tl.translate(contents)
            file_name = args[0].removesuffix(".txt")
            
            with open(full_path := f'./files/out/{file_name}_{lang}.txt', 'a') as file:
                file.write(contents_t)
                newFiles.append(full_path)

        print("done\n")

        print("Generated File(s):")
        for file in newFiles:
            print(f"  =>  {file}")

    except Exception as err:
        print(f"Could Not Translate: \n  {err}\n",)
        raise err