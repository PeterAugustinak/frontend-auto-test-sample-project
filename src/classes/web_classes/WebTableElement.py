# This is the engine which handles data in web table


class WebTableElement:
    def __init__(self, web_table):
        self.table = web_table

    # get row count without header
    def get_row_count(self):
        return len(self.table.find_elements_by_tag_name("tr")) - 1

    def get_column_count(self):
        return len(self.table.find_elements_by_xpath("//tr[2]/td"))

    def get_table_size(self):
        return {"rows": self.get_row_count(),
                "columns": self.get_column_count()}

    def row_data(self, row_number):
        if row_number == 0:
            raise Exception("Row number starts from 1")

        # row_number = row_number + 1
        row = self.table.find_elements_by_xpath(f"//tr[{row_number}]/td")
        row_data = []
        for value in row:
            row_data.append(value.text)

        return row_data

    def column_data(self, col_number):
        col = self.table.find_elements_by_xpath(f"//tr/td[{col_number}]")
        col_data = []
        for data in col:
            col_data.append(data.text)
        return col_data

    def get_all_data(self):
        # get number of rows
        nr_of_rows = len(self.table.find_elements_by_xpath("//tr")) - 1
        # get number of columns
        nr_of_cols = len(self.table.find_elements_by_xpath("//tr[2]/td"))
        all_data = []
        # iterate over the rows, to ignore the headers we have started the i with '1'
        for i in range(1, nr_of_rows + 1):
            # reset the row data every time
            ro = []
            # iterate over columns
            for j in range(1, nr_of_cols + 1):
                # get text from the i th row and j th column
                ro.append(self.table.find_element_by_xpath(f"//tr[{i}]/td[{j}]").text)

            # add the row data to all_data of the self.table
            all_data.append(ro)

        return all_data

    def presence_of_data(self, data):

        # verify the data by getting the size of the element matches based on the text/data passed
        data_size = len(self.table.find_elements_by_xpath(f"//td[normalize-space(text())='{data}']"))
        presence = False
        if data_size > 0:
            presence = True
        return presence

    def get_cell_data(self, column_number, row_number):
        if row_number == 0:
            raise Exception("Row number starts from 1")

        cell_value = self.table.find_element_by_xpath(f"//tr[{row_number}]/td[{column_number}]")

        return cell_value
