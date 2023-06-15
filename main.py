import os

marks_dict = {'удовлетворительно': 3, 'хорошо': 4, 'отлично': 5}


def get_file_names(basic_path):
    names_list = []
    for root, dirs, files in os.walk(basic_path):
        for file in files:
            names_list.append(os.path.join(basic_path, file))
    return names_list


def get_path():
    path = '/\\Example files'
    return path


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        marks_list = f.read().split()
    return marks_list


def write_file():
    pass


def calculate_avg_mark(marks_list):
    marks_counter = 0
    marks_sum = 0

    for mark in marks_list:
        if mark in marks_dict.keys():
            marks_sum += marks_dict[mark]
            marks_counter += 1
    avg_mark = marks_sum / marks_counter
    return f'{avg_mark:.2f}'


current_path = get_path()
names = get_file_names(current_path)
for name in names:
    print(calculate_avg_mark(read_file(name)))
