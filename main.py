# main start module
from controllers import main_controller
from data import data_loader

def main():
    data_loader.load_data_from_files()

    main_controller.start_controller()

    data_loader.save_data_to_files()

if __name__ == '__main__':
    main()
