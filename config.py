from dataclasses import dataclass


@dataclass
class Settings:
    work_dir: str = r"D:\Wlasne\olga\translations-excel\materialy\markus"
    result_filename: str = r"D:\Wlasne\olga\translations-excel\materialy\markus\result.xlsx"
    header_row_number: int = 2
    translation_column_name: str = "C"


def get_settings():
    return Settings()
