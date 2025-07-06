from src.decorators import log


@log()
def hello_world():
    return "Hello, world!"


def test_success_hello_world(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert "hello_world start" in captured.out
    assert "hello_world result: Hello, world!" in captured.out
    assert "hello_world end" in captured.out


@log()
def fail_function(arg):
    raise Exception("Exception error")


def test_fail_function(capsys):
    try:
        fail_function(10)
    except Exception as e:
        assert str(e) == "Exception error"
    captured = capsys.readouterr()
    assert "fail_function start" in captured.out
    assert "fail_function error: Exception error. Inputs: (10,), {}" in captured.out
    assert "fail_function end" in captured.out


def test_file_logging():
    filename = "testlog.txt"

    @log(filename)
    def goodbye_mars():
        return "Goodbye, Mars!"

    goodbye_mars()
    with open(filename, "r") as f:
        result = f.read()
    assert "goodbye_mars start" in result
    assert "goodbye_mars result: Goodbye, Mars!" in result
    assert "goodbye_mars end" in result


def test_fail_file_logging():
    filename = "testlog.txt"

    @log(filename)
    def fail_mars(arg):
        raise Exception("Houston, we have a problem!!!")

    try:
        fail_mars(42)
    except Exception as e:
        assert str(e) == "Houston, we have a problem!!!"
    with open(filename, "r") as f:
        result = f.read()
    assert "fail_mars start" in result
    assert "fail_mars error: Houston, we have a problem!!!. Inputs: (42,), {}" in result
    assert "fail_mars end" in result
