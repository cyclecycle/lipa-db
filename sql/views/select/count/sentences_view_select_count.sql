select
    count(sentences.id)
from
    sentences
    left join matches on sentences.id = matches.sentence_id
    left join pattern_matches on matches.id = pattern_matches.match_id
group by
    sentences.id
order by
    n_matches desc;