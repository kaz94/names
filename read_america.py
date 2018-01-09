
from utils.util import get_data_dir
from utils.readers import read, read_by_state, join_files
from utils.constants import *


def main():
    data_dir = get_data_dir()
    us_df = read(data_dir / USA / 'yob1880.txt')
    us_df_by_state = read_by_state(data_dir / USA_BY_STATE / 'AK.TXT')
    print(us_df)
    print(us_df_by_state)
    print(join_files(str(data_dir / USA)))

if __name__ == '__main__':
    main()



