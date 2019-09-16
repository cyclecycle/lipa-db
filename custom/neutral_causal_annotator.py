import os
from spacy.matcher import Matcher
from spacy.tokens import Token
from util import util

CWD = util.get_file_directory(__file__)
VOCAB_PATH = os.path.join(CWD, 'neutral_causal_vocab/terms.txt')


class NeutralCausalAnnotator:
    name = 'neutral_causal_annotator'

    def __init__(self, nlp):
        with open(VOCAB_PATH) as f:
            vocab = [line.strip() for line in f.readlines()]

        self.matcher = Matcher(nlp.vocab)
        for term in vocab:
            self.matcher.add('neutral_causal', None, [{'LOWER': term}])

        Token.set_extension('is_neutral_causal_term', default=False)

    def __call__(self, doc):
        matches = self.matcher(doc)
        for label, start, end in matches:
            token = doc[start]
            token._.set('is_neutral_causal_term', True)
        return doc
