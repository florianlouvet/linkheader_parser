# linkheader_parser

This is a parser for HTTP link header. This package does not cover 100% of the RFC definition of LinkHeaders, but should work in 99% of common cases.

Please report any issue on github.

## Install package:
```
pip install linkheader_parser
```

## Usage:

```python
from linkheader_parser import parse

link_header = (
    '<https://api.github.com/user/9287/repos?client_id=1&client_secret=2&page=2&per_page=100>; rel="next", <https://api.github.com/user/9287/repos?client_id=1&client_secret=2&page=3&per_page=100>; rel="last"'
)

result = parse(link_header)
```

**Result:**

```

```
