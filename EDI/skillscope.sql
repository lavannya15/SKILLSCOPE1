-- =========================================
-- 1. Drop old tables (if exist)
-- =========================================
DROP TABLE IF EXISTS job_skills;
DROP TABLE IF EXISTS skills;
DROP TABLE IF EXISTS jobs;

-- =========================================
-- 2. Create jobs table
-- =========================================
CREATE TABLE jobs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    company VARCHAR(255),
    posted_date DATE
);

-- =========================================
-- 3. Create skills table
-- =========================================
CREATE TABLE skills (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

-- =========================================
-- 4. Create job_skills bridge table
-- =========================================
CREATE TABLE job_skills (
    job_id INT REFERENCES jobs(id) ON DELETE CASCADE,
    skill_id INT REFERENCES skills(id) ON DELETE CASCADE,
    PRIMARY KEY (job_id, skill_id)
);

-- =========================================
-- 5. Insert jobs
-- =========================================
INSERT INTO jobs (title, company, posted_date)
VALUES
('Data Analyst', 'Google', '2025-08-22'),
('Machine Learning Engineer', 'Microsoft', '2025-08-20');

-- =========================================
-- 6. Insert skills
-- =========================================
INSERT INTO skills (name)
VALUES
('SQL'), ('Python'), ('Excel'), ('TensorFlow'), ('Azure');

-- =========================================
-- 7. Link jobs to skills
-- =========================================
-- Data Analyst → SQL, Python, Excel
INSERT INTO job_skills (job_id, skill_id)
VALUES
(1, 1), -- SQL
(1, 2), -- Python
(1, 3); -- Excel

-- Machine Learning Engineer → Python, TensorFlow, Azure
INSERT INTO job_skills (job_id, skill_id)
VALUES
(2, 2), -- Python
(2, 4), -- TensorFlow
(2, 5); -- Azure

-- =========================================
-- 8. Example Query: Find jobs requiring Python
-- =========================================
SELECT j.title, j.company, j.posted_date
FROM jobs j
JOIN job_skills js ON j.id = js.job_id
JOIN skills s ON js.skill_id = s.id
WHERE s.name = 'Python';
