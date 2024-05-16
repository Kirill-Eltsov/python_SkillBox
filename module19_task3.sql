SELECT full_name FROM students s WHERE group_id IN (
    SELECT group_id FROM students groups sg WHERE teacher_id = (
        SELECT teacher_id FROM (
            SELECT teacher_id, assignment_id, max(avg_score) as max_score FROM
            (
                SELECT a.teacher_id, ag.assisgnment_id, AVG(ag.grade)
                as avg_score
                FROM assignments_grades ag
                JOIN assignments a ON ag.assignment_id = a.assignment_id
                GROUP BY ag.assignment_id ORDER BY avg_score DESC
)))))