Contributing
============

1. Fork it.

2. Clone it

create a `virtualenv <http://pypi.python.org/pypi/virtualenv>`__

.. code:: bash

    $ virtualenv develop              # Create virtual environment
    $ source develop/bin/activate     # Change default python to virtual one
    (develop)$ git clone https://github.com/tasdikrahman/vocabulary.git
    (develop)$ cd vocabulary
    (develop)$ pip install -r requirements.txt  # Install requirements for 'Vocabulary' in virtual environment

Or, if ``virtualenv`` is not installed on your system:

.. code:: bash

    $ wget https://raw.github.com/pypa/virtualenv/master/virtualenv.py
    $ python virtualenv.py develop    # Create virtual environment
    $ source develop/bin/activate     # Change default python to virtual one
    (develop)$ git clone https://github.com/tasdikrahman/vocabulary.git
    (develop)$ cd vocabulary
    (develop)$ pip install -r requirements.txt  # Install requirements for 'Vocabulary' in virtual environment

3. Create your feature branch (``$ git checkout -b my-new-awesome-feature``)

4. Commit your changes (``$ git commit -am 'Added <xyz> feature'``)

5. Run tests and validate that the code conforms to `PEP8 <https://www.python.org/dev/peps/pep-0008/>`__

.. code:: bash

    (develop) $ pytest --pep8

If everything is running fine, integrate your feature

6. Push to the branch (``$ git push origin my-new-awesome-feature``)

7. Create new Pull Request

Hack away!

To do
~~~~~

-  [X] Add translate module
-  [X] Add an option like `JSON=False` or `JSON=True` where the former returns a list object

Tests
~~~~~

``Vocabulary`` uses ``pytest`` for testing purposes.

Running the test cases

.. code:: bash

    $ pytest --pep8
    ========================== test session starts ==========================
    platform darwin -- Python 3.7.2, pytest-4.3.1, py-1.8.0, pluggy-0.9.0
    cachedir: .pytest_cache
    rootdir: /Users/mike/dev/vocabulary, inifile: pytest.ini
    plugins: pep8-1.0.6, mock-1.10.1
    collected 37 items

    setup.py PASSED                                                   [  2%]
    docs/conf.py PASSED                                               [  5%]
    tests/__init__.py PASSED                                          [  8%]
    tests/tests.py PASSED                                             [ 10%]
    tests/tests.py::TestModule::test_antonym_ant_key_error PASSED     [ 13%]
    tests/tests.py::TestModule::test_antonym_found PASSED             [ 16%]
    tests/tests.py::TestModule::test_antonym_not_found PASSED         [ 18%]
    tests/tests.py::TestModule::test_hyphenation_found PASSED         [ 21%]
    tests/tests.py::TestModule::test_hyphenation_not_found PASSED     [ 24%]
    tests/tests.py::TestModule::test_meaning_found PASSED             [ 27%]
    tests/tests.py::TestModule::test_meaning_key_error PASSED         [ 29%]
    tests/tests.py::TestModule::test_meaning_not_found PASSED         [ 32%]
    tests/tests.py::TestModule::test_partOfSpeech_found PASSED        [ 35%]
    tests/tests.py::TestModule::test_partOfSpeech_not_found PASSED    [ 37%]
    tests/tests.py::TestModule::test_pronunciation_found PASSED       [ 40%]
    tests/tests.py::TestModule::test_pronunciation_not_found PASSED   [ 43%]
    tests/tests.py::TestModule::test_respond_as_dict_1 PASSED         [ 45%]
    tests/tests.py::TestModule::test_respond_as_dict_2 PASSED         [ 48%]
    tests/tests.py::TestModule::test_respond_as_dict_3 PASSED         [ 51%]
    tests/tests.py::TestModule::test_respond_as_list_1 PASSED         [ 54%]
    tests/tests.py::TestModule::test_respond_as_list_2 PASSED         [ 56%]
    tests/tests.py::TestModule::test_respond_as_list_3 PASSED         [ 59%]
    tests/tests.py::TestModule::test_synonynm_empty_list PASSED       [ 62%]
    tests/tests.py::TestModule::test_synonynm_found PASSED            [ 64%]
    tests/tests.py::TestModule::test_synonynm_not_found PASSED        [ 67%]
    tests/tests.py::TestModule::test_synonynm_tuc_key_error PASSED    [ 70%]
    tests/tests.py::TestModule::test_translate_empty_list PASSED      [ 72%]
    tests/tests.py::TestModule::test_translate_found PASSED           [ 75%]
    tests/tests.py::TestModule::test_translate_not_found PASSED       [ 78%]
    tests/tests.py::TestModule::test_translate_tuc_key_error PASSED   [ 81%]
    tests/tests.py::TestModule::test_usageExample_empty_list PASSED   [ 83%]
    tests/tests.py::TestModule::test_usageExample_found PASSED        [ 86%]
    tests/tests.py::TestModule::test_usageExample_not_found PASSED    [ 89%]
    vocabulary/__init__.py PASSED                                     [ 91%]
    vocabulary/responselib.py PASSED                                  [ 94%]
    vocabulary/version.py PASSED                                      [ 97%]
    vocabulary/vocabulary.py PASSED                                   [100%]

    ======================= 37 passed in 0.25 seconds =======================

