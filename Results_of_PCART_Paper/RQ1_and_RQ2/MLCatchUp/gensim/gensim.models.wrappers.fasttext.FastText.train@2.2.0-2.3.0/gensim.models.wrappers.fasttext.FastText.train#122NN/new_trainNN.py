from gensim.models.wrappers import FastText
ft_path = '/home/zhang/fastText/build/fasttext'
corpus_file = '/home/zhang/corpus.txt'
output_file = '/home/zhang/'
model = FastText.train(ft_path, corpus_file, output_file, 'cbow', 100, 0.025, 5, 1, 'ns', 0.001, 5, iter=1, min_n=3, max_n=6, sorted_vocab=1, word_ngrams=1)
