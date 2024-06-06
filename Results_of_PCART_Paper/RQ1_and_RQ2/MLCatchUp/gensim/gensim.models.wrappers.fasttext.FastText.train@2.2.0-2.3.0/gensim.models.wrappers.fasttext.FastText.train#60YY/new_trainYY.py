from gensim.models.wrappers import FastText
ft_path = '/home/zhang/fastText/build/fasttext'
corpus_file = '/home/zhang/corpus.txt'
output_file = '/home/zhang/'
model = FastText.train(ft_path, corpus_file, output_file, model='cbow', size=100, alpha=0.025, window=5, min_count=1, loss='ns', sample=0.001, word_ngrams=1)
