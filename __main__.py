"""Pulumi project to manage `notdodo` public repositories"""

import pulumi_github as github

github_repo = github.Repository(
    "github",
    name="github",
    has_downloads=True,
    has_issues=True,
    has_projects=True,
    has_wiki=True,
    vulnerability_alerts=True,
)
oidc_sub_customization_template = (
    github.ActionsRepositoryOidcSubjectClaimCustomizationTemplate(
        f"{github_repo.name}-oidc-sub-customization",
        repository=github_repo.name,
        use_default=False,
        include_claim_keys=[
            "actor",
            "context",
            "repository_owner",
        ],
    )
)

erfiume_repo = github.Repository(
    "erfiume-bot",
    name="erfiume_bot",
    has_downloads=True,
    has_issues=True,
    has_projects=False,
    has_wiki=False,
    vulnerability_alerts=True,
    allow_squash_merge=True,
)
oidc_sub_customization_template = (
    github.ActionsRepositoryOidcSubjectClaimCustomizationTemplate(
        f"{erfiume_repo.name}-oidc-sub-customization",
        repository=erfiume_repo.name,
        use_default=False,
        include_claim_keys=[
            "actor",
            "context",
            "repository_owner",
        ],
    )
)
