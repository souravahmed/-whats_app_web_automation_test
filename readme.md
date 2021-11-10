# Whatsapp ui automation(web): 

## Project Description
This is a whatsapp ui automation(web) project.This project follow POM(page Object model) folder structure.

## Tech

Below are the libraries  used in this project:

- [Selenium] - popular web browser automation
- [Pytest] - testing framework
- [Openpyxl] - python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files

## Installation
First download chrome driver from [here](https://chromedriver.storage.googleapis.com/index.html?path=95.0.4638.69/). Extract using winRar. Driver should be in Downloads folder. Program will look for the driver in Downlaods folder inside chromedriver_win32 folder.
requirments.txt file has all the dependency.
To install all the dependency run below command after activating your virtualenv. follow below command

```sh
pip install -r /path/to/requirements.txt
```

## Excel File location

Inside project folder structure there is a folder name ExcelFile. Inside ExcelFile folder there is a file called mobile-numbers.xlsx. Open that file and enter a valid mobile number and save it.

## Run test

To run the test cases follow below command
```sh
pytest Tests\whats_app_page_test.py
```

