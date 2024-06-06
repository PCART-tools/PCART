from gensim.models import Word2Vec
sentences = [['hello', 'world'], ['gensim', 'word2vec']]
model = Word2Vec(min_count=1)
model.build_vocab(sentences)
model.train(sentences, None, word_count=0, total_examples=model.corpus_count, queue_factor=2, report_delay=1.0, epochs=None, start_alpha=None, end_alpha=None)
