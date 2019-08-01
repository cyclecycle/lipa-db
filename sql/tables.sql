PRAGMA foreign_keys=ON;

CREATE TABLE documents (
    -- Contains only the id and content fields specified in the provided corpus_schema
    id integer primary key,
    data blob
);

CREATE TABLE sentences (
    id integer primary key,
    document_id integer,
    text text,
    data blob,
    foreign key(document_id) references documents(id) on delete cascade
);

CREATE TABLE sentence_linguistic_data (
    id integer primary key,
    sentence_id integer,
    spacy_doc blob,
    spacy_vocab blob,
    foreign key(sentence_id) references sentences(id) on delete cascade
);

CREATE TABLE tokens (
    id integer primary key,
    sentence_id integer,
    token_offset integer,  -- Token number in sentence
    data blob,
    foreign key(sentence_id) references sentences(id) on delete cascade
);

CREATE TABLE matches (
    id integer primary key,
    sentence_id integer not null,
    data blob not null,
    foreign key(sentence_id) references sentences(id) on delete cascade
);

CREATE TABLE patterns (
    id integer primary key,
    name text,
    role_pattern_instance blob not null,  -- Python class serialised with pickle
    data blob
);

CREATE TABLE pattern_training_matches (
    match_id integer not null,
    pattern_id integer not null,
    pos_or_neg text not null,
    foreign key(match_id) references matches(id) on delete cascade,
    foreign key(pattern_id) references patterns(id) on delete cascade
);

CREATE TABLE pattern_matches (
    id integer primary key,
    match_id integer references matches(id) on delete cascade,
    pattern_id integer references patterns(id) on delete cascade
);


