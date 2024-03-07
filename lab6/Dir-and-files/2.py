# os.F_OK - объект существует, 
# os.R_OK - доступен на чтение, 
# os.W_OK - доступен на запись, 
# os.X_OK - доступен на исполнение.
import os
print('Существование:', os.access('C:\Users\Admin\Desktop\pp2\lab6\Dir-and-files\check1_for1231', os.F_OK)) # False так как у меня нет файла check1_for2
print('Чтение доступно:', os.access('C:\Users\Admin\Desktop\pp2\lab6\Dir-and-files\check1_for1', os.R_OK))
print('Запись доступна:', os.access(__file__, os.W_OK))
print('Доступен на исполнение:', os.access(__file__, os.X_OK))