import sys

def get_mean_size():
    lines = sys.stdin.readlines()[1:]
    total_size = 0
    file_count = 0

    for line in lines:
        file_info = line.split()
        if len(file_info) >= 5:
            file_size = int(file_info[4])
            total_size += file_size
            file_count += 1

    if file_count > 0:
        mean_size = total_size / file_count
        print(mean_size)
    else:
        print("No files found.")

if __name__ == "__main__":
    get_mean_size()
