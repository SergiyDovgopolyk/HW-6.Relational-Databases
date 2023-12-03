SELECT subjects.subject_name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
WHERE grades.student_id = 14
  AND subjects.teacher_id = 2;