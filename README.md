# Dash-Flask Template Repository
This project was based on a repository [published by Todd Birchard](https://github.com/toddbirchard/plotlydash-flask-tutorial). For more information, check out the following links.

* **Tutorial**: https://hackersandslackers.com/plotly-dash-with-flask/
* **Demo**: https://plotlydashflask.hackersandslackers.app/


## Quick Start Guide

#### Installation
Builds are tested in Windows 10 x64 machines. To install the dependencies, use the `install.bat` script.

#### Local Deployment
To deploy the app on your local machine, use the `run.bat` script.


# Notes
To add a new dashboard, create a new `dashboardX.py` file in the `plotlydash` repository. Note you will need to change the value of `routes_pathname_prefix` in the instantiation of the Dash app. You will also need to change the name of the initialization function so that it can be imported and called within the `plotlydash\__init__.py` script.