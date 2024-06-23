from pysimplerepl.models.exceptions import InvalidFlag
from pysimplerepl.models.exceptions import InsufficientArgsError
from unittest import TestCase

class InvalidFlagTests(TestCase):
    def test_invalid_flag_no_arg(self):
        with self.assertRaises(InvalidFlag) as err:
            raise InvalidFlag
        self.assertIsInstance(err.exception, ValueError)
        expected_message = 'invalid flag'
        self.assertEqual(
            expected_message,
            str(err.exception)
        )

    def test_invalid_flag_init_no_arg(self):
        with self.assertRaises(InvalidFlag) as err:
            raise InvalidFlag()
        self.assertIsInstance(err.exception, ValueError)
        expected_message = 'invalid flag'
        self.assertEqual(
            expected_message,
            str(err.exception)
        )

    def test_invalid_flag_message(self):
        expected_message = 'test invalid flag'
        with self.assertRaises(InvalidFlag) as err:
            raise InvalidFlag(expected_message)
        self.assertIsInstance(err.exception, ValueError)
        self.assertEqual(
            expected_message,
            str(err.exception)
        )


class InsufficientArgsErrorTest(TestCase):
    def test_insufficient_args_error(self):
        with self.assertRaises(InsufficientArgsError) as err:
            raise InsufficientArgsError
        self.assertIsInstance(err.exception, Exception)
