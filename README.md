# E-learning
<p>A learning system based on formalised teaching but with the help of electronic resources is known as E-learning. While teaching can be based in or out of the classrooms, the use of computers and the Internet forms the major component of E-learning. E-learning can also be termed as a network enabled transfer of skills and knowledge, and the delivery of education is made to a large number of recipients at the same or different times. Earlier, it was not accepted wholeheartedly as it was assumed that this system lacked the human element required in learning. </p>

### Technologies we used :
- Python framework Django .
- Django REST framework .
- PostgreSQL database .
### API documentation 
<p>https://documenter.getpostman.com/view/13014200/VUqypEHg</p>
### How to Install and Run the Project on windows :
- Create a virtual environment on the desktop, for example 'env' .
- write this command in CMD to create it :- ' virtualenv env ' .
- open folder 'env' and acvtivate virtualenv using this command : '.\Scripts\activate' .
- clone my project using this command : git clone "https://github.com/werdani/E-learning" .
- cd 'Blog' and install requirments using this command : pip install -r requirment.txt .
- now need to create database in PostgreSQL using this name 'E-learning' .
- 'USER': 'postgres', 'PASSWORD': 'postgres', 'HOST': 'localhost', 'PORT': '5432' .
- add this information in file 'setting.py' .
- need to makemigrations using this command in CMD : 'python manage.py makemigrations' .
- need to migrate using this command in CMD : 'python manage.py migrate' .
- now database is ready to add products, but now you need to create a superuser .
- to create superuser write this command in CMD: 'python mange.py createsuperuser' . 
