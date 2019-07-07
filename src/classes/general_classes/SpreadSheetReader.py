# This is the engine for manipulating data of Test Scenario spread sheets

# standard library imports
import os

# 3rd party imports
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class SpreadSheetReader:

    # this method opens spreadsheet with particular worksheet from google drive based on API credentials
    @staticmethod
    def open_sheet(name, sheet):
        file_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "fesp.json")
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(file_path, scope)

        gc = gspread.authorize(credentials)
        sh = gc.open(name)
        worksheet = sh.worksheet(sheet)

        return worksheet

    # this method reads data of all rows from 'data' worksheet of test scenario based on provided column number
    @classmethod
    def read_ts_data(cls, name, col_num):

        worksheet = cls.open_sheet(name, 'data')
        value_list = worksheet.col_values(col_num)
        data = value_list[2:]

        return data

    # this method reads value of cell from 'scenario' worksheet of test scenario based on provided row and column number
    @classmethod
    def read_ts_info(cls, name, row_num, col_num):

        worksheet = cls.open_sheet(name, 'scenario')
        value = worksheet.cell(row_num, col_num).value

        return value
