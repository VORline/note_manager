user_name = input('Введите имя пользователя - ')
title = input('Введите заголовок заметки - ')
content = input('Введите описание заметки - ')
status = input('Выберите статус заметки (в процессе/готово) - ')
created_date = input('Введите дату создания заметки в формате 01.01.2025 - ')
issue_date = input('Введите дату выполнения заметки в формате 31.12.2025'
                   ' (если заметка в процессе, поставьте прочерк) - ')


print(f'Имя пользователя: {user_name}')
print(f'Заголовок заметки:  {title}')
print(f'Описание заметки:  {content}')
print(f'Статус заметки:  {status}')
print(f'Дата создания заметки: {created_date}')
print(f'Дата выполнения заметки: {issue_date}')
