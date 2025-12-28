# pyravelry

[![Release](https://img.shields.io/github/v/release/theuerc/pyravelry)](https://img.shields.io/github/v/release/theuerc/pyravelry)
[![Build status](https://img.shields.io/github/actions/workflow/status/theuerc/pyravelry/main.yml?branch=main)](https://github.com/theuerc/pyravelry/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/theuerc/pyravelry/branch/main/graph/badge.svg)](https://codecov.io/gh/theuerc/pyravelry)
[![Commit activity](https://img.shields.io/github/commit-activity/m/theuerc/pyravelry)](https://img.shields.io/github/commit-activity/m/theuerc/pyravelry)
[![License](https://img.shields.io/github/license/theuerc/pyravelry)](https://img.shields.io/github/license/theuerc/pyravelry)

This is python wrapper for the Ravelry API, which is a database of knitting / crocheting patterns.

- **Github repository**: <https://github.com/theuerc/pyravelry/>
- **Documentation** <https://theuerc.github.io/pyravelry/>

Documentation for the Ravelry API--including how to get a http read-only API key--can be found here after logging in or making an account: https://www.ravelry.com/api

This is the list of endpoints I am working through:

- [x] /color_families
- [ ] /current_user
- [x] /fiber_attributes
- [x] /fiber_categories
- [x] /search
- [x] /yarn_weights
- [ ] /app (base level)
- [ ] /bundled_items (base level)
- [ ] /bundles (base level)
- [ ] /carts (base level)
- [ ] /comments (base level)
- [ ] /deliveries (base level)
- [ ] /designers (base level)
- [ ] /drafts (base level)
- [ ] /favorites (base level)
- [ ] /fiber (base level)
- [ ] /fiber_attributes_groups (base level)
- [ ] /forum_posts (base level)
- [ ] /forums (base level)
- [ ] friends (base level)

This is the list of pydantic models I am using for validating the output of the API:

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

---

Everything below this point will be deleted before the package is published.

### 1. Create a New Repository

First, create a repository on GitHub with the same name as this project, and then run the following commands:

```bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:theuerc/pyravelry.git
git push -u origin main
```

### 2. Set Up Your Development Environment

Then, install the environment and the pre-commit hooks with

```bash
make install
```

This will also generate your `uv.lock` file

### 3. Run the pre-commit hooks

Initially, the CI/CD pipeline might be failing due to formatting issues. To resolve those run:

```bash
uv run pre-commit run -a
```

### 4. Commit the changes

Lastly, commit the changes made by the two steps above to your repository.

```bash
git add .
git commit -m 'Fix formatting issues'
git push origin main
```

You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.

To finalize the set-up for publishing to PyPI, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/codecov/).

## Releasing a new version

- Create an API Token on [PyPI](https://pypi.org/).
- Add the API Token to your projects secrets with the name `PYPI_TOKEN` by visiting [this page](https://github.com/theuerc/pyravelry/settings/secrets/actions/new).
- Create a [new release](https://github.com/theuerc/pyravelry/releases/new) on Github.
- Create a new tag in the form `*.*.*`.

For more details, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/cicd/#how-to-trigger-a-release).

---

Repository initiated with [fpgmaas/cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv).
