"""
Tests for the :func:`dicom_parser.utils.mime_generator.generate_by_mime`
utility function.
"""
import platform
from typing import Generator
from unittest import TestCase

import pytest
from dicom_parser.utils.mime_generator import generate_by_mime

from tests.fixtures import TEST_MIME_SERIES_PATH

#: Message to display for Linux and macOS tests.
WINDOWS_RUN: str = "Mime type generation is not supported in Windows."

#: Message to display for Windows only tests.
NON_WINDOWS_RUN: str = "Windows-specific tests."

#: Whether the current platform OS is Windows or not.
RUNNING_ON_WINDOWS: bool = platform.system() == "Windows"


# TODO: Fix windows test. For some reason NotImplementedError isn't raised
# when tested with GitHub Actions.
#
# @pytest.mark.skipif(not RUNNING_ON_WINDOWS, reason=NON_WINDOWS_RUN)
# class WindowsMimeGeneratorTestCase(TestCase):
#     """
#     Windows-specific tests (where libmagic and python-magic are not
#     available).
#     """

#     def test_notimplemetederror_raised(self):
#         """
#         Tests generation by mime type on Windows raises a RuntimeError.
#         """
#         with self.assertRaises(NotImplementedError):
#             generate_by_mime(TEST_MIME_SERIES_PATH)


@pytest.mark.skipif(RUNNING_ON_WINDOWS, reason=WINDOWS_RUN)
class MimeGeneratorTestCase(TestCase):
    """
    Tests for Linux and macOS.
    """

    def setUp(self):
        """
        Create a base sample generator available for each test.
        """
        self.generator = generate_by_mime(TEST_MIME_SERIES_PATH)

    def test_return_type(self):
        """
        Tests the returned object is a generator instance.
        """
        self.assertIsInstance(self.generator, Generator)

    def test_number_of_files(self):
        """
        Checks that the generator generates the expected number of files.
        """
        n_images = len(list(self.generator))
        expected = 3
        self.assertEqual(n_images, expected)
