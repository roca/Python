#!/usr/bin/python

import re
from parse_out_pubmed_text import parseOutText

def main():
    f = open("./pubmed.txt", "r")
    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    abstracts = re.compile('Abastract-\d+\)').split(all_text)
    for i, abstract in enumerate(abstracts):
        a =  open("./abstracts/abstract-" + str(i), "w")
        a.write(abstract)
        a.close()



if __name__ == '__main__':
    main()
