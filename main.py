marks_dict = {'удовлетворительно': 3, 'хорошо': 4, 'отлично': 5}
example_marks_list = ['зачтено', 'удовлетворительно', 'хорошо', 'хорошо', 'удовлетворительно', 'отлично', 'зачтено',
                      'удовлетворительно', 'удовлетворительно']

marks_counter = 0
marks_sum = 0

for mark in example_marks_list:
    if mark in marks_dict.keys():
        marks_sum += marks_dict[mark]
        marks_counter += 1

print(f'Средний балл диплома {marks_sum/marks_counter:.2f}')
