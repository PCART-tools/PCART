from gensim.models import Word2Vec
sentences = [['hello', 'world'], ['gensim', 'word2vec']]
model = Word2Vec(min_count=1)
model.build_vocab(sentences)
model.train(sentences, None, word_count=0, epochs=None, start_alpha=None, end_alpha=None)
