import numpy as np
import os
import pickle


def word2id(path, name):
    if os.path.exists(path+name[:-3]+"pkl"):
        with open(path+name[:-3]+"pkl") as f:
            word_to_id, id_to_word = pickle.load(f)
        return word_to_id, id_to_word

    word_to_id = dict()
    id_to_word = dict()

    sentence = [s.strip().split(' ') for s in open(path+name).read().strip().split('\n') if s.strip() != '']
    for i, word in enumerate(sentence):
        if word not in word_to_id:
            tmp_id = len(word_to_id)
            word_to_id[word] = tmp_id
            id_to_word[tmp_id] = word

    with open(path+name[:-3]+"pkl", 'wb') as f:
        pickle.dump((word_to_id, id_to_word), f)

    return sentence, word_to_id, id_to_word

def load_data(path, name):
    sentence, word_to_id, id_to_word = word2id(path, name)

    if os.path.exists(path+name[:-3]+"npy"):
        corpus = np.load(path+name[:-3]+"npy")
        return corpus, word_to_id, id_to_word

    corpus = np.array([word_to_id[w] for w in sentence])

    np.save(path+name[:-3]+"npy", corpus)

    return corpus, word_to_id, id_to_word
