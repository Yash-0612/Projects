# classes - template
# object - instance of the class
# DRY - do not repeat yourself


class Student():
    pass

Proton = Student()
Electron = Student()

# print(Proton)
# print(Electron)

Proton.name = "Proton"
Proton.std = 12
Proton.section = 1


Electron.name = "Electron"
Electron.std = 11
Electron.section = 3


print(Proton.name)
print(Electron.name)