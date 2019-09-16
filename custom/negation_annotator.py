import os
from spacy.matcher import Matcher
from spacy.tokens import Token
from util import util

CWD = util.get_file_directory(__file__)
VOCAB_PATH = os.path.join(CWD, 'negation_vocab/terms.txt')


class NegationAnnotator:
    name = 'negation_annotator'

    def __init__(self, nlp):
        with open(VOCAB_PATH) as f:
            vocab = [line.strip() for line in f.readlines()]

        self.matcher = Matcher(nlp.vocab)
        for term in vocab:
            self.matcher.add('negation', None, [{'LOWER': term}])

        Token.set_extension('is_negation', default=False)

    def __call__(self, doc):
        matches = self.matcher(doc)
        for label, start, end in matches:
            token = doc[start]
            token._.set('is_negation', True)
        return doc
