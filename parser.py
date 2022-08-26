import re

with open("PythonTest.txt", encoding="utf-8") as f:
    for line in f.readlines():
        if not line.startswith('#') and not line.startswith('\n'):
            if re.split(r"[\t,;]", line):
                text = line.removesuffix("\n").split("\t")
                english_word = text[0].split(';')
                rus_word = text[1].split(';')
                for eng in english_word:
                    for rus in rus_word:
                        with open("English.txt", 'a', encoding='utf-8') as e:
                            e.write(f'{eng.strip()}\n')
                        with open("Russian.txt", 'a', encoding='utf-8') as r:
                            r.write(f'{rus.strip()}\n')
