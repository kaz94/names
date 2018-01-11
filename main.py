
from utils.util import get_data_dir
from utils.readers import read, read_us_by_state, read_files, read_france_by_dep, read_sweden, read_england
from utils.constants import *


def main():
    data_dir = get_data_dir()
    # us_df = read(data_dir / USA / 'yob1880.txt')
    # us_df_by_state = read_us_by_state(data_dir / USA_BY_STATE / 'AK.TXT')
    # print(us_df)
    # print(us_df_by_state)
    # print(read_files(str(data_dir / USA), read))
    # print(read_files(str(data_dir / USA_BY_STATE), read_us_by_state))
    # print(read_france_by_dep(data_dir / FRANCE[0]))
    # print(read_sweden(data_dir, SWEDEN))
    print(read_england(data_dir, ENGLAND_AND_WALES))

if __name__ == '__main__':
    main()



