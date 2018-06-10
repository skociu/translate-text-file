import os
import argparse
from googletrans import Translator

def remove_old_translated():
    mypath =  os.path.dirname(os.path.abspath(__file__))
    for f in os.listdir(mypath):
        if f.startswith("translated"):
            os.remove(f)
            
def remove_old_temps():
    mypath =  os.path.dirname(os.path.abspath(__file__))
    for f in os.listdir(mypath):
        if f.startswith("temp"):
            os.remove(f)

class Translation:
    '''The script will translate the text file from one language to the next language.
    Example of command to run the script: python TranslateText.py fr sq
    The "fr en" means to translate a French text into Albanian.
    For more information on googletrans go to: http://py-googletrans.readthedocs.io/en/latest/
    Note: type print(googletrans.LANGUAGES) to see supported languages
    Example of language codes: 'fr' = French; 'sq' = Albanian; 'en' = English
    '''
    def __init__(self, *a):
        self.from_language = args.from_language
        self.to_language = args.to_language
        self.extract_file = extract_file
        self.translate_file = translate_file
        self.transformed_file = transformed_file
        with open(self.extract_file, 'a') as f:
            f.write('\n')
	    

    def clean_text(self):
        text = open(self.extract_file, 'r').read()
        text = text.replace('\n', '\n ')
        text = text.replace('\n', '')
        text = text.replace('.', '.\n')
        text = text.replace('!', '!\n')
        text = text.replace('?', '?\n')
        f = open(self.transformed_file, 'w')
        f.write(text)
        
    def translate_text(self, text):
        #for more information on googletrans
        #http://py-googletrans.readthedocs.io/en/latest/
        #Note: type print(googletrans.LANGUAGES) to see supported languages
        # i.e. 'fr' = French; 'sq' = Albanian; 'en' = English
        translator = Translator()
        from_language = self.from_language
        to_language = self.to_language
        translation = translator.translate(text, 
            src=from_language, dest=to_language).text.encode("utf-8")
        return translation


    def write_translation(self):
        f1 = open(self.transformed_file, 'r')
        with open(self.translate_file, 'w') as f:
            for i, line in enumerate(f1, 1):
                f.write(str(i) + ') ' + str(line.strip()) + '\n')
                f.write(str(i) + ') ' + str(self.translate_text(line.strip()))+ '\n\n')
        f.close()

    
if __name__ == "__main__":
    remove_old_translated()
    mypath =  os.path.dirname(os.path.abspath(__file__))
    for f in os.listdir(mypath):
        if f.endswith(".txt"):
            argparser = argparse.ArgumentParser()
            argparser.add_argument('from_language',help = 'Example of command to run: python TranslateText.py fr en')
            argparser.add_argument('to_language',help = 'Example of command to run: python TranslateText.py fr en')
            args = argparser.parse_args()
            extract_file = "{}.txt".format(os.path.splitext(f)[0])
            transformed_file = "temp_{}.txt".format(os.path.splitext(f)[0])
            translate_file = "translated_{}_{}_{}.txt".format(args.from_language, 
                args.to_language, os.path.splitext(f)[0])
            t=Translation()
            t.clean_text()
            t.write_translation()
            remove_old_temps()
            print('translation complete - check text file that starts with translated')


