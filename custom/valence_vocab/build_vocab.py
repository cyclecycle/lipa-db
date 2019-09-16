from itertools import product
from word_forms.word_forms import get_word_forms


vocabs = [
    {
        'name': 'valence_down',
        'file': 'valence_down_root.txt',
        'expanded': [],
        'expanded_file': 'valence_down_expanded.txt',
        'postbuild': {
            'add': [],
            'remove': [],
        },
    },
    {
        'name': 'valence_up',
        'file': 'valence_up_root.txt',
        'expanded': [],
        'expanded_file': 'valence_up_expanded.txt',
        'postbuild': {
            'add': [
                'overexpress',
                'overexpression',
                'up-regulates',
            ],
            'remove': [
                'stimulus',
                'stimuli',
                'stimulative',
            ],
        },
    }
]


def word_forms_to_flat_list(word_forms_dict):
    sets = word_forms_dict.values()
    flat = [x for y in sets for x in y]
    flat = set(flat)
    return flat


def yield_word_forms(term):
    terms = term.split(' ')
    form_dicts = [get_word_forms(t) for t in terms]
    form_lists = [word_forms_to_flat_list(d) for d in form_dicts]
    for comb in product(*form_lists):
        new_term = ' '.join(comb)
        yield new_term


if __name__ == '__main__':
    for vocab in vocabs:
        with open(vocab['file'], encoding='utf-8') as f:
            lines = f.readlines()
            lines = [l.strip() for l in lines]
            vocab['terms'] = lines

    for vocab in vocabs:
        new_terms = []
        for term in vocab['terms']:
            new_terms.append(term)
            new_terms += list(yield_word_forms(term))
            new_terms = [t.lower() for t in new_terms]
        new_terms += vocab['postbuild']['add']
        new_terms = list(set(new_terms) - set(vocab['postbuild']['remove']))
        new_terms = sorted(new_terms)
        vocab['expanded'] = new_terms

    for vocab in vocabs:
        with open(vocab['expanded_file'], 'w', encoding='utf-8') as f:
            f.write('\n'.join(vocab['expanded']))