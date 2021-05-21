PRAGMA foreign_keys = ON;

CREATE TABLE users
(
    username VARCHAR(20) NOT NULL,
    fullname VARCHAR(40) NOT NULL,
    email VARCHAR(40) NOT NULL,
    password CHARACTER(256) NOT NULL,
    class VARCHAR(40) NOT NULL,
    residency VARCHAR(40) NOT NULL,
    PRIMARY KEY(username)
);

CREATE TABLE tags 
(
    username VARCHAR(20) NOT NULL,
    tag VARCHAR(20) NOT NULL,
    PRIMARY KEY (username, tag),
    FOREIGN KEY (username) REFERENCES users
);