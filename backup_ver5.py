import zipfile
import time
import os

# 1. Файлы и каталоги,которые необходимо скопировать, собираются в список.
sourse = ['"C:\\test_file1"','"C:\\test_file2"']

# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'C:\\backup_test'
# 3. Файлы помещаются в zip-архив.
# 4. Текущая дата служит именем подкаталога в основном каталоге.
today = target_dir + os.sep + time.strftime('%Y_%m_%d')
# Текущее время служит именем zip-архива.
now = time.strftime('%H%M%S')

# Запрашиваем комментарий пользователя для имени файла.
comment = input('Введите комментарий --> ')
if len(comment) == 0: # проверяем, введен ли комментарий
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' +\
    comment.replace(' ', '_')+ '.zip'

# Создаём каталог, если его ещё нет
if not os.path.exists(today):
    os.mkdir(today)  # создание каталога
print('Каталог успешно создан', today)

archive = zipfile.ZipFile(target,'w') #,compression=zipfile.ZIP_DEFLATED

archDirName = ''
for dir, subdirs, files in os.walk("C:\\test_file1"):
        print('Добавление файлов из директории %s...' % (dir))
        # Имя текущей директории в архиве
        archDirName = '/'.join([archDirName, os.path.basename(dir)]).strip('/')
        # Добавить в архив текущую директорию
        archive.write(dir, archDirName)

        # Добавить в архив все файлы из текущей директории
        for file in files:
            # Имя текущего файла в архиве
            archFileName = archDirName + '/' + file
            archive.write(os.path.join(dir, file), archFileName)

archDirName2 = ''
for dir, subdirs, files in os.walk("C:\\test_file2"):
        print('Добавление файлов из директории %s...' % (dir))
        # Имя текущей директории в архиве
        archDirName2 = '/'.join([archDirName2, os.path.basename(dir)]).strip('/')
        # Добавить в архив текущую директорию
        archive.write(dir, archDirName2)

        # Добавить в архив все файлы из текущей директории
        for file in files:
            # Имя текущего файла в архиве
            archFileName2 = archDirName2 + '/' + file
            archive.write(os.path.join(dir, file), archFileName2)

