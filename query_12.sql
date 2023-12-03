SELECT students.first_name, students.last_name, grades.grade, grades.date_received
FROM grades
JOIN students ON grades.student_id = students.id
JOIN subjects ON grades.subject_id = subjects.id
JOIN groups ON students.group_id = groups.id
WHERE subjects.id = 5
  AND groups.id = 1
ORDER BY grades.date_received DESC
LIMIT 1;