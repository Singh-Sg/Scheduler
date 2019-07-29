# scheduler

Alfred Scheduler


Getting Started

	To work on the sample code, you'll need to clone project's repository to your local computer. If you haven't, do that first.

	bitbucket repo :

	git clone

	1)Create a Python virtual environment for your Django project. This virtual environment allows you to isolate this project and install any packages you need without affecting the system Python installation. At the terminal, type the following command:

		$ virtualenv -p python3.6 venv

	2)Activate the virtual environment:

		$ source venv/bin/activate

	3)Install Python dependencies for this project:

		$ pip install -r requirements.txt

	4)For Database schema:

		$ python manage.py migrate

	5)Create Super User

		$ python manage.py createsupersuer

	6)Start the Django development server:

		$ python manage.py runserver

	7)Run Celery
	    $ celery -A scheduler worker -l info

	8)Run Celery Beat
	    $ celery beat --pidfile= -A scheduler -l INFO




Step: Check async task to call this api:
     http://127.0.0.1:8000/api/weather/

     Output on the celery window:   {'coord': {'lon': -115.15, 'lat': 36.17}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 104.45, 'pressure': 1012, 'humidity': 5, 'temp_min': 99, 'temp_max': 107.01}, 'visibility': 16093, 'wind': {'speed': 4.7, 'deg': 130, 'gust': 5.1}, 'clouds': {'all': 1}, 'dt': 1563220425, 'sys': {'type': 1, 'id': 3527, 'message': 0.0073, 'country': 'US', 'sunrise': 1563194082, 'sunset': 1563245879}, 'timezone': -25200, 'id': 5506956, 'name': 'Las Vegas', 'cod': 200}


Step 2: Everyday 3:00 PM UTC Time zone schedule task will work



celery beat --pidfile= -A scheduler -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
