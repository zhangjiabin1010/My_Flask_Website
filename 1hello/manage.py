from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from niub import app
from models import Navigation,Menu,Article,User,Index
from exts import db



manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__ == "__main__":
    manager.run()

