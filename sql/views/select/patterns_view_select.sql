select
    patterns.id,
    patterns.name,
    patterns.data,
    count(pattern_matches.id) as n_matches
from
    patterns
left join
    pattern_matches
on
    patterns.id = pattern_matches.pattern_id
group by
    patterns.id
order by n_matches desc;