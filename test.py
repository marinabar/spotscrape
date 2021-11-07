from main import findvid, data, findall, download, gendownloads, meta
from remover import remover



file = '/home/mrnb/Téléchargements/spotlistr-exported-playlist (1).csv'

meta(gendownloads(findall(data(file))))