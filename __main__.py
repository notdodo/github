"""Pulumi project to manage `notdodo` public repositories"""

import pulumi
import pulumi_github as github

# Create a GitHub repository
repository = github.Repository(
    "github",
    has_downloads=True,
    has_issues=True,
    has_projects=True,
    has_wiki=True,
    vulnerability_alerts=True,
)

repository = github.Repository(
    "test-removeme",
)
