myBlog
==============

**Author**: [Lydia Mitchelle Makini](https://github.com/lydiah2015)
## Description
[myBlog](https://github.com/lydiah2015/myBlog.git) is a personal blogging website where you can create and share your opinions and other users can read and comment on them. 

Additionally, it displays random quotes to inspire your users. 


## Installation

### Requirements
* Python 3.6.5

### Cloning the repository
```bash
git clone https://github.com/lydiah2015/myBlog.git && cd myBlog
```

### Creating a virtual environment
```bash
sudo apt-get install python3.6-venv
python3.6 -m venv virtual
source virtual/bin/activate
```

### Installing dependencies
```bash
pip install -r requirements.txt
```

### Running Tests
```bash
python run.py test
```

### Running in development
```bash
python run.py runserver
```
Open the app on your browser, by default on `127.0.0.1:5000`.

### Deploying to heroku
- Make sure you have  `requirements.txt`
```bash
pip freeze > requirements.txt
```
- create a `Procfile` with the following content
```Procfile
web: gunicorn run:app 
```
- If **deploying for the first time**, make sure you have `heroku cli` installed then create app by running
```bash
heroku create appname
```
- Create Postgres addon
```bash
heroku addons:create heroku-postgresql:hobby-dev
```
- Make sure you have committed all changes then run
```bash
git push heroku master
```
- upgrade db to create tables on production database
```bash
heroku run python run.py db upgrade
```

## Live Demo

The web app can be accessed from the following link
[https://lydiah-blog.herokuapp.com/](https://lydiah-blog.herokuapp.com/)

## Technology used

* [Python3.6](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)

## Known Bugs 

There are no known bugs. If you find any be sure to create an issue 

## License ##
This project is licensed under the MIT Open Source license, (c) [ Lydia Mitchelle Makini](https://github.com/lydiah2015)