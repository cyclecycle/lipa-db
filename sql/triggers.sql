CREATE TRIGGER default_pattern_name
AFTER INSERT ON patterns
FOR EACH ROW
WHEN NEW.name IS NULL
BEGIN
    UPDATE patterns SET name = 'Pattern ' || CAST(NEW.id as VARCHAR) WHERE id = NEW.id;
END;