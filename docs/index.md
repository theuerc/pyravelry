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
- [ ] ~~/current_user~~
- [x] /fiber_attributes
- [x] /fiber_categories
- [x] /search
- [x] /yarn_weights
- [ ] ~~/app (base level)~~
- [ ] /bundled_items (base level)
- [ ] /bundles (base level)
- [ ] ~~/carts (base level)~~
- [ ] ~~/comments (base level)~~ # doesn't allow retrieval of anyone else's comments.
- [ ] ~~/deliveries (base level)~~
- [ ] /designers (base level)
- [ ] ~~/drafts (base level)~~
- [ ] ~~/favorites (base level)~~
- [ ] /fiber (base level)
- [ ] /fiber_attributes_groups (base level)
- [ ] /forum_posts (base level)
- [ ] /forums (base level)
- [ ] ~~/friends (base level)~~
- [ ] /groups
- [ ] ~~/in_store_sales~~
- [ ] /languages
- [ ] ~~/library~~
- [ ] ~~/messages~~
- [ ] /needles
- [ ] ~~/packs~~
- [ ] /pages
- [ ] /pattern_attributes
- [ ] /pattern_categories
- [ ] /pattern_source_types
- [ ] /pattern_sources
- [ ] /patterns
- [ ] /people
- [ ] /photos
- [ ] /product_attachments
- [ ] /products
- [ ] /projects
- [ ] ~~/queue~~
- [ ] ~~/saved_searches~~
- [ ] ~~/shops~~
- [ ] ~~/stash~~
- [ ] /stores
- [ ] /topics
- [ ] /upload
- [ ] /volumes
- [ ] /yarn_attributes
- [x] /yarn_companies
- [ ] /yarns

Models:

- [ ] Activity
- [ ] Ad
- [ ] AttributeGroup
- [ ] Bookmark
- [ ] Bundle
- [ ] BundledItem
- [ ] Business
- [ ] Cart
- [ ] CartItem
- [ ] Collection
- [x] ColorFamily
- [x] Colorway
- [ ] CombinedCart
- [ ] ComponentYarn
- [x] Craft
- [ ] Delivery
- [ ] Document
- [ ] DownloadLink
- [ ] DraftComponentYarn
- [ ] DraftErrataLink
- [ ] DraftNeedleSize
- [ ] DraftPattern
- [ ] DraftPatternYarn
- [x] FiberAttribute
- [x] FiberAttributeGroup
- [x] FiberCategory
- [ ] FiberPack
- [ ] FiberStash
- [x] FiberType
- [ ] Forum
- [ ] ForumPost
- [ ] ForumPreference
- [ ] ForumSet
- [ ] ForumStatisticSummary
- [ ] Friendship
- [ ] Group
- [ ] InStoreSale
- [ ] Invoice
- [ ] InvoiceLineItem
- [ ] Language
- [ ] Message
- [ ] NeedleRecord
- [ ] NeedleSize
- [ ] NeedleType
- [ ] Pack
- [ ] Pattern
- [ ] PatternAttribute
- [ ] PatternAuthor
- [ ] PatternCategory
- [ ] PatternClassification
- [ ] PatternLanguage
- [ ] PatternNeedleSize
- [ ] PatternSource
- [ ] PatternSourceType
- [ ] PatternTagging
- [x] Photo
- [ ] Printing
- [ ] Product
- [ ] ProductAttachment
- [ ] ProductNotification
- [ ] Project
- [ ] ProjectStatus
- [ ] QueuedProject
- [ ] QueuedStash
- [ ] Saleable
- [ ] SavedSearch
- [ ] Shop
- [ ] ShopCustomer
- [ ] ShopSchedule
- [ ] SocialSite
- [ ] Stash
- [ ] StashStatus
- [ ] Store
- [ ] Tool
- [ ] Topic
- [ ] UnifiedStash
- [ ] User
- [ ] UserSite
- [ ] Volume
- [ ] VolumeAttachment
- [x] Yarn
- [x] YarnAttributeGroup
- [x] YarnCompany
- [x] YarnCountry
- [x] YarnFiber
- [x] YarnProvenance
- [x] YarnWeight
