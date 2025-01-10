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


print(f'Имя пользователя: {user_name}')
print(f'Заголовок заметки:  {title}')
print(f'Подзаголовки: {subtitle}')
print(f'Описание заметки:  {content}')
print(f'Статус заметки:  {status}')
print(f'Дата создания заметки: {created_date}')
print(f'Дата выполнения заметки: {issue_date}')

