def pytest_addoption(parser):
    parser.addoption('--os-name', default='linax', help='os name')