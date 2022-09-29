import tomllib
import pprint

with open("pyproject.toml", "rb") as f:
    data = tomllib.load(f)

pprint.pprint(data)
