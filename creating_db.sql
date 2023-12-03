DROP TABLE IF EXISTS grades;
DROP TABLE IF EXISTS subjects;
DROP TABLE IF EXISTS teachers;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS groups;

CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    group_name VARCHAR(50)
);

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    group_id INTEGER REFERENCES groups(id)
    	ON DELETE CASCADE
    	ON UPDATE CASCADE
);

CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

CREATE TABLE subjects (
    id SERIAL PRIMARY KEY,
    subject_name VARCHAR(50),
    teacher_id INTEGER REFERENCES teachers(id)
    	ON DELETE SET NULL
    	ON UPDATE CASCADE
);

CREATE TABLE grades (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(id)
    	ON DELETE SET NULL
    	ON UPDATE CASCADE,
    subject_id INTEGER REFERENCES subjects(id)
    	ON DELETE SET NULL
    	ON UPDATE CASCADE,
    grade DECIMAL(4, 2),
    date_received DATE
);