import json
from itertools import groupby

def task1() -> dict:
    count_log_levels = {'DEBUG': 0, 'INFO': 0, 'WARNING': 0, 'ERROR': 0, 'CRITICAL': 0}
    with open('skillbox_json_messages.log.json', 'r') as file:
        for line in file:
            log = json.loads(line.strip())
            level = log['level']
            if level in count_log_levels:
                count_log_levels[level] += 1
    return count_log_levels

def task2() -> int:
    hours = []
    with open('skillbox_json_messages.log.json', 'r') as file:
        for line in file:
            log = json.loads(line.strip())
            hours.append(log['time'][:2])
    hour_groups = [(key, len(list(group))) for key, group in groupby(sorted(hours))]
    max_hour = max(hour_groups, key=lambda x: x[1])
    return int(max_hour[0])

def task3() -> int:
    critical_logs_count = 0
    with open('skillbox_json_messages.log.json', 'r') as file:
        for line in file:
            log = json.loads(line.strip())
            if log['level'] == 'CRITICAL' and '05:00:00' <= log['time'] <= '05:20:00':
                critical_logs_count += 1
    return critical_logs_count

def task4() -> int:
    dog_messages_count = 0
    with open('skillbox_json_messages.log.json', 'r') as file:
        for line in file:
            log = json.loads(line.strip())
            if 'dog' in log['message']:
                dog_messages_count += 1
    return dog_messages_count

def task5() -> str:
    warning_messages = []
    with open('skillbox_json_messages.log.json', 'r') as file:
        for line in file:
            log = json.loads(line.strip())
            if log['level'] == 'WARNING':
                warning_messages.append(log['message'])
    words = [word for message in warning_messages for word in message.split()]
    if words:
        most_common_word = max(set(words), key=words.count)
        return most_common_word
    else:
        return "No warning messages found"


if __name__ == '__main__':
    tasks = [task1, task2, task3, task4, task5]
    for i, task_fun in enumerate(tasks, 1):
        task_answer = task_fun()
        print(f'{i}. {task_answer}')
