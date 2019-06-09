select
    pattern_matches.match_id,
    pattern_matches.pattern_id,
    patterns.name,
    matches.sentence_id,
    sentences.document_id,
    sentences.data,
    matches.data
from
    pattern_matches,
    patterns,
    matches,
    sentences
where
    pattern_matches.pattern_id = patterns.id and
    pattern_matches.match_id = matches.id and
    matches.sentence_id = sentences.id
group by
    pattern_matches.match_id
order by
    patterns.name asc;