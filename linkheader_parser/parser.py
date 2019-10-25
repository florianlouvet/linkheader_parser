from re import match, compile
from urllib.parse import parse_qsl, urlsplit

rlink = compile(r'<(.*?)>(.*?)rel="([A-z\s]*)"(.*?)(?:$|(?:,))')
assignations = compile(r'([A-z]*?)="(.*?)"')


def parse(link_header):
    links = {}
    for match in rlink.finditer(link_header):
        parsed_content = {}
        link = match.group(1)
        rel = match.group(3)
        parsed_content["url"] = link
        query_params = dict(parse_qsl(urlsplit(link).query))
        parsed_content = {**parsed_content, **query_params}
        extra = match.group(2)
        if match.group(4) is not None:
            extra += match.group(4)
        for a in assignations.finditer(extra):
            parsed_content[a.group(1)] = a.group(2)
        for r in rel.split(" "):
            links[r] = {**parsed_content, **{"rel": r}}
    return links
