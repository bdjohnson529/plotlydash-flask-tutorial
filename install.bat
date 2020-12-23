:: virtual environment
:: for some reason installation does not work on some machines
call conda remove -y -n plotlydash --all
call conda create -y -n plotlydash python
call activate plotlydash

:: install requirements
call pip install -r requirements.txt