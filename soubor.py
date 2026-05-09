def count_rows_and_words(filename):
    n_rows = 0
    n_words = 0
    with open(filename, 'rt', encoding='utf-8') as f:
        for line in f:
            # Pri kazdem pruchodu radku pocitam
            n_rows += 1
            words = line.split()
            n_words += len(words)
            print(words)
            print("cislo radku:",n_rows,"pocet slov:",n_words)
        return n_rows, n_words

count_rows_and_words('Sazka.txt')
# count_rows_and_words('~/Dokumenty/Stažené/cervenec2023.txt')

print("od zacatku")
