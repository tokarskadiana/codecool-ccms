import sys
sys.path.append('../home/diana/Codecool/python-ccms-team10-1')
from python-ccms-team10-1.model import User


class UserController:
    def __init__(self, user):
        '''
        Constructor of user controller.

        Arguments:user object
        '''
        pass

    #  Maybe must be in separate class
    def check_user_type(self):
        '''
        Check what type of user was loged in.

        Returns:class type
        '''
        pass

    def start_session(self):
        '''
        Create apropriate conntroller for user.

        Returns: controller object
        '''
        pass
