titles = [] #список для ввода заголовоков
i = 0 #бесконечный цикл
while True:
    title = input(f'Добавьте заголовок №{i + 1}\n'
                  ' (Enter для отмены): ')
    i += 1
    # условие для остановки программы
    if title == '':
        break
    titles.append(title)
    print('Вы ввели: ', title) #отображение введенного значения
    if len(titles) == len(set(titles)):
        continue
    elif len(titles) != len(set(titles)):
        titles.pop(-1)
        print('Вы ввели повторяющийся заголовок!\n',
              'Он будет удалён: ', title)
print("Ваши заголовки: ") #вывод всех введенных заголовоков
print('\n'.join(titles))