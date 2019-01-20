import io
import unicodedata

dataset = io.open('./irish_words.txt', 'r', encoding='utf-8')
ascii_words = []
for line in dataset:
    word = line.split('\t')[1]
    nfkd_form = unicodedata.normalize('NFKD', word)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    ascii_words.append(only_ascii)

formatted = "'" + "', \n'".join(ascii_words) + "'"
out_file = open('./irish_js.txt', 'w')
out_file.write(formatted)
out_file.close()

