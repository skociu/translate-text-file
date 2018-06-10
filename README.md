# Requirements

<code>
 pip install googletrans
</code>

For more information go to: https://pypi.org/project/googletrans/

# About
The script will translate the text file from one language to the next language.
Example of command to run the script: 
<code>
python TranslateText.py fr en
</code>

The "fr en" means to translate a French text into English.
For more information on googletrans go to: http://py-googletrans.readthedocs.io/en/latest/

Note: type print(googletrans.LANGUAGES) to see supported languages
Example of language codes: 'fr' = French; 'sq' = Albanian; 'en' = English

# Translation Text

The translation text is a small extract from the The Project Gutenberg EBook of Meditations, by Marcus Aurelius. The text can be translated from English to Albanian using the command below:

<code>
python TranslateText.py en sq
</code>

Link to the Gutenberg text:
http://www.gutenberg.org/cache/epub/2680/pg2680.txt
