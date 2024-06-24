# pyright: strict, reportPrivateUsage=false

from unittest import TestCase
from pysimplerepl.models import command


class CommandFlagTests(TestCase):
    short_simple = '-h'
    short_next_arg = 'world'
    short_next_arg_with_quote = '"hello world"'
    long_simple = '--hello'
    long_keyword = '--hello=world'
    not_a_flag = 'hello'

    def test__is_short_short(self):
        expected = True
        challenge = self.short_simple
        self.assertEqual(
            expected,
            command.CommandFlag._is_short(challenge),
            'short simple failed'
        )

    def test__is_short_long(self):
        expected = False
        challenge = self.long_simple
        self.assertEqual(
            expected,
            command.CommandFlag._is_short(challenge),
            'long simple failed'
        )

        challenge = self.long_keyword
        self.assertEqual(
            expected,
            command.CommandFlag._is_short(challenge),
            'long keyword failed'
        )
    
    def test__is_short_non_flag(self):
        expected = False
        challenge = self.not_a_flag
        self.assertEqual(
            expected,
            command.CommandFlag._is_short(challenge)
        )

    def test__is_long_short(self):
        expected = False
        challenge = self.short_simple
        self.assertEqual(
            expected,
            command.CommandFlag._is_long(challenge),
            'short simple failed'
        )

    def test__is_long_long(self):
        expected = True
        challenge = self.long_simple
        self.assertEqual(
            expected,
            command.CommandFlag._is_long(challenge),
            'long simple failed'
        )

        challenge = self.long_keyword
        self.assertEqual(
            expected,
            command.CommandFlag._is_long(challenge),
            'long keyword failed'
        )
    
    def test__is_long_non_flag(self):
        expected = False
        challenge = self.not_a_flag
        self.assertEqual(
            expected,
            command.CommandFlag._is_long(challenge)
        )

    def test__split_long_simple(self):
        expected = ('hello', None)
        challenge = self.long_simple
        self.assertEqual(
            expected,
            command.CommandFlag._split_long(
                challenge
            )
        )
    
    def test__split_long_keyword(self):
        expected = ('hello', 'world')
        challenge = self.long_keyword
        self.assertEqual(
            expected,
            command.CommandFlag._split_long(
                challenge
            )
        )

    def test__match_name_no_expected(self):
        expected = False
        flag = 'some_flag'
        flag_expected = None

        self.assertEqual(
            expected,
            command.CommandFlag._match_name(
                flag=flag,
                flag_expected=flag_expected
            )
        )
    
    def test__match_name_no_match(self):
        expected = False
        flag = 'some_flag'
        flag_expected = 'some_other_flag'

        self.assertEqual(
            expected,
            command.CommandFlag._match_name(
                flag=flag,
                flag_expected=flag_expected
            )
        )

    def test__match_name_subset_match(self):
        expected = False
        flag = 'some'
        flag_expected = 'some_flag'

        self.assertEqual(
            expected,
            command.CommandFlag._match_name(
                flag=flag,
                flag_expected=flag_expected
            )
        )

    def test__match_name_match(self):
        expected = True
        flag = 'some_flag'
        flag_expected = 'some_flag'

        self.assertEqual(
            expected,
            command.CommandFlag._match_name(
                flag=flag,
                flag_expected=flag_expected
            )
        )
    
    def test__parse_short_no_arg(self):
        expected = ('h', None)
        flag = self.short_simple
        next_token = None
        self.assertEqual(
            expected,
            command.CommandFlag._parse(
                flag_str=flag,
                next_token=next_token
            )
        )

    def test__parse_short_simple_arg(self):
        expected = ('h', self.short_next_arg)
        flag = self.short_simple
        next_token = self.short_next_arg
        self.assertEqual(
            expected,
            command.CommandFlag._parse(
                flag_str=flag,
                next_token=next_token
            )
        )

    def test__parse_short_quote_arg(self):
        expected = ('h', self.short_next_arg_with_quote)
        flag = self.short_simple
        next_token = self.short_next_arg_with_quote
        self.assertEqual(
            expected,
            command.CommandFlag._parse(
                flag_str=flag,
                next_token=next_token
            )
        )

    def test__parse_long_no_arg_no_next_token(self):
        expected = ('hello', None)
        flag = self.long_simple
        next_token = None
        self.assertEqual(
            expected,
            command.CommandFlag._parse(
                flag_str=flag,
                next_token=next_token
            )
        )

    def test__parse_long_arg_no_next_token(self):
        expected = ('hello', 'world')
        flag = self.long_keyword
        next_token = None
        self.assertEqual(
            expected,
            command.CommandFlag._parse(
                flag_str=flag,
                next_token=next_token
            )
        )

    def test__parse_long_no_arg_next_token(self):
        expected = ('hello', None)
        flag = self.long_simple
        next_token = 'ignore me'
        self.assertEqual(
            expected,
            command.CommandFlag._parse(
                flag_str=flag,
                next_token=next_token
            )
        )

    def test__parse_long_arg_next_token(self):
        expected = ('hello', 'world')
        flag = self.long_keyword
        next_token = 'ignore me'
        self.assertEqual(
            expected,
            command.CommandFlag._parse(
                flag_str=flag,
                next_token=next_token
            )
        )

    def test__parse_no_flag_next_token(self):
        expected = (None, None)
        flag = self.not_a_flag
        next_token = 'ignore me'
        self.assertEqual(
            expected,
            command.CommandFlag._parse(
                flag_str=flag,
                next_token=next_token
            )
        )

    def test__parse_no_flag_no_next_token(self):
        expected = (None, None)
        flag = self.not_a_flag
        next_token = None
        self.assertEqual(
            expected,
            command.CommandFlag._parse(
                flag_str=flag,
                next_token=next_token
            )
        )
