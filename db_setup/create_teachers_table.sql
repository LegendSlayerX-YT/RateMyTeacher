-- Create schema if it doesn't exist
CREATE SCHEMA IF NOT EXISTS teacher_sch;

-- Create sequence for auto-incrementing id
CREATE SEQUENCE IF NOT EXISTS teacher_sch.teachers_id_seq;

-- Create teachers table
CREATE TABLE IF NOT EXISTS teacher_sch.teachers (
    id bigint NOT NULL DEFAULT nextval('teacher_sch.teachers_id_seq'::regclass),
    school_id integer,
    name character varying,
    email character varying,
    PRIMARY KEY (id)
);

-- Set the sequence owner
ALTER SEQUENCE teacher_sch.teachers_id_seq OWNED BY teacher_sch.teachers.id;
