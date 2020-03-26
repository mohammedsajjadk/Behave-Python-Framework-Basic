<h2> Folder Structure</h2>

```
├───drivers
└───tests
    ├───acceptance
    │   ├───locators                 # Locators are stored here (mostly as tuple)
    │   │   └───base_page.py
    │   │   └───cookies_page.py
    │   │   └───home_page.py
    │   ├───page_model               # we will have the methods here which use the locators and return specific step (example., one method will return URL, one method will return the driver.find_element(email) etc.,
    │   │   └───base_page.py
    │   │   └───cookies_page.py
    │   │   └───home_page.py
    │   ├───steps                    # step definitions - we write the step definitions in this package. We will use the methods defined in "page_models"
    │   │   └───cookiePage.py
    │   │   └───homePage.py
    │   │   └───navigation.py
    └───facebook.feature             # feature file
```
<br><br>

<h2> Instructions </h2>
<li>Clone the repo (see Note before cloning)
<li>Install the below mentioned packages:
<li>Pip install selenium
<li>Pip install requests
<li>pip install behave

<h2> Note </h2>
<li>Your project folder should be where your Behave.exe exists. In my case, I have installed it globally on C:\ drive, hence I had to create my project on C:\. Reason behind this is, we will get an error if we are trying to run a feature file in PyCharm

<h2>Running a feature file(s) in Pycharm </h2>
<li>Open Run/Debug Configuration
<li>Click "+"
<li>Click "Python"
<li>Script path - Should be the folder where Behave.exe exists
<li>Parameters - Folder where you have your feature files
<li>Working Directory - Should be the folder where Behave.exe exists
