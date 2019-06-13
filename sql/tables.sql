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
    foreign key(document_id) references documents(id)
);

CREATE TABLE sentence_linguistic_data (
    id integer primary key,
    sentence_id integer,
    spacy_doc blob,
    spacy_vocab blob,
    foreign key(sentence_id) references sentences(id)
);

CREATE TABLE tokens (
    id integer primary key,
    sentence_id integer,
    token_offset integer,  -- Token number in sentence
    data blob,
    foreign key(sentence_id) references sentences(id)
);

CREATE TABLE matches (
    id integer primary key,
    sentence_id integer not null,
    data blob not null,
    foreign key(sentence_id) references sentences(id)
);

CREATE TABLE patterns (
    id integer primary key,
    name text,
    role_pattern_instance blob not null
);

CREATE TABLE pattern_training_matches (
    match_id integer not null,
    pattern_id integer not null,
    pos_or_neg text not null,
    foreign key(match_id) references matches(id)
    foreign key(pattern_id) references patterns(id)
);

CREATE TABLE pattern_matches (
    id integer primary key,
    match_id integer,
    pattern_id integer,
    foreign key(match_id) references matches(id),
    foreign key(pattern_id) references pattern(id)
);

