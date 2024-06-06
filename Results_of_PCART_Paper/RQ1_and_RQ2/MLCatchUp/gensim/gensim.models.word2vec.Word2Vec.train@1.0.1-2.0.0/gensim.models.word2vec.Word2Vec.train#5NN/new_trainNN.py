from gensim.models import Word2Vec
sentences = [['hello', 'world'], ['gensim', 'word2vec']]
model = Word2Vec(min_count=1)
model.build_vocab(sentences)
model.train(sentences=sentences, total_words=None, epochs=None, start_alpha=None, end_alpha=None)
