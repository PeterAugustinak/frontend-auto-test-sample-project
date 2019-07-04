@echo off
cls
cmd /k "cd /d venv\Scripts & activate & cd /d    ..\..\src & python TestSuiteRunner.py test_suite_01_admin DEV CHROME"