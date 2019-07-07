<h2>FRONTEND-AUTO-TEST-SAMPLE-PROJECT (FESP)</h2>
<p>This is just a sample of how can Automation Tests could be introduced for any frontend project.</p>

<h2>Environment prerequisities</h2>
- Python 3.7.2. (https://www.python.org/downloads/release/python-372/)
- Firefox 67 or higher or/and<br/>
- Chrome 75

<h2>How to run tests</h2>
<p>All the necessary settings are done within the batch script (windows cmd settings, virtual environment activation,
test suite run with predefined parameters). There is Virtual Environment created for this project in /venv directory.
</p>

For run this project just follow these two steps:
- <b>edit python home path in pyvenv.cfg</b> file located in project /venv/ directory - change the path to your installation of python
(ex. C:\Users\user\AppData\Local\Programs\Python\Python37)
- run file <b>'testrunner.bat'</b>

<p>Current predefined parameters are for test_suite_fesp_01_admin, DEV environment and CHROME browser.
You can change them by editing the file.</p> 

<h2>Environment for the project</h2>
If above settings will not work, you have to do following steps to set environment for the project.
- install Python 3.7.2. (https://www.python.org/downloads/release/python-372/)
 
Install folowing 3rd party libraries:
- selenium<br/>
- request<br/>
- gspread<br/>
- oath2client<br/>
- colorama

- run 
Installation example:
python -m pip install requests

Project is runnig from script "<b><i>src/TestSuiteRunner.py</i></b>" with following (requiered) parameters:

[test suite] [ENV] [BROWSER]

Possible values:
- [test suite] = see Test Suite list in https://bit.ly/328X0GS
- [ENV] = "DEV", "STAG"
- [BROWSER] = "FIREFOX", "CHROME"

Examples: (only possibility for now is test_suite_fesp_01_admin & DEV & FIREFOX or CHROME):

<b>python -u src/TestSuiteRunner.py test_suite_fesp_01_admin DEV CHROME</b>

<h2>Project configuration</h2>
For configuration settings see:
<b><i>src/data/config.ini</i></b>

<h2>Owner / Contact Person</h2>
peter.augustinak@gmail.com
