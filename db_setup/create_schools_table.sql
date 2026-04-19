-- Create schema if it doesn't exist
CREATE SCHEMA IF NOT EXISTS teacher_sch;

-- Create sequence for auto-incrementing id
CREATE SEQUENCE IF NOT EXISTS teacher_sch.schools_id_seq;

-- Create schools table
CREATE TABLE IF NOT EXISTS teacher_sch.schools (
    id bigint NOT NULL DEFAULT nextval('teacher_sch.schools_id_seq'::regclass),
    name character varying,
    country character varying,
    state character varying,
    city character varying,
    zip_code character varying,
    address character varying,
    grade_level character varying,
    PRIMARY KEY (id)
);

-- Set the sequence owner
ALTER SEQUENCE teacher_sch.schools_id_seq OWNED BY teacher_sch.schools.id;
