# Backend-Panel
Admin Panel for backend<br/>

## Steps for execution<br/>
1.) Create a virtual environment after cloning the repository<br/>
2.) Activate the virtual environment by: source venv/bin/activate <br/>
3.) Install all the requirements in the requirements.txt by: pip3 install -r requirements.txt <br/>
4.) Make sure you have Postgres installed and make changes to the name,password and host in the settings.py file as per your convenience <br/>
5.) Migrate the migrations files by : python3 manage.py migrate <br/>
6.) Create a superuser who can make changes in the database by: python3 manage.py createsuperuser <br/>
7.) Run the server by: python3 manage.py runserver <br/>
8.) Go to http://localhost:8000/admin/ and login with the super user credentials to make changes in the tables <br/>
9.) Go to http://localhost:8000/api/login/ to login with a normal user <br/>
10.) Go to http://localhost:8000/api/register/ to signup <br/>
