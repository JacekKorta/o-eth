from openpyxl import load_workbook
from openpyxl.styles import Font


def set_cell_colour(cell, colour):
    cell.font = Font(color=colour)


def change_workbook_colours(filename: str, colour) -> None:
    workbook = load_workbook(filename=filename)
    active_sheet = workbook.active
    for row in active_sheet.rows:
        for cell in row:
            set_cell_colour(cell, colour)

    workbook.save(filename=filename)
