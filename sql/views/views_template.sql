DROP VIEW IF EXISTS patterns_view;
CREATE VIEW patterns_view AS
{{ sql/views/select/patterns_view_select.sql }}

DROP VIEW IF EXISTS matches_view;
CREATE VIEW matches_view AS
{{ sql/views/select/matches_view_select.sql }}

DROP VIEW IF EXISTS pattern_matches_view;
CREATE VIEW pattern_matches_view AS
{{ sql/views/select/pattern_matches_view_select.sql }}

DROP VIEW IF EXISTS pattern_matches_count_view;
CREATE VIEW pattern_matches_count_view AS
{{ sql/views/select/count/pattern_matches_view_select_count.sql }}

DROP VIEW IF EXISTS documents_view;
CREATE VIEW documents_view AS
{{ sql/views/select/documents_view_select.sql }}

DROP VIEW IF EXISTS sentences_view;
CREATE VIEW sentences_view AS
{{ sql/views/select/sentences_view_select.sql }}