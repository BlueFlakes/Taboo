# main start module
from controllers import main_controller
from data import data_loader

def main():
    # load data
    data_loader.load_data_from_files()

    # run application
    main_controller.start_controller()

    # save data
    data_loader.save_data_to_files()

if __name__ == '__main__':
    main()
