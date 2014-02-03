from flask.ext.script import Manager, Server
from flask.ext.migrate import MigrateCommand
from app import app

manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(
    use_debugger = True,
    use_reloader = True)
)

if __name__ == '__main__':
    manager.run()
