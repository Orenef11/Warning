import logging
from datetime import datetime
from pandas import ExcelWriter, DataFrame
from os import path

import global_variables


class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls.__instances[cls]


class WarningLogger(logging.Handler, metaclass=Singleton):
    def __init__(self, class_types_list: list):
        super(WarningLogger, self).__init__(global_variables.WARNING_TEST)
        self.__setting_logger()
        self.__system_obj_types_set = {key.lower() for key in class_types_list}
        self.HEADERS_CREATE = "Created"
        self.__csv_headers = [self.HEADERS_CREATE, "Class_Type", "Filename", "Func_Name", "Log_Level", "Line", "Module",
                              "File_Full_Path", "Message"]
        self.__df_data_list = []

    def __setting_logger(self) -> None:
        logger = logging.getLogger(self.__class__.__name__)
        logging.addLevelName(global_variables.WARNING_TEST, "WARNING_TEST")
        self.setLevel(global_variables.WARNING_TEST)
        logger.addHandler(self)
        global_variables.warning_handler_name = self.__class__.__name__

    def emit(self, record: logging.LogRecord) -> None:
        # record.message is the log message
        self.__parser_log_record(record)

    def __parser_log_record(self, record: logging.LogRecord) -> None:
        record_separators_list = [':', ',', '-', "->"]
        class_type, msg = None, record.msg.lower()

        for separator in record_separators_list:
            if separator in msg and msg.split(separator, maxsplit=1)[0] in self.__system_obj_types_set:
                class_type, msg = msg.split(separator, maxsplit=1)
                break

        if class_type is None:
            raise ValueError("Incorrect format: The supported format is from the following format\n"
                             "class type, separator ({}) and message.".format(record_separators_list))

        record_vars_list = [datetime.fromtimestamp(record.created), class_type, record.filename, record.funcName,
                            record.levelname, int(record.lineno), record.module, record.pathname, msg]
        self.__df_data_list.append(record_vars_list)

    def __create_df(self) -> DataFrame:
        return DataFrame(data=self.__df_data_list, columns=self.__csv_headers)

    def export_to_excel(self, file_path: str) -> None:
        excel_writer = ExcelWriter(file_path, engine="xlsxwriter")
        folder_path = path.split(file_path)[0]
        if folder_path != '' and not path.isdir(folder_path):
            raise NotADirectoryError(f"The folder does not exist in the following path: {folder_path}")
        self.__create_df().to_excel(excel_writer, index=False)

    def export_to_csv(self, file_path: str) -> None:
        folder_path = path.split(file_path)[0]
        if folder_path != '' and not path.isdir(folder_path):
            raise NotADirectoryError(f"The folder does not exist in the following path: {folder_path}")

        self.__create_df().to_csv(file_path, index=False)

