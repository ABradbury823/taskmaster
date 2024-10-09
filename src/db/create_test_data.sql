-- delete existing tables and schema
DROP TABLE IF EXISTS test.task_categories CASCADE;
DROP TABLE IF EXISTS test.categories CASCADE;
DROP TABLE IF EXISTS test.tasks CASCADE;
DROP TABLE IF EXISTS test.taskboards CASCADE;
DROP TABLE IF EXISTS test.team_members CASCADE;
DROP TABLE IF EXISTS test.teams CASCADE;
DROP TABLE IF EXISTS test.users CASCADE;
DROP SCHEMA IF EXISTS test CASCADE;
--COMMIT;
-- create schema and intialize parameters
CREATE SCHEMA IF NOT EXISTS test;

-- define tablespace for created tables
-- empty string means use the database's default tablespace
SET default_tablespace = '';

-- do not use object ids for new tables
SET default_with_oids = FALSE;

-- make users table
CREATE TABLE IF NOT EXISTS test.users (
	id SERIAL PRIMARY KEY,
	name TEXT UNIQUE NOT NULL,
	email TEXT UNIQUE NOT NULL,
	password TEXT NOT NULL,
	display_name TEXT NOT NULL DEFAULT '',	-- later set to user name by default
	bio TEXT NOT NULL DEFAULT ''
);

-- make teams table
CREATE TABLE IF NOT EXISTS test.teams (
	id SERIAL PRIMARY KEY,
	name TEXT NOT NULL,
	created_on DATE NOT NULL DEFAULT '-infinity'
);

-- make team members table, a join table between users and teams
CREATE TABLE IF NOT EXISTS test.team_members (
	id SERIAL PRIMARY KEY,
	team_id INTEGER NOT NULL REFERENCES test.teams(id),
	user_id INTEGER NOT NULL REFERENCES test.users(id) ON DELETE CASCADE,
	joined_on DATE NOT NULL DEFAULT '-infinity',
	is_admin BOOLEAN NOT NULL DEFAULT FALSE
);

-- make taskboards table
CREATE TABLE IF NOT EXISTS test.taskboards (
	id SERIAL PRIMARY KEY,
	team_id INTEGER NOT NULL REFERENCES test.teams(id),
	name TEXT NOT NULL
);


-- make tasks table
CREATE TABLE IF NOT EXISTS test.tasks (
	id SERIAL PRIMARY KEY,
	taskboard_id INTEGER NOT NULL REFERENCES test.taskboards(id),
	assignee_id INTEGER REFERENCES test.users(id) ON DELETE SET NULL,
	name TEXT NOT NULL,
	description TEXT NOT NULL DEFAULT '',
	due_date TIMESTAMP
);

-- make categories table
CREATE TABLE IF NOT EXISTS test.categories (
	id SERIAL PRIMARY KEY,
	taskboard_id INTEGER NOT NULL REFERENCES test.taskboards(id),
	name TEXT NOT NULL
);

-- make task categories table, a join table between tasks and categories
CREATE TABLE IF NOT EXISTS test.task_categories (
	id SERIAL PRIMARY KEY,
	task_id INTEGER NOT NULL REFERENCES test.tasks(id),
	category_id INTEGER NOT NULL REFERENCES test.categories(id)
);

-- make test users
INSERT INTO test.users (name, email, password, display_name) VALUES ('God', 'topG@email.com', 'password', 'Father of Man');
INSERT INTO test.users (name, email, password) VALUES ('Adam', 'adam@email.com', 'adam_madman');
INSERT INTO test.users (name, email, password) VALUES ('Eve', 'eve@email.com', 'eve<3apples');
INSERT INTO test.users (name, email, password, display_name) VALUES ('Satan', 'notevil@email.com', 'evilgenius666', 'Serpent');

-- make test teams
INSERT INTO test.teams (name) VALUES ('Eden Crew');
INSERT INTO test.teams (name) VALUES ('Divine Realm');

-- make test team members
INSERT INTO test.team_members (team_id, user_id, is_admin) VALUES (1, 1, TRUE);
INSERT INTO test.team_members (team_id, user_id) VALUES (1, 2);
INSERT INTO test.team_members (team_id, user_id) VALUES (1, 3);
INSERT INTO test.team_members (team_id, user_id, is_admin) VALUES (1, 4, TRUE);
INSERT INTO test.team_members (team_id, user_id, is_admin) VALUES (2, 1, TRUE);
INSERT INTO test.team_members (team_id, user_id, is_admin) VALUES (2, 4, TRUE);

-- make test taskboards
INSERT INTO test.taskboards (team_id, name) VALUES (1, 'Garden of Eden Tending');
INSERT INTO test.taskboards (team_id, name) VALUES (2, 'Divine Tasks');

-- make test tasks
INSERT INTO test.tasks (taskboard_id, assignee_id, name, description, due_date)
VALUES (1, 2, 'Name All Creatures', 'Give all wild animals and livestock a name.', 'tomorrow');
INSERT INTO test.tasks (taskboard_id, assignee_id, name, description)
VALUES (1, 1, 'Find Adam''s Helper', 'Find a suitable helper for Adam.');
INSERT INTO test.tasks (taskboard_id, name, description)
VALUES (1, 'Avoid the Tree of Knowledge', 
'Do not eat from the tree of the knowledge of good and evil, for when you eat from it you will certainly die.');

INSERT INTO test.tasks (taskboard_id, assignee_id, name) VALUES (2, 1, 'Create Garden of Eden');
INSERT INTO test.tasks (taskboard_id, assignee_id, name) VALUES (2, 4, 'Bring About the Fall of Man');

-- make test categories
INSERT INTO test.categories (taskboard_id, name) VALUES (1, 'Commandment');
INSERT INTO test.categories (taskboard_id, name) VALUES (1, 'Done');
INSERT INTO test.categories (taskboard_id, name) VALUES (2, 'Done');
INSERT INTO test.categories (taskboard_id, name) VALUES (2, 'Overdue');
INSERT INTO test.categories (taskboard_id, name) VALUES (2, 'High Priority');

-- make test task categories
INSERT INTO test.task_categories (task_id, category_id) VALUES (1, 1);
INSERT INTO test.task_categories (task_id, category_id) VALUES (1, 2);
INSERT INTO test.task_categories (task_id, category_id) VALUES (2, 2);
INSERT INTO test.task_categories (task_id, category_id) VALUES (3, 1);
INSERT INTO test.task_categories (task_id, category_id) VALUES (4, 3);
INSERT INTO test.task_categories (task_id, category_id) VALUES (5, 4);
INSERT INTO test.task_categories (task_id, category_id) VALUES (5, 5);

-- update empty display names
UPDATE test.users
SET display_name = name
WHERE display_name = '';