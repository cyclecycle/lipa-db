select
    matches.id,
    matches.sentence_id,
    sentences.document_id,
    matches.data "match_data",
    sentences.data as "sentence_data"
from
    matches
    left join sentences on matches.sentence_id = sentences.id;