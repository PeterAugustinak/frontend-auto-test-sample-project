@echo off
cls

IF EXIST venv-fesp (
START /MAX cmd /k "mode con cols=145 lines=80 && cd /d venv-fesp\Scripts & activate & cd /d    ..\..\src & python TestSuiteRunner.py test_suite_fesp_01_admin DEV CHROME & cd /d    ..\"
) ELSE (
START /MAX cmd /k "mode con cols=145 lines=80 && echo **** Installing environment for the project ***** & py -m venv venv-fesp & cd /d venv-fesp\Scripts & activate & cd /d ..\..\..\frontend-auto-test-sample-project & python -m pip install --upgrade pip & pip install -r requierements.txt & cls & cd /d    src & python TestSuiteRunner.py test_suite_fesp_01_admin DEV CHROME & cd /d    ..\"
)