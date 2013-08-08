import unittest
from hamcrest import *
from lib.params import parse_args


class test_arguments_parsing(unittest.TestCase):

    def test_default_secret_and_token_to_data_dir(self):
        argument = parse_args("")

        assert_that(argument.client_secrets, is_('data/client_secrets.json'))
        assert_that(argument.oauth_tokens, is_('data/tokens.dat'))