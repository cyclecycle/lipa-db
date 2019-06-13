select
    pattern_matches.pattern_id,
    pattern_matches.match_id,
    matches.id,
    matches.sentence_id,
    sentences.document_id,
    matches.data "match_data"
    -- sentences.data as "sentence_data"
from
    pattern_matches
    inner join matches on pattern_matches.match_id = matches.id
    inner join sentences on matches.sentence_id = sentences.id
;