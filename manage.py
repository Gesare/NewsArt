from app import create_app
from flask_script import Manager,Server

# Creating app instance
app = create_app('development')

@manager.command
def test():
    '''
    Run the unit tests for the classes.
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=1).run(tests)

manager = Manager(app)
manager.add_command('server', Server)

if __name__ == '__main__':
    manager.run()