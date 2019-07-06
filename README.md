<h2>FRONTEND-AUTO-TEST-SAMPLE-PROJECT</h2>
<p>This is just a sample of how can Automation Tests could be introduced for any frontend project.</p>

<h2>Environment prerequisities</h2>
- Firefox 67 or higher
- Chrome 75

<h2>How to run tests</h2>
<p>All the necessary settings are done within the batch script (windows cmd settings, virtual environment activation,
test suite run with predefined parameters). You don't need to have installed Python in you machine.</p>

<p>Just run file <b>'test_runner.bat'</b></p>

<p>Current predefined parameters are for test_suite_01_admin, DEv environment and FIREFOX browser.
You can change them by editing the file.</p> 

<h2>Environment for the project</h2>
There is Virtual Environment created for this project in /venv directory. It uses Python 3.7. 
and folowing 3rd party libraries:
- selenium
- request
- gspread
- oath2client
- colorama

Installation example:
python -m pip install requests

<h2>Project configuration</h2>
For configuration settings see:
<b><i>src/data/config.ini</i></b>

<h2>How to run tests manually</h2>
Project is runnig from script "<b><i>src/TestSuiteRunner.py</i></b>" with following (requiered) parameters:

[test suite] [ENV] [BROWSER]

Possible values:
- [test suite] = see Test Suite list
- [ENV] = "DEV", "STAG"
- [BROWSER] = "FIREFOX", "CHROME"

Examples:
- python -u src/TestSuiteRunner.py test_suite_01_admin DEV CHROME

<h2>Owner / Contact Person</h2>
peter.augustinak@gmail.com
