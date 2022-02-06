from os import listdir
from os.path import isfile, join
from typing import List, Optional

from code.constants import COUNTRY_LIST


def get_filenames_list(_dir: str) -> List:
    return [filename for filename in listdir(_dir) if isfile(join(_dir, filename))]


def get_translation_language(filename: str) -> Optional[str]:
    country_list = COUNTRY_LIST
    for country in country_list:
        if filename.find(country) > -1:
            return country
    return None
