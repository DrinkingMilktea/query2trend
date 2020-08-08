stopword = set(open("./data/stop_word_korean.txt").read().split())

from konlpy.tag import Okt

def word2noun(sentence):
    tokenizer = Okt()
    tempX = tokenizer.morphs(sentence)
    ret = [word for word in tempX if not word in stopword]
    return " ".join(ret)

fromfilelist = [
    "wiki-alpha.txt",
    "wiki-kowiki.txt",
    "wiki-kowikisource.txt",
    "wiki-kowiktionary.txt",
    "wiki-namu.txt",
    "wiki-oriwiki.txt",
    "wiki-osa.txt"
]

morphed = "morphed-"

def morpher(name):
    savefilename = morphed + name
    with open("/home/sentiment/tenTB/wiki_dump/txtfiles/"+name, 'r') as f:
        with open("/home/sentiment/tenTB/wiki_dump/txtfiles/"+savefilename, 'w') as fw:
            while True:
                line = f.readline()
                if not line: break
                fw.write(word2noun(line))
                fw.write('\n')
    print(name, "finish")

from multiprocessing import Pool
myp = Pool(len(fromfilelist))
with myp:
    myp.map(morpher, fromfilelist)