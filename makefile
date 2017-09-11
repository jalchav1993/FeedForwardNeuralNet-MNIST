# make
TEST_PATH=./

clean-pyc:
    find . -name '*.pyc' -exec rm --force {} +
    find . -name '*.pyo' -exec rm --force {} +
    find . -name '*~' -exec rm --force  {} +

clean-build:
    rm --force --recursive build/
    rm --force --recursive dist/
    rm --force --recursive *.egg-info

test: clean-pyc
    py.test --verbose --color=yes $(TEST_PATH)

run:
    python manage.py runserver
