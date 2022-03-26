import markdown
# import sys

SITE_NAME = 'CSarpAlex'
POST_NAME = 'post'

file_name = None

# args = sys.argv


while True:
    file_name = input('file: ')

    if file_name=='exit':
        break

    # открываем файл преобразуем его содержимое в HTML которое помещаем в переменную html
    with open(file_name, 'r') as f:
        text = f.read()

        with open('d:/!site/index.html', 'r') as theme_file:
            t = theme_file.read()

            html = markdown.markdown(text)
            page = t.replace('$site_name', SITE_NAME).replace('$post_name', POST_NAME).replace('$content', html)


            # записываем содержимое переменной html в файл
            with open(POST_NAME + '.html', 'w') as f:
                f.write(page)

            print('yes!')