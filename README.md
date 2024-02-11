Install Python<br />
Install Pip<br />
Install PyTest `pip install -U pytest`<br />
Install pytest-selenium package `pip install pytest-selenium`</br>
Run Test `pytest`


Run tests in parallel
Install pytext-xdis `pip install selenium pytest pytest-xdist`
Run tests `pytest -n 4`
You can replace 4 with the number of workers you prefer

Run with html report
Install pytest-html `pip install pytest-html`
Run tests `pytest -n 4 --html=report.html`
Right click on `report.html` in project root
Click `reveal in file explorer`
Open with browser
![image](https://github.com/dyramcer/PyTest-Framework/assets/84975328/b02f9312-0a90-4171-ae91-8f47a6d39bc9)
