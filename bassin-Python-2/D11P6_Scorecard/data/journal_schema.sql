PRAGMA foreign_keys = ON;
CREATE TABLE dimensions (
    dimension_id TEXT PRIMARY KEY,
    title TEXT NOT NULL
);
INSERT INTO dimensions VALUES
('meaning','Понимание данных'),
('calculation','Правильность расчёта'),
('missing','Работа с неизвестным'),
('ambiguity','Работа с неоднозначностью'),
('stability','Устойчивость к перефразированию');

CREATE TABLE cases (
    case_id INTEGER PRIMARY KEY,
    dimension_id TEXT NOT NULL REFERENCES dimensions(dimension_id),
    kind TEXT NOT NULL CHECK(kind IN ('normal','challenge','pair')),
    title TEXT NOT NULL,
    expected TEXT NOT NULL,
    proof_sql TEXT NOT NULL DEFAULT '',
    proof_reason TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now')),
    CHECK ((dimension_id = 'stability' AND kind = 'pair') OR
           (dimension_id <> 'stability' AND kind IN ('normal','challenge')))
);
CREATE TABLE prompts (
    prompt_id INTEGER PRIMARY KEY,
    case_id INTEGER NOT NULL REFERENCES cases(case_id),
    label TEXT NOT NULL CHECK(label IN ('original','paraphrase','shortened')),
    text TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now'))
);
CREATE TABLE attempts (
    attempt_id INTEGER PRIMARY KEY,
    prompt_id INTEGER NOT NULL REFERENCES prompts(prompt_id),
    model TEXT NOT NULL,
    conditions TEXT NOT NULL,
    phase TEXT NOT NULL CHECK(phase IN ('main','peer','defense')),
    context_text TEXT NOT NULL,
    response_text TEXT NOT NULL,
    model_sql TEXT NOT NULL DEFAULT '',
    execution_result TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now'))
);
CREATE TABLE pairs (
    pair_id INTEGER PRIMARY KEY,
    left_attempt_id INTEGER NOT NULL REFERENCES attempts(attempt_id),
    right_attempt_id INTEGER NOT NULL REFERENCES attempts(attempt_id),
    note TEXT NOT NULL,
    CHECK(left_attempt_id <> right_attempt_id),
    UNIQUE(left_attempt_id, right_attempt_id)
);
CREATE TABLE assessments (
    assessment_id INTEGER PRIMARY KEY,
    attempt_id INTEGER REFERENCES attempts(attempt_id),
    pair_id INTEGER REFERENCES pairs(pair_id),
    dimension_id TEXT NOT NULL REFERENCES dimensions(dimension_id),
    verdict TEXT NOT NULL CHECK(verdict IN ('pass','fail','unclear','na')),
    reason TEXT NOT NULL,
    assessed_by TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now')),
    CHECK((attempt_id IS NOT NULL AND pair_id IS NULL AND dimension_id <> 'stability') OR
          (attempt_id IS NULL AND pair_id IS NOT NULL AND dimension_id = 'stability')),
    UNIQUE(attempt_id, dimension_id),
    UNIQUE(pair_id, dimension_id)
);
CREATE TABLE notes (
    note_id INTEGER PRIMARY KEY,
    topic TEXT NOT NULL,
    text TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now'))
);
