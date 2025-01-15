titles = []
i = 0
while True:
    title = input(f'Lобавьте заголовок №{i + 1}\n'
                  ' (Enter для отмены): ')
    i += 1
    if title == '':
        break
    titles.append(title)
    print('Вы ввели: ', title)
    if len(titles) == len(set(titles)):
        continue
    elif len(titles) != len(set(titles)):
        titles.pop(-1)
        print('Вы ввели повторяющийся заголовок!\n',
              'Он будет удалён: ', title)
print("Ваши заголовки: ")
print('\n'.join(titles))