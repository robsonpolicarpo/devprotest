from main.logg.level import Level
from main.logg.logger import log_message, get_last_line

FILENAME = 'application.log'


def test_level_info():
    msg = "Testing log INFO"
    log_message(FILENAME, Level.INFO, msg)
    lline = get_last_line(FILENAME)
    assert lline.__contains__(Level.INFO.value)
    assert lline.__contains__(msg)


def test_level_warn():
    msg = "Testing log WARN"
    log_message(FILENAME, Level.WARN, msg)
    lline = get_last_line(FILENAME)
    assert lline.__contains__(Level.WARN.value)
    assert lline.__contains__(msg)


def test_level_debug():
    msg = "Testing log DEBUG"
    log_message(FILENAME, Level.DEBUG, msg)
    lline = get_last_line(FILENAME)
    assert lline.__contains__(Level.DEBUG.value)
    assert lline.__contains__(msg)


def test_level_error():
    msg = "Testing log ERROR"
    log_message(FILENAME, Level.ERROR, msg)
    lline = get_last_line(FILENAME)
    assert lline.__contains__(Level.ERROR.value)
    assert lline.__contains__(msg)


def test_filename_empty_error():
    msg = "Testing log filename_empty"
    try:
        log_message("", Level.ERROR, msg)
    except Exception as e:
        assert str(e) == 'Please inform filename'


def test_filename_without_extension():
    msg = "Testing log without_extension"
    log_message("application", Level.INFO, msg)


def test_filename_without_level():
    msg = "Testing log attribute ERROR"
    try:
        log_message("application", None, msg)
    except AttributeError:
        pass


def test_filename_without_message():
    msg = ""
    try:
        log_message("test", Level.ERROR, msg)
    except Exception as e:
        assert str(e) == 'Please inform a message'
