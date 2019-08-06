import re
import spacy
from spacy.tokens import Doc
from nlp.custom_tokenize import custom_tokenizer
from util import util

config = util.load_config()

REGEXES = {
    'parenthetic': r'(?<=\s|,|\.)(\(.+?\))(?=\s|,|\.)',
    'multispace': r'\s+',
    'initial_colon_clause': r'^.+?:\s?',
    'floating_punct': r'(\s)(?=[,\.]\s)',
}

REGEXES = {name: re.compile(regex) for name, regex in REGEXES.items()}

SPACY_DISABLE = [
    'ner',
    'entity_ruler',
    'textcat',
    'sentencizer',
    'merge_noun_chunks',
    'merge_entities',
    'merge_subtokens',
]


class Parser:
    def __init__(self):
        spacy_model = config['spacy_model']
        self.nlp = spacy.load(spacy_model, disable=SPACY_DISABLE)
        self.nlp.tokenizer = custom_tokenizer(self.nlp)

    def parse(
        self,
        text,
        resolve_corefs=False,
        resolve_acros=False,
        coref_clusters=False,
        sentence_case=False,
    ):
        text = str(text)
        if text[-1] != '.':
            text += '.'
        text = text.replace('\n', ' ')
        text = text.replace('\\n', ' ')
        text = re.sub(REGEXES['multispace'], ' ', text)
        text = re.sub(REGEXES['floating_punct'], '', text)
        text = text.strip()
        text = re.sub(REGEXES['parenthetic'], ' ', text)
        text = re.sub(REGEXES['multispace'], ' ', text)
        text = re.sub(REGEXES['floating_punct'], '', text)
        if sentence_case:
            doc = self.nlp.make_doc(text)
            doc = sentence_case(doc, self.nlp)
        else:
            doc = self.nlp(text)
        return doc


def separate_trees(doc):
    '''For each ROOT token in doc, return the subtree as a Doc object

    Arguments:
        doc {SpaCy Doc}
    '''
    if len(doc) == 1:
        yield doc
    else:
        Doc.set_extension('tree_i', default=None, force=True)
        Doc.set_extension('start_idx', default=None, force=True)
        tree_i = 0
        for token in doc:
            if token.dep_ == 'ROOT':
                idxs = [w.i for w in token.subtree]
                span = doc[min(idxs) : max(idxs)]
                tree = span.as_doc()
                tree._.tree_i = tree_i
                start_idx = min([w.idx for w in token.subtree])
                tree._.start_idx = start_idx
                tree_i += 1
                yield tree


def text_to_trees(text):
    doc = text_to_doc(text)
    png = visualise_spacy_tree.plot(doc)
    with open('parse_trees/1.png', 'wb') as f:
        f.write(png)
    for tree in separate_trees(doc):
        yield tree


if __name__ == '__main__':
    text = "Immune thrombocytopenia (ITP) is an acquired autoimmune disease characterized by an immune mediated decrease in platelet number"
    input_text_to_trees(text)
