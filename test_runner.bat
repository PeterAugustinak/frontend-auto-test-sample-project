@echo off
cls
START /MAX cmd /k "mode con cols=120 lines=80 && cd /d venv\Scripts & activate & cd /d    ..\..\src & python TestSuiteRunner.py test_suite_fesp_01_admin DEV FIREFOX & cd /d    ..\"
