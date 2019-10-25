import unittest
from linkheader_parser.parser import parse


class TestParser(unittest.TestCase):
    def test_parsing_proper_link_header_with_next_and_last(self):
        link = (
            '<https://api.github.com/user/9287/repos?client_id=1&client_secret=2&page=2&per_page=100>; rel="next", '
            '<https://api.github.com/user/9287/repos?client_id=1&client_secret=2&page=3&per_page=100>; rel="last"'
        )
        expected = {
            "next": {
                "url": "https://api.github.com/user/9287/repos?client_id=1&client_secret=2&page=2&per_page=100",
                "rel": "next",
                "client_id": "1",
                "client_secret": "2",
                "page": "2",
                "per_page": "100"
            },
            "last": {
                "url": "https://api.github.com/user/9287/repos?client_id=1&client_secret=2&page=3&per_page=100",
                "rel": "last",
                "client_id": "1",
                "client_secret": "2",
                "page": "3",
                "per_page": "100"
            }
        }
        self.assertEqual(parse(link), expected)

    def test_parsing_proper_link_header_with_next_last_and_prev(self):
        link = (
            '<https://api.github.com/user/9287/repos?page=3&per_page=100>; rel="next", '
            '<https://api.github.com/user/9287/repos?page=1&per_page=100>; rel="prev", '
            '<https://api.github.com/user/9287/repos?page=5&per_page=100>; rel="last"'
        )
        expected = {
            "next": {
                "url": "https://api.github.com/user/9287/repos?page=3&per_page=100",
                "rel": "next",
                "page": "3",
                "per_page": "100"
            },
            "last": {
                "url": "https://api.github.com/user/9287/repos?page=5&per_page=100",
                "rel": "last",
                "page": "5",
                "per_page": "100"
            },
            "prev": {
                "url": "https://api.github.com/user/9287/repos?page=1&per_page=100",
                "rel": "prev",
                "page": "1",
                "per_page": "100"
            }
        }
        self.assertEqual(parse(link), expected)

    def test_parsing_empty_link_header(self):
        link = ""
        expected = {}
        self.assertEqual(parse(link), expected)

    def test_parsing_proper_link_header_with_next_and_a_link_without_rel(self):
        link = (
            '<https://api.github.com/user/9287/repos?page=3&per_page=100>; rel="next", '
            '<https://api.github.com/user/9287/repos?page=1&per_page=100>; pet="cat", '
        )
        expected = {
            "next": {
                "url": "https://api.github.com/user/9287/repos?page=3&per_page=100",
                "rel": "next",
                "page": "3",
                "per_page": "100"
            }
        }
        self.assertEqual(parse(link), expected)

    def test_parsing_proper_link_header_with_next_and_properties_besides_rel(self):
        link = '<https://api.github.com/user/9287/repos?page=3&per_page=100>; rel="next"; hello="world"; pet="cat"'
        expected = {
            "next": {
                "url": "https://api.github.com/user/9287/repos?page=3&per_page=100",
                "rel": "next",
                "page": "3",
                "per_page": "100",
                "hello": "world",
                "pet": "cat"
            }
        }
        self.assertEqual(parse(link), expected)

    def test_parsing_proper_link_header_with_a_comma_in_the_url(self):
        link = '<https://imaginary.url.notreal/?name=What,+me+worry>; rel="next";'
        expected = {
            "next": {
                "url": "https://imaginary.url.notreal/?name=What,+me+worry",
                "rel": "next",
                "name": "What, me worry"
            }
        }
        self.assertEqual(parse(link), expected)

    def test_parsing_proper_link_header_with_a_multiword_rel(self):
        link = '<https://imaginary.url.notreal/?name=What,+me+worry>; rel="next page";'
        expected = {
            "next": {
                "url": "https://imaginary.url.notreal/?name=What,+me+worry",
                "rel": "next",
                "name": "What, me worry"
            },
            "page": {
                "url": "https://imaginary.url.notreal/?name=What,+me+worry",
                "rel": "page",
                "name": "What, me worry"
            }
        }
        self.assertEqual(parse(link), expected)

    def test_parsing_proper_link_header_with_matrix_parameters(self):
        link = '<https://imaginary.url.notreal/segment;foo=bar;baz/item?name=What,+me+worry>; rel="next";'
        expected = {
            "next": {
                "url": "https://imaginary.url.notreal/segment;foo=bar;baz/item?name=What,+me+worry",
                "rel": "next",
                "name": "What, me worry"
            }
        }
        self.assertEqual(parse(link), expected)


if __name__ == "__main__":
    unittest.main()
