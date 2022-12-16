# CARD_CRM

## First start

* python3 -m venv venv 
* . ./venv/bin/activate
* pip3 install -t requirements.txt
* python card_crm/manage.py makemigrations
* python card_crm/manage.py migrate
* python card_crm/manage.py createsuperuser 
* python card_crm/manage.py runserver

DASHBOARD:
![image](https://github.com/samolin/card_crm/blob/main/readme_media/card_crm.gif)

Transcation restriction with lack of balance:
![image](https://github.com/samolin/card_crm/blob/main/readme_media/card_crm_admin.gif)


