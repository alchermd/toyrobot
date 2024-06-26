import logging
import unittest

logging.disable(logging.CRITICAL)

loader = unittest.TestLoader()
tests = loader.discover('tests', pattern='*tests.py')
testRunner = unittest.runner.TextTestRunner()
testRunner.run(tests)
