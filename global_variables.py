import logging

WARNING_TEST = logging.CRITICAL + 10
warning_handler_name = None


def warning_test(self, message, *args, **kws):
    # Yes, logger takes its '*args' as 'args'.
    if self.isEnabledFor(WARNING_TEST):
        self._log(WARNING_TEST, message, args, **kws)

