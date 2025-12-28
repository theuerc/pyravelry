# pyravelry

[![Release](https://img.shields.io/github/v/release/theuerc/pyravelry)](https://img.shields.io/github/v/release/theuerc/pyravelry)
[![Build status](https://img.shields.io/github/actions/workflow/status/theuerc/pyravelry/main.yml?branch=main)](https://github.com/theuerc/pyravelry/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/theuerc/pyravelry/branch/main/graph/badge.svg)](https://codecov.io/gh/theuerc/pyravelry)
[![Commit activity](https://img.shields.io/github/commit-activity/m/theuerc/pyravelry)](https://img.shields.io/github/commit-activity/m/theuerc/pyravelry)
[![License](https://img.shields.io/github/license/theuerc/pyravelry)](https://img.shields.io/github/license/theuerc/pyravelry)

This is python wrapper for the Ravelry API (a database of knitting / crocheting patterns).

- **Github repository**: <https://github.com/theuerc/pyravelry/>
- **Documentation** <https://theuerc.github.io/pyravelry/>
- **Official Ravelry API Documentation** <https://www.ravelry.com/api>

Use of this API wrapper requires a [Ravelry Account](https://www.ravelry.com/) and a username and apikey as specified in the [HTTP Basic Auth](https://www.ravelry.com/api#authenticating) section of the Ravelry API Documentation.

Quick Start:

```bash
$pip install pyravelry
$python -i
>>> from pyravelry import Client, Settings
>>> settings = Settings(RAVELRY_USERNAME=..., RAVELRY_API_KEY=...)
>>> client = Client(settings=settings)
>>> results = client.search.query(query="merino", limit=10, types="Yarn")
>>> results[0].title
'MerinoSeide'
```

More information can be found in the [pyravelry documentation](https://theuerc.github.io/pyravelry/).
