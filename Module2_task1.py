def get_summary_rss(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()[1:]

    total_rss = 0
    for line in lines:
        columns = line.split()
        rss = int(columns[5])
        total_rss += rss


    units = ['Б', 'Кб', 'Мб', 'Гб']
    unit_index = 0
    while total_rss >= 1024 and unit_index < len(units) - 1:
        total_rss /= 1024
        unit_index += 1

    return f'{total_rss:.0f} {units[unit_index]}'

if __name__ == '__main__':
    file_path = 'output_file.txt'
    summary_rss = get_summary_rss(file_path)
    print(summary_rss)
