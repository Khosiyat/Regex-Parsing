#Copywrite Warning: Owner of the code is Gulcheera Academy(Khosiyat Sabirova)
                                                        #This code can be used by anyone for free, but the name "Gulcheera Academy" must be acknowledged 
#CHUNKING (Regex Parsing)

#nltk packages are imported
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

example_4Tagging1 = state_union.raw("2005-GWBush.txt")#create a variable to store a raw data which is in text format provided by the corpus of nltk package
example_4Tagging2 = state_union.raw("2006-GWBush.txt")

def contentTagging2(sample_text,train_text ):
    tokenized_trained = PunktSentenceTokenizer(train_text)
    tokenized = tokenized_trained.tokenize(sample_text)
    try:
        for lexUnit in tokenized:
            words = nltk.word_tokenize(lexUnit)
            tagged = nltk.pos_tag(words)
            chunk_pattern = r"""Chunk: {<.*>+}}<VB.?|IN|DT|TO>+{"""
            #r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunk_parsedPattern = nltk.RegexpParser(chunk_pattern)
            chunked = chunk_parsedPattern.parse(tagged)    

        chunk_pattern = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""


        for netUnit in chunked.subtrees():
            print(netUnit)

        for netUnit in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
            print(netUnit)

    except Exception as skip:
        print(str(skip))
#print the result
contentTagging2(example_4Tagging1,example_4Tagging2)


import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

example_4Tagging1 = state_union.raw("2005-GWBush.txt")
example_4Tagging2 = state_union.raw("2006-GWBush.txt")

def contentTagging3(sample_text,train_text):
    tokenized_trained = PunktSentenceTokenizer(train_text)
    tokenized = tokenized_trained.tokenize(sample_text)
    try:
        for lexUnit in tokenized:
            words = nltk.word_tokenize(lexUnit)
            tagged = nltk.pos_tag(words)
            chunked_pattern = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            #r"""Chunk: {<.*>+}}<VB.?|IN|DT|TO>+{"""
            #}<VB.?|IN|DT|TO>+{
            chunk_parsedPattern = nltk.RegexpParser(chunked_pattern)
            chunked = chunk_parsedPattern.parse(tagged)
            
            print(chunked)
            for netUnit in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
                print(netUnit)


    except Exception as skip:
        print(str(skip))
#print the result
contentTagging3(example_4Tagging1,example_4Tagging2)
