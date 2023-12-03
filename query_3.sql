SELECT students.group_id, AVG(grades.grade) AS avg_grade
FROM grades
JOIN students ON grades.student_id = students.id
WHERE grades.subject_id = 5
GROUP BY students.group_id;