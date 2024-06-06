from gensim.models import Word2Vec
model = Word2Vec(size=50, min_count=1)
sentences = [['hello', 'world'], ['gensim', 'word2vec']]
model.build_vocab(sentences)
model.train(sentences, total_words=None, word_count=0, total_examples=None, queue_factor=2, report_delay=1.0)
fname = '/home/zhang/glove.6B.50d.w2v.txt'
model.intersect_word2vec_format(fname, False, 'utf8', unicode_errors='strict', lockf=0.0)
