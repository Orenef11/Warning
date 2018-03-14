import logging
from Modules import Warning

import global_variables

a = Warning.WarningLogger(["SSH", "DB", "SERVER"])

# x ,msg = "1:2:3:4".split(":",1)
# print(x,msg)
# exit()

# l = logging.getLogger(global_variables.warning_test_name)
# # And finally a test
# logging.critical('Test 1')
# logging.info('Test 2')
# logging.warning('Test 3')
# logging.error('Test 4')
# l.warning_test("ssh:Sdfsdf")
# l.warning_test("DB: fghfghfg")
# l.warning_test("SERVER:354345345")
# l.warning_test("ssh:ererttyuytiu")
# l.warning_test("SERVER:Sdfgnuykuyotfjsdf")
# l.warning_test("ssh:Sdfsdf")
# l.warning_test("DB:Sdfsdf")
#
# a.export_to_excel("report.xlsx")
# print()

#
# class WarningType():
#     pass
#
# class SshWarning(WarningType):
#     pass
#
# warning.add("sadsadsad", warn=SshWarning)