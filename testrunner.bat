@echo off
cls
START /MAX cmd /k "mode con cols=110 lines=65 && cd /d venv\Scripts & activate & cd /d    ..\..\src & python TestSuiteRunner.py test_suite_fesp_01_admin DEV CHROME & cd /d    ..\"
