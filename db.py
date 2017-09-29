import dataset

db = dataset.connect('sqlite:///noticias.db')
noticias = db['noticias']