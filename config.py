from dataclasses import dataclass


@dataclass
class Settings:
    work_dir: str = r""
    result_filename: str = r""
    header_row_number: int = 2
    translation_column_name: str = "C"
    color: str = "00000000"  # black


def get_settings():
    return Settings()
