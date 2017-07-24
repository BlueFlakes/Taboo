# main start module
from controllers import registration_controller
from models.registration_code import RegistrationCode

def main():
    RegistrationCode.add_code(['ST123456', '1111-11-11'])
    registration_controller.start_controller()


if __name__ == '__main__':
    main()
