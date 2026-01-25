# pyravelry

[![Release](https://img.shields.io/github/v/release/theuerc/pyravelry)](https://img.shields.io/github/v/release/theuerc/pyravelry)
[![Build status](https://img.shields.io/github/actions/workflow/status/theuerc/pyravelry/main.yml?branch=main)](https://github.com/theuerc/pyravelry/actions/workflows/main.yml?query=branch%3Amain)
[![Commit activity](https://img.shields.io/github/commit-activity/m/theuerc/pyravelry)](https://img.shields.io/github/commit-activity/m/theuerc/pyravelry)
[![License](https://img.shields.io/github/license/theuerc/pyravelry)](https://img.shields.io/github/license/theuerc/pyravelry)

This is python wrapper for the Ravelry API (a database of knitting / crocheting patterns).

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

I've checked the API endpoints / models that are currently supported from the official [Ravelry Documentation](https://www.ravelry.com/api/). The crossed ones are not planned to ever be supported:

Endpoints:

- [x] /color_families
- [X] /current_user
- [x] /fiber_attributes
- [x] /fiber_categories
- [x] /search
- [x] /yarn_weights
- [ ] /app
- [ ] /bundled_items
- [ ] /bundles
- [ ] /carts
- [X] /comments
- [ ] /deliveries
- [ ] /designers
- [ ] /drafts
- [ ] /favorites
- [ ] /fiber
- [ ] /fiber_attributes_groups
- [ ] /forum_posts
- [ ] /forums
- [ ] /friends
- [ ] /groups
- [ ] /in_store_sales
- [ ] /languages
- [ ] /library
- [ ] /messages
- [ ] /needles
- [ ] /packs
- [ ] /pages
- [ ] /pattern_attributes
- [ ] /pattern_categories
- [ ] /pattern_source_types
- [ ] /pattern_sources
- [ ] /patterns
- [x] /people
- [ ] /photos
- [ ] /product_attachments
- [ ] /products
- [ ] /projects
- [ ] /queue
- [ ] /saved_searches
- [ ] /shops
- [ ] /stash
- [ ] /stores
- [ ] /topics
- [ ] /upload
- [ ] /volumes
- [x] /yarn_attributes
- [x] /yarn_companies
- [ ] /yarns
