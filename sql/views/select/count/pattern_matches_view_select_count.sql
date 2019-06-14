select
    count(pattern_matches.pattern_id)
from
    pattern_matches
    inner join matches on pattern_matches.match_id = matches.id
    inner join sentences on matches.sentence_id = sentences.id
;