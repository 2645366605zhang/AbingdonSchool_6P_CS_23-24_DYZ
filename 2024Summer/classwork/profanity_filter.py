from re import sub, IGNORECASE, compile

BAD_WORDS = [
   'poo',
   'frack',
   'poppycock',
   'dunderhead',
   'lordy'
]

def censor_0(sentence: str) -> str:
   sentencelist = sentence.split(" ")
   for word in sentencelist:
      if word.strip().lower() in BAD_WORDS:
         sentence = sentence.replace(word.strip(), f"{word.strip()[0]}{"*" * (len(word.strip()) - 2)}{word.strip()[-1]}")
   return sentence

def censor_1(sentence: str) -> str:
   for word in BAD_WORDS:
      sentence = sub(word, f"{f"{word.strip()[0]}{"*" * (len(word.strip()) - 2)}{word.strip()[-1]}"}", sentence, flags = IGNORECASE)
   return sentence