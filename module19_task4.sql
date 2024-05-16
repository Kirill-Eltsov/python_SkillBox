SELECT min(expired), ROUND(AVG(expired)), MAX(expired) FROM
(
SELECT sg.group_id, count(ag.assignment_id) as expired
FROM students_group sg
JOIN assignments a on sg.group_id = a.group_id
JOIN assignments_grades ag on a.assignment_id = ag.assignment_id
WHERE ag.date > a.due_date
GROUP BY sg.group_id
)