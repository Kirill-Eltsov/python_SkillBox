SELECT MIN("Средняя оценка"), "Фамилия учителя" FROM
(
SELECT ROUND(AVG(ag.grade), 2) as "Средняя оценкa", t.full_name as "Фамилия учителя" FROM assignments_grades ag
JOIN assignments a ON a.assignment_id = ag.assignment_id
JOIN teachers t ON t.teacher_id = a.teacher_id
GROUP BY ag.assignment_id
)