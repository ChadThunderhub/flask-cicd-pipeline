import pytest 

from aheflask.code import credentials_string

class TestGroup():
    @pytest.fixture
    def fixt(self) -> str:
        """This fixture will only be available within the scope of TestGroup"""
        return "Janko Muzykant"

    def test_credentials(self, fixt: str) -> None:
        left = credentials_string(fixt)
        right = str("(c) %s" % fixt)
        assert(left == right)
