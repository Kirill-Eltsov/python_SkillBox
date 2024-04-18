import subprocess


def process_count(username: str) -> int:
    args = ['ps', '-u', username, '-o', 'pid']
    process = subprocess.run(args, capture_output=True)
    list_processes = process.stdout.decode().splitlines()[1:]
    return len(list_processes)


def total_memory_usage(root_pid: int) -> float:
    args = ['ps', '--ppid', str(root_pid), '-o', '%mem=']
    process = subprocess.run(args, capture_output=True)
    list_processes = process.stdout.decode().splitlines()
    new_list = [float(i) for i in list_processes]
    return sum(new_list)


if __name__ == "__main__":
    count = process_count("user")
    print(f"Количество процессов, запущенных из под пользователя 'user': {count}")
    memory = total_memory_usage(1)
    print(f"Суммарное потребление памяти древа процессов с PPID=1: {memory}%")