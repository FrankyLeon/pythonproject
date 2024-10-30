## 1. Introduction

This is backend project which interact with MetaMarket's smart contracts.  
Production (BSC): https://metamarket.click 
Staging (BSC testnet): https://testnet.metamarket.click

## 2. Requirements

Python 3.7 or higher.

## 3. How to run the project

1. `cd` into the project and then run `virtualenv venv`
    run at win10_OS terminal: `python -m venv venv`

2. Run `source venv/bin/activate`
    run at win10_OS terminal: `venv\Scripts\activate`

3. Run `pip install -r requirements.txt`
4. Install Ganache by running `python setup_ganache.py`
5. Run `python manage.py migrate`
6. (optional) Run `python manage.py createsuperuser`
7. Run `python manage.py runserver`