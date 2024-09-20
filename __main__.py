"""Pulumi project to manage `notdodo` public repositories"""

import pulumi_github as github

github.Repository(
    "github",
    has_downloads=True,
    has_issues=True,
    has_projects=True,
    has_wiki=True,
    vulnerability_alerts=True,
)

github.Repository(
    "erfiume-bot",
    name="erfiume_bot",
    has_downloads=True,
    has_issues=True,
    has_projects=False,
    has_wiki=False,
    vulnerability_alerts=True,
    allow_squash_merge=True,
)
