import os
import re
from util import util

CWD = util.get_file_directory(__file__)
VOCAB_PATH = os.path.join(CWD, 'abstract_demarcation_vocab/section_delimiters_flat.txt')
with open(VOCAB_PATH) as f:
    vocab = [l.strip() for l in f.readlines()]

DEMARC_PATTERN = re.compile(r'\s?{}'.format('|'.join(vocab)), flags=re.I)


def remove_abstract_demarcation(string):
    string = DEMARC_PATTERN.sub('', string)
    return string
