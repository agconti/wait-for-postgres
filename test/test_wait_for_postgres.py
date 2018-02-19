import unittest
from unittest.mock import patch
from ..wait_for_postgres.wait import pg_is_ready


class WaitForPostgresTestcase(unittest.TestCase):

    @patch("psycopg2.connect")
    def pg_is_ready_returns_false_when_postgres_cannot_be_connected_to(self, mock_connect):
        mock_connect.return_value = False
        assert pg_is_ready() is False

    @patch("psycopg2.connect")
    def pg_is_ready_returns_true_when_postgres_is_able_to_accept_connections(self, mock_connect):
        mock_connect.return_value = True
        assert pg_is_ready() is True


if __name__ == '__main__':
    unittest.main()
