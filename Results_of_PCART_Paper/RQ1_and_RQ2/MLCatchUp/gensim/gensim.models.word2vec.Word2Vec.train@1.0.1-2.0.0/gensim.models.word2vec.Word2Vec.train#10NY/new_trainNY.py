from gensim.models import Word2Vec
sentences = [['hello', 'world'], ['gensim', 'word2vec']]
model = Word2Vec(min_count=1)
model.build_vocab(sentences)
model.train(sentences, None, 0, model.corpus_count, epochs=None, start_alpha=None, end_alpha=None)
