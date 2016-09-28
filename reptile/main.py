import os

from reptile.get_orignal_data import get_original_data
from reptile.downloadsrt import download_srt
# from formattxt import del_blankline
# from step2 import del_time
# from step3 import merge_line


# del_blankline("harry_cn4.srt", "new_session1.txt")
# del_time("new_session1.txt", "new_session1-1.txt")
# merge_line("new_session1-1.txt", "new_session1-2.txt")

# del_blankline("harry_en.srt", "new_session2.txt")
# del_time("new_session2.txt", "new_session2-1.txt")
# merge_line("new_session2-1.txt", "new_session2-2.txt")


if __name__ == '__main__':
    get_original_data()
    download_srt()

