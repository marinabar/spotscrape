from main import findvid, data, findall, download, gendownloads, meta
from remover import remover



file = '/home/mrnb/Téléchargements/spotlistr-exported-playlist (1).csv'
meta(gendownloads(findall(data(file))))

#print(getlyricsfromname("Je te laisserai des mots", "Patrick Watson ", "JCpKrww1Q-onpumYXIRsgEWnZilXwaZrNI8Rp9lCaaTM-jkloRvTo5Dm8ZmagrK3"))