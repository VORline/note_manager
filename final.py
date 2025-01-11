user_name = input('Введите имя пользователя - ')
title = input('Введите заголовок заметки - ')
subtitle1 = input('Первый подзаголовок- ')
subtitle2 = input('Второй подзаголовок- ')
subtitle3 = input('Третий подзаголовок- ')
subtitle = [subtitle1, subtitle2, subtitle3]
content = input('Введите описание заметки - ')
status = input('Выберите статус заметки (в процессе/готово) - ')
created_date = input('Введите дату создания заметки в формате 01.01.2025 - ')
issue_date = input('Введите дату выполнения заметки в формате 31.12.2025'
                   ' (если заметка в процессе, поставьте прочерк) - ')

note = {'Имя пользователя - ': {user_name},
        'Заголовок заметки - ': {title},
        'Подзаголовки - ': [subtitle1, subtitle2, subtitle3],
        'Описание заметки - ': {content},
        'Статус заметки - ' : {status},
        'Дата создания заметки - ' : {created_date},
        'Дата выполнения заметки - ' : {issue_date}
        }

for key, value in note.items():
    print(key, value)

# print(note)