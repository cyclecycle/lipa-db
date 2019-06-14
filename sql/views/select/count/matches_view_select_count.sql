select
    count(matches.id)
from
    matches
    left join sentences on matches.sentence_id = sentences.id;