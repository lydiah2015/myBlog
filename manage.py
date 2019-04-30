from app import create_app,db
from flask_script import Manager, Server
from flask_migrate import Migrate,MigrateCommand
from app.models import User,Post,Comment

app=create_app("development")

manager=Manager(app)
manager.add_command("runserver",Server(use_debugger=True))
migrate=Migrate(app,db)
manager.add_command("db",MigrateCommand)

@manager.command
def test():
    import unittest
    tests= unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@manager.command
def create_writer():
    from config import Config
    try:
        u=User(username=Config.WRITER_USERNAME,passwd=Config.WRITER_PASSWORD,writer=True)
        db.session.add(u)
        db.session.commit()
    except Exception as e:
        pass

if __name__=="__main__":
    manager.run()