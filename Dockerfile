from python:3.9-slim

env PYTHONBUFFERED 1

copy requirements.txt requirements.txt
run pip install\
 --trusted-host pypi.org\
 --trusted-host files.pythonhosted.org\
 -r requirements.txt

run mkdir /src
add ./src /src
workdir /src

