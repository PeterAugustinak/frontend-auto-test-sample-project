@echo off
cls

ECHO ****PYTHON VERSION CHECK****
python.exe --version >NUL 2>&1
IF NOT ErrorLevel 1 GOTO PythonOk

FOR /F "tokens=1,2" %%G IN ('"python.exe -V 2>&1"') DO ECHO %%H | find "3.7" > Nul
IF NOT ErrorLevel 1 GOTO PythonOk

FOR /F "tokens=1,2" %%G IN ('"python.exe -V 2>&1"') DO ECHO %%H | find "3.8" > Nul
IF NOT ErrorLevel 1 GOTO PythonOk

FOR /F "tokens=1,2" %%G IN ('"python.exe -V 2>&1"') DO ECHO %%H | find "3.9" > Nul
IF NOT ErrorLevel 1 GOTO PythonOk

ECHO You need Python 3.7 or higher. Please download, install and then restart this script.
goto :exit

:PythonOk
ECHO Python version OK!


IF EXIST venv-fesp (
START /MAX cmd /k "mode con cols=145 lines=80 && cd /d venv-fesp\Scripts & activate & cd /d    ..\..\src & python TestSuiteRunner.py test_suite_fesp_01_admin DEV CHROME & cd /d    ..\"
) ELSE (
START /MAX cmd /k "mode con cols=145 lines=80 && echo **** Installing environment for the project ***** & py -m venv venv-fesp & cd /d venv-fesp\Scripts & activate & cd /d ..\..\ & python -m pip install --upgrade pip & pip install -r requirements.txt & cls & cd /d    src & python TestSuiteRunner.py test_suite_fesp_01_admin DEV CHROME & cd /d    ..\"
)

:exit
ECHO Python version check done!
cmd /k
