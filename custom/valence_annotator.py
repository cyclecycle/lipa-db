import os
from spacy.matcher import Matcher
from spacy.tokens import Doc, Token
from util import util

CWD = util.get_file_directory(__file__)
UP_VOCAB_PATH = os.path.join(CWD, 'vocab/valence_up_expanded.txt')
DOWN_VOCAB_PATH = os.path.join(CWD, 'vocab/valence_down_expanded.txt')


class ValenceAnnotator:
    name = 'valence_annotator'

    def __init__(self, nlp):
        with open(UP_VOCAB_PATH) as f:
            up_vocab = [line.strip() for line in f.readlines()]
        with open(DOWN_VOCAB_PATH) as f:
            down_vocab = [line.strip() for line in f.readlines()]

        self.matcher = Matcher(nlp.vocab)
        for up_term in up_vocab:
            self.matcher.add('UP', None, [{'LOWER': up_term}])
        for down_term in down_vocab:
            self.matcher.add('DOWN', None, [{'LOWER': down_term}])

        Token.set_extension('valence', default=None)
        Doc.set_extension('has_valence_term', getter=self.has_valence_term)

    def __call__(self, doc):
        matches = self.matcher(doc)
        for label, start, end in matches:
            label = self.matcher.vocab[label].text
            token = doc[start]
            token._.set('valence', label)
        return doc

    def has_valence_term(self, tokens):
        return any([t._.get('valence') for t in tokens])
