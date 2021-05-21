PRAGMA foreign_keys = ON;

INSERT INTO users
    (username, fullname, email, password, class, residency)
VALUES
    ('abigley', 'Alyssa Bigley', 'abigley@umich.edu', 'pass333', 'Master''s', 'U.S.Citizen');
INSERT INTO users
    (username, fullname, email, password, class, residency)
VALUES
    ('tonyd', 'Tony Dae', 'tonyd@umich.edu', 'pass333', 'PhD', 'Permanent Resident');
INSERT INTO users
    (username, fullname, email, password, class, residency)
VALUES
    ('djj', 'Don Jones', 'djj@umich.edu', 'pass333', 'Postdoc', 'U.S. Citizen');

INSERT INTO tags
    (username, tag)
VALUES
    ('abigley', 'Women');
INSERT INTO tags
    (username, tag)
VALUES
    ('tonyd', 'URM');
INSERT INTO tags
    (username, tag)
VALUES
    ('tonyd', 'International');