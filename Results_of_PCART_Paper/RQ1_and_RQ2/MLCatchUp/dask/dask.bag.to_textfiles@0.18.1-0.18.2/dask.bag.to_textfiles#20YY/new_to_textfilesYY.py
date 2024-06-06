import dask.bag as db
b = db.from_sequence(['apple', 'banana', 'cherry', 'date', 'elderberry'], npartitions=2)
b.to_textfiles(path='/home/zhang/Documents/*.txt', name_function=None, compression='infer', encoding='utf-8', compute=True, last_endline=False)
