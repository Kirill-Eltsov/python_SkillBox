SELECT ag.assignment_id, ROUND(AVG(ag.grade), 2) as "Средняя оценка где нужно прочитать или выучить"
FROM assignments_grades ag WHERE ag.assignment_id IN
(
SELECT a.assisgnment_id FROM assignments a
WHERE a.assignment_text LIKE '%прочитать%' OR a.assignment_text LIKE '%выучить%'
)
GROUP BY ag.assignment_id