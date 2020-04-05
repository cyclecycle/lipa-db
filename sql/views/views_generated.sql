-- FILE AUTOGENERATED BY scripts/generate_views.py
DROP VIEW IF EXISTS patterns_view;
CREATE VIEW patterns_view AS
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

DROP VIEW IF EXISTS matches_view;
CREATE VIEW matches_view AS
select
    matches.id,
    matches.sentence_id,
    sentences.document_id,
    matches.data "match_data",
    sentences.data as "sentence_data"
from
    matches
    left join sentences on matches.sentence_id = sentences.id;

DROP VIEW IF EXISTS pattern_matches_view;
CREATE VIEW pattern_matches_view AS
select
    pattern_matches.pattern_id,
    pattern_matches.match_id,
    matches.id,
    matches.sentence_id,
    sentences.document_id,
    matches.data "match_data",
    sentences.data as "sentence_data"
from
    pattern_matches
    inner join matches on pattern_matches.match_id = matches.id
    inner join sentences on matches.sentence_id = sentences.id
;

DROP VIEW IF EXISTS pattern_training_matches_view;
CREATE VIEW pattern_training_matches_view AS
select
    pattern_training_matches.pattern_id,
    pattern_training_matches.match_id,
    matches.id,
    matches.sentence_id,
    sentences.document_id,
    matches.data "match_data",
    sentences.data as "sentence_data"
from
    pattern_training_matches
    inner join matches on pattern_training_matches.match_id = matches.id
    inner join sentences on matches.sentence_id = sentences.id
;

DROP VIEW IF EXISTS pattern_matches_count_view;
CREATE VIEW pattern_matches_count_view AS
select
    count(*) as 'count'
from pattern_matches;


DROP VIEW IF EXISTS documents_view;
CREATE VIEW documents_view AS
select
    documents.id,
    count(distinct sentences.id) as n_sentences,
    count(distinct pattern_matches.id) as n_matches,
    documents.data
from
    documents
    left join sentences on sentences.document_id = documents.id
    left join matches on sentences.id = matches.sentence_id
    left join pattern_matches on matches.id = pattern_matches.match_id
group by
    documents.id;

DROP VIEW IF EXISTS sentences_view;
CREATE VIEW sentences_view AS
select
    sentences.id,
    sentences.data,
    count(pattern_matches.id) as n_matches
from
    sentences
    left join matches on sentences.id = matches.sentence_id
    left join pattern_matches on matches.id = pattern_matches.match_id
group by
    sentences.id
order by
    n_matches desc;