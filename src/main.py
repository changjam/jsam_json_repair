from utils.JsonRepair import JsonRepair
from utils.error_format import *

if __name__ == '__main__':
    repairer = JsonRepair(ERROR_FORMAT5)
    print(repairer.repair())