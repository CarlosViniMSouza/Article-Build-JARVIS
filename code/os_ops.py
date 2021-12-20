import os
import subprocess as sp

paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'Visual Studio': "C:\\Program Files (x86)\\Microsoft Visual Studio\\Installer\\setup",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_notepad():
    os.startfile(paths['notepad'])


def open_discord():
    os.startfile(paths['Visual Studio'])


def open_cmd():
    os.system('cmd inicial')


def open_calculator():
    sp.Popen(paths['calculator'])
