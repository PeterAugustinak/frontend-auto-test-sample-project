<b>***UPDATE!!! You don't need to edit python path in venv/pyenv.cfg. Just run testrunner.bat. Read below description ***</b><br/>

<h2>FRONTEND-AUTO-TEST-SAMPLE-PROJECT (FESP)</h2>
<p>This is just a sample of how can Automation Tests could be introduced for any frontend project.</p>

<h2>Environment prerequisities</h2>
- Python 3.7.2.<br/>
- Firefox 67 or higher or/and<br/>
- Chrome 75

<h2>How to run the project</h2>
- <b>install Python</b> 3.7.2 if you don't have (https://www.python.org/downloads/release/python-372/)</b><br/>
    
<h3>Automated procedure</h3>
- in root directory, run **testrunner.bat**<br/>
- _(this will setup complete environment for the project and run tests, in case environment is already created,
  just directly run tests)_
- for edit configuration (change test suite/environment/browser) of the tests, see below <b>"How to run tests"</b> 

<h3>Manual procedure</h3>
- _(in case of anything goes wrong with testrunner.bat)_<br/>
- create virtual environment for the project in (root) directory by **py -m venv venv-fesp**<br/>
- activate created virtual environment by run **activate.bat** in venv-fesp\Scripts <br/>
- install external libraries - back to root directory and **pip install -r requirements.txt**<br/>
- run tests by run TestSuiteRunner.py - see below <b>"How to run tests"</b><br/>
<br/>

<p>Current predefined parameters are for test_suite_fesp_01_admin, DEV environment and CHROME browser.
You can change them by editing the file.</p> 


<h2>How to run tests</h2>
Project is runnig from script "<b><i>src/TestSuiteRunner.py</i></b>" with following (requiered) parameters:<br/>
[test suite] [ENV] [BROWSER]</br>

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
