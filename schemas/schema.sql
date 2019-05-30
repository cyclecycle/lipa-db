CREATE TABLE documents (
    -- Contains only the id and content fields specified in the provided corpus_schema
    id integer primary key,
    data blob
);

CREATE TABLE sentences (
    id integer primary key,
    document_id integer,
    sentence_text text,
    data blob,  -- Contains list of tokens and their linguistic features
    foreign key(document_id) references documents(id)
);

CREATE TABLE patterns (
    id integer primary key,
    data blob
);

CREATE TABLE training_examples (
    id integer primary key,
    data blob,
    pos_or_neg boolean,
    pattern_id integer,
    sentence_id integer,
    foreign key(pattern_id) references patterns(id),
    foreign key(sentence_id) references sentences(id)
);

CREATE TABLE matches (
    id integer primary key,
    pattern_id integer,
    sentence_id integer,
    data blob,
    foreign key(pattern_id) references patterns(id),
    foreign key(sentence_id) references sentences(id)
);
