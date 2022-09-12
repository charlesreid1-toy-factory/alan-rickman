import os
import unittest
from unittest import mock

from alan_rickman.gh import fetch

HERE = os.path.split(os.path.abspath(__file__))[0]


class TestFetchStandalone(unittest.TestCase):
    def test_fetch_standalone(self):
        """
        Test fetch(), the lone function in alan-rickman, in standalone mode.
        """

        # To test this in standalone mode,
        # We don't have to mock the actual request, which would be hard,
        # since that happens deep inside the PyGithub library.
        #
        # Instead, we can mock the Github class
        # so that when we call g.get_repo("...") it returns a dummy object
        # which has a dummy attribute git_url
        # that is returned by fetch()

        fake_git_url = "git@github.com:charlesreid1/five-letter-words-dummy-not-real"

        # Mock the Github object, so we can return our own
        # fake Repository class, instead of a real Repository
        with mock.patch("alan_rickman.gh.Github") as FakeGithub:
            # This is our fake Repository class
            class MockPyGithubRepo:
                def __init__(self):
                    self.git_url = fake_git_url

            # Now we need to swap out the Github.get_repo() function
            # with a MagicMock() object, which can return whatever we want.
            #
            # These do not work, as explained here:
            # https://stackoverflow.com/q/38199008
            #
            # FakeGithub.get_repo.return_value = MockPyGithubRepo()
            # FakeGithub.get_repo = mock.MagicMock(return_value=MockPyGithubRepo())
            #
            # These do work:
            FakeGithub().get_repo.return_value = MockPyGithubRepo()
            # This one is more explicit:
            # FakeGithub.return_value.get_repo.return_value = MockPyGithubRepo()
            git_url = fetch()
            self.assertGreater(len(git_url), 0)
            self.assertEqual(git_url, fake_git_url)
