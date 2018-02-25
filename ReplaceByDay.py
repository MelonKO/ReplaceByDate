# coding=utf-8

import os
import datetime
import re
import calendar

class PhotoFile(object):

    def __init__(self, name: str, path: str, date: datetime = datetime.datetime(1,1,1)):
        self.name = name
        self.path = path
        self.date = date


def ReCreateFile():
    newdir_path_by_year = path + "\\" + str(MyPhoto[i].date.year)
    if (os.path.exists(newdir_path_by_year) == False):
        os.mkdir(newdir_path_by_year)
    newdir_path_by_month = newdir_path_by_year + "\\" + str(calendar.month_name[MyPhoto[i].date.month])
    if (os.path.exists(newdir_path_by_month) == False):
        os.mkdir(newdir_path_by_month)
    newdir_path_by_day = newdir_path_by_month + "\\" + str(MyPhoto[i].date.date())
    if (os.path.exists(newdir_path_by_day) == False):
        os.mkdir(newdir_path_by_day)
    j = int(1)
    # запихивает файлы в папку с датой и переименовывает
    for elem in support_list:
        print("Пишу файл", elem)
        if os.path.exists(newdir_path_by_day + "\\" + str(MyPhoto[i].date.date()) + "_" + str(j) + "."
                          + pattern.search(elem).group(0)) == False:
            os.rename(elem, newdir_path_by_day + "\\" + str(MyPhoto[i].date.date()) + "_" + str(j) + "."
                      + pattern.search(elem).group(0))
        else:
            while os.path.exists(newdir_path_by_day + "\\" + str(MyPhoto[i].date.date()) + "_" + str(j) + "."
                                 + pattern.search(elem).group(0)) == True:
                j += 1
            os.rename(elem,
                      newdir_path_by_day + "\\" + str(MyPhoto[i].date.date()) + "_" + str(j) + "." + pattern.search(
                          elem).group(0))
    j += 1

print("Укажите путь к директории (папке) для сортировки: ")
path = input()

all_files = os.listdir(path)
pattern = re.compile("png|jpg|jpeg|nef|raw", re.IGNORECASE)
files_name = []
for file in all_files:
    result = pattern.search(file)
    if(result != None):
        files_name.append(file)
    else:
        print(result)
#список файлов директории "path"
MyPhoto = [PhotoFile(name=name,path=path +"\\"+ name, date= datetime.datetime.fromtimestamp(
    os.path.getmtime(path +"\\"+name)))
           for name in files_name]
#сортируем
for i in range(len(MyPhoto)):
    for j in range(i, 0, -1):
        if (MyPhoto[j].date <= MyPhoto[j - 1].date):
            MyPhoto[j], MyPhoto[j - 1] = MyPhoto[j - 1], MyPhoto[j]
#пробуем выделить нужные папки по дням
support_list=[] #в этот массив запишем пути к файлам, которые переместим в созданную папку
print(MyPhoto.__len__()) #количество файлов в директории
#сортируем по папочкам
for i in range(0, MyPhoto.__len__()):
    print(i)
    support_list.append(MyPhoto[i].path)
    if(i != MyPhoto.__len__()-1):
        if(MyPhoto[i+1].date.date() != MyPhoto[i].date.date()):
            ReCreateFile()
            support_list.clear()
    else:
        ReCreateFile()
        support_list.clear()
        break