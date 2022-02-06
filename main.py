from code.file_handler import get_filenames_list, get_translation_language
from code.sheet_handler import copy_column, find_column
from config import get_settings
from code.constants import CountryMapper


def main():
    settings = get_settings()
    files = get_filenames_list(settings.work_dir)
    for filename in files:
        if translation_language := get_translation_language(filename):
            header_value = CountryMapper[translation_language].value
            header_column_name = find_column(settings.result_filename, header_value)
            copy_column(filename, settings.result_filename, header_column_name, settings.work_dir)


if __name__ == "__main__":
    main()
