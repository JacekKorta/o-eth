from os.path import join

from code.arguments import get_args
from code.colour_handler import change_workbook_colours
from code.file_handler import get_filenames_list, get_translation_language
from code.translation_handler import copy_column, find_column
from code.constants import CountryMapper
from config import get_settings


settings = get_settings()


def translate():
    files = get_filenames_list(settings.work_dir)
    for filename in files:
        if translation_language := get_translation_language(filename):
            header_value = CountryMapper[translation_language].value
            header_column_name = find_column(header_value, settings)
            if all([filename, settings.result_filename, header_column_name, settings.work_dir]):
                copy_column(filename, header_column_name, settings)
            else:
                print(filename, settings.result_filename, header_column_name, settings.work_dir)


def change_colour():
    files = get_filenames_list(settings.work_dir)
    filenames = [join(settings.work_dir, filename) for filename in files]
    for file in filenames:
        change_workbook_colours(file, settings.color)


if __name__ == "__main__":
    args = get_args()
    if args.mode == "translate":
        print("Translation handling")
        translate()
    elif args.mode == "colour":
        print("Changing cells colours")
        change_colour()
