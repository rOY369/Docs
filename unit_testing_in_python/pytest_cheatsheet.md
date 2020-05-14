## Fixtures

### General
- `pytest --fixtures` on command line will give all built-in fixtures in pytest.
- `conftest.py` is used for defining test fixtures. It has a special meaning for pytest. It is considered as a local plugin. It can contain hook functions and fixtures which will be available to use in the same directory and the sub-directories.

### Built-in Fixtures 

### Test Runner

- `@pytest.mark.<marker_name>` used to mark a test case with a name. Example - `@pytest.mark.slow` to mark a test case, `python -m pytest -m "not slow"` to exclude the test case which has been marked as slow.
- `@pytest.mark.skip(reason=None)`  to exclude a test case to be run by the test runner.
- `@pytest.mark.skipif(condition,reason=None)`
- 

## Configuration

    [pytest]
    addopts = --strict
    markers = 
    	slow : Run tests that use sample data 

- `pytest.ini` is kept in the root folder of the project. This contains project wide pytest configuration which can change the behaviour of the test runner.
- `addopts = --strict` will only allow markers to be used that are specified in the `.ini` file.
- `markers = ` used for listing valid markers.

## Command Line

- `python -m pytest --markers` to list all available markers.
- `python -m pytest --doctest-modules` to will discover and execute all the doctests in the cwd. 
	- `python -m pytest --doctest-modules -o doctest_optionflags=IGNORE_EXCEPTION_DETAIL` to run doctest with any `doctest directive optionflag`. 

## Doctest

- [https://docs.python.org/3/library/doctest.html#option-flags](https://docs.python.org/3/library/doctest.html#option-flags)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjA0MDk0MzQ0Nl19
-->