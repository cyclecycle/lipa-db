CREATE VIEW patterns_view (id, name, n_matches) AS
    {{ sql/view/patterns_view_select.sql }}