import base64



class User:
    """
    This class representing User class
    """

    def __init__(self, id, password, first_name, last_name, telephone="", mail=""):
        """
        Constructs User object
        :param id: (int) store of id of User object
        :param password: (str) store of password of User object
        :param first_name: (str) store of first name of User object
        :param last_name: (str) store of last name of User object
        :param telephone: (str) store of phone number of User object
        :param mail: (str) store of e-mail address of User object
        """
        self.id = id
        self.username = '{}.{}'.format(first_name.lower(), last_name.lower())
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.telephone = telephone
        self.mail = mail

    def full_name(self):
        """
        Retuns full name of user.
        return: str(full name)
        """
        return "{} {}".format(self.first_name, self.last_name)

    @staticmethod
    def encodeBase64(password):
        """
        Static method to encode user password
        :param password: (str) password
        :return: (str) encoded password
        """
        encoded_pwd = base64.encodebytes(password.encode())
        encoded_pwd = str(encoded_pwd)
        return encoded_pwd

    @staticmethod
    def decodeBase64(password):
        """
        Static method for decoding encoded password
        :param password: (str) encoded password
        :return: decoded password
        """
        passwd_striped = password.replace('\\n', '')
        passwd = passwd_striped[2:]
        passwd_striped = password.replace('\\n', '')
        passwd = passwd_striped[2:]
        passwd = passwd[:-1]
        passwd = passwd.encode()
        decoded_pwd = base64.standard_b64decode(passwd).decode()
        return decoded_pwd
