import dask.bag as db
b = db.from_sequence(['apple', 'banana', 'cherry', 'date', 'elderberry'], npartitions=2)
b.to_textfiles('/home/zhang/Documents/*.txt', name_function=None, compression='infer', encoding='utf-8', compute=True, storage_options=None, last_endline=False)
