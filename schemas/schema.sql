CREATE TABLE documents (
    -- Contains only the id and content fields specified in the provided corpus_schema
    data blob
);

CREATE TABLE sentences (
    document_id integer,
    sentence_text text,
    data blob,  -- Contains list of tokens and their linguistic features
    foreign key(document_id) references documents(rowId)
);

CREATE TABLE patterns (
    data blob
);

CREATE TABLE training_examples (
    data blob,
    pos_or_neg boolean,
    pattern_id integer,
    sentence_id integer,
    foreign key(pattern_id) references patterns(rowId),
    foreign key(sentence_id) references sentences(rowId)
);

CREATE TABLE matches (
    pattern_id integer,
    sentence_id integer,
    data blob,
    foreign key(pattern_id) references patterns(rowId),
    foreign key(sentence_id) references sentences(rowId)
);
