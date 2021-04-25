def wordcount(filename):
        counts = {'characters' : 0,
                  'words' : 0,
                  'lines' : 0}
        unique_words = set()

        for single_line in open(filename):
            counts['lines'] += 1
            counts['characters'] += len(single_line)
            counts['words'] += len(single_line.split())

            unique_words.update(single_line.split())

        counts['unique words'] = len(unique_words)

        for key, value in counts.items():
            print(f'{key}: {value}')

wordcount('file.txt')
