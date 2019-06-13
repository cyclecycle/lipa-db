select
    documents.id,
    count(sentences.id) as n_sentences,
    count(pattern_matches.id) as n_matches,
    documents.data
from
    documents
    left join sentences on sentences.document_id = documents.id
    left join matches on sentences.id = matches.sentence_id
    left join pattern_matches on matches.id = pattern_matches.match_id
group by
    documents.id
order by
    n_matches desc;