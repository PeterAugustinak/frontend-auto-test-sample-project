# This is the engine for reading from Test Scenario spread sheets

# 3rd party imports
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class SpreadSheetReader:

    @staticmethod
    def open_sheet(name, sheet):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('frontend-auto-secret.json', scope)

        gc = gspread.authorize(credentials)
        sh = gc.open(name)
        worksheet = sh.worksheet(sheet)

        return worksheet

    @classmethod
    def read_data(cls, name, sheet, col_num,):

        worksheet = cls.open_sheet(name, sheet)

        value_list = worksheet.col_values(col_num)

        data = value_list[2:]
        return data

    @classmethod
    def read_info(cls, name, sheet, row_num, col_num):

        worksheet = cls.open_sheet(name, sheet)

        value = worksheet.cell(row_num, col_num).value

        return value






