CREATE TABLE documents (
    -- Contains only the id and content fields specified in the provided corpus_schema
    id integer primary key,
    data blob
);

CREATE TABLE document_linguistic_data (
    id integer primary key,
    document_id,
    spacy_doc blob,
    spacy_vocab blob,
    foreign key(document_id) references documents(id)
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
    i integer,
    data blob,
    foreign key(sentence_id) references sentences(id)
);

CREATE TABLE patterns (
    id integer primary key,
    name text,
    seed_example_id integer,
    role_pattern_instance blob,
    foreign key(seed_example_id) references training_examples(id)
);

CREATE TABLE training_examples (
    id integer primary key,
    data blob,
    pos_or_neg text,
    sentence_id integer,
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
