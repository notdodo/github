"""Pulumi project to manage `notdodo` public repositories"""

import pulumi_github as github

from notdodo_github import PublicRepository

github_repo = PublicRepository(
    name="github",
)
oidc_sub_customization_template = (
    github.ActionsRepositoryOidcSubjectClaimCustomizationTemplate(
        "github-repo-oidc-sub-customization",
        repository=github_repo.name,
        use_default=False,
        include_claim_keys=[
            "repo",
            "context",
            "job_workflow_ref",
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
        "erfiume-repo-oidc-sub-customization",
        repository=erfiume_repo.name,
        use_default=False,
        include_claim_keys=[
            "repo",
            "context",
            "job_workflow_ref",
        ],
    )
)

name = "github-actions"
gha_repo = github.Repository(
    name,
    name=name,
    allow_merge_commit=False,
    allow_update_branch=True,
    delete_branch_on_merge=True,
    has_downloads=True,
    has_issues=True,
    has_projects=True,
    merge_commit_message="PR_BODY",
    merge_commit_title="PR_TITLE",
    squash_merge_commit_message="BLANK",
    squash_merge_commit_title="PR_TITLE",
    vulnerability_alerts=True,
    # has_wiki=False,
    # vulnerability_alerts=True,
    # allow_squash_merge=True,
)
oidc_sub_customization_template = (
    github.ActionsRepositoryOidcSubjectClaimCustomizationTemplate(
        f"{name}-repo-oidc-sub-customization",
        repository=gha_repo.name,
        use_default=True,
        # include_claim_keys=[
        #     "repo",
        #     "context",
        #     "job_workflow_ref",
        # ],
    )
)


name = "notdodo"
notdodo_repo = github.Repository(
    name,
    name=name,
    allow_merge_commit=True,
    allow_update_branch=False,
    delete_branch_on_merge=False,
    description="About",
    has_wiki=True,
    has_downloads=True,
    has_issues=True,
    has_projects=True,
    merge_commit_message="PR_TITLE",
    merge_commit_title="MERGE_MESSAGE",
    squash_merge_commit_message="COMMIT_MESSAGES",
    squash_merge_commit_title="COMMIT_OR_PR_TITLE",
    vulnerability_alerts=False,
    # vulnerability_alerts=True,
    # allow_squash_merge=True,
)
oidc_sub_customization_template = (
    github.ActionsRepositoryOidcSubjectClaimCustomizationTemplate(
        f"{name}-repo-oidc-sub-customization",
        repository=notdodo_repo.name,
        use_default=True,
        # include_claim_keys=[
        #     "repo",
        #     "context",
        #     "job_workflow_ref",
        # ],
    )
)


name = "pulumi-k8s"
pulumi_k8s_repo = github.Repository(
    name,
    name=name,
    allow_merge_commit=True,
    allow_update_branch=False,
    delete_branch_on_merge=True,
    description="Pulumi deployments for Kubernetes",
    has_downloads=True,
    has_issues=True,
    has_projects=True,
    has_wiki=True,
    merge_commit_message="PR_TITLE",
    merge_commit_title="MERGE_MESSAGE",
    squash_merge_commit_message="COMMIT_MESSAGES",
    squash_merge_commit_title="COMMIT_OR_PR_TITLE",
    vulnerability_alerts=True,
    topics=[
        "infrastructure-as-code",
        "kubernetes",
        "kubernetes-cluster",
        "pulumi",
        "security",
    ],
    # vulnerability_alerts=True,
    # allow_squash_merge=True,
)
oidc_sub_customization_template = (
    github.ActionsRepositoryOidcSubjectClaimCustomizationTemplate(
        f"{name}-repo-oidc-sub-customization",
        repository=pulumi_k8s_repo.name,
        use_default=True,
        # include_claim_keys=[
        #     "repo",
        #     "context",
        #     "job_workflow_ref",
        # ],
    )
)


name = "sparktrail"
sparktrail_repo = github.Repository(
    name,
    name=name,
    allow_merge_commit=True,
    allow_update_branch=False,
    delete_branch_on_merge=True,
    description="Query AWS CloudTrail using Spark (python) to perform analysis",
    has_downloads=True,
    has_issues=True,
    has_projects=True,
    has_wiki=True,
    merge_commit_message="PR_TITLE",
    merge_commit_title="MERGE_MESSAGE",
    squash_merge_commit_message="COMMIT_MESSAGES",
    squash_merge_commit_title="COMMIT_OR_PR_TITLE",
    vulnerability_alerts=True,
    # vulnerability_alerts=True,
    # allow_squash_merge=True,
)
oidc_sub_customization_template = (
    github.ActionsRepositoryOidcSubjectClaimCustomizationTemplate(
        f"{name}-repo-oidc-sub-customization",
        repository=sparktrail_repo.name,
        use_default=True,
        # include_claim_keys=[
        #     "repo",
        #     "context",
        #     "job_workflow_ref",
        # ],
    )
)

name = "tools"
tools_repo = github.Repository(
    name,
    name=name,
    allow_merge_commit=True,
    allow_update_branch=False,
    delete_branch_on_merge=True,
    description="List of tools",
    has_downloads=True,
    has_issues=True,
    has_projects=False,
    has_wiki=False,
    merge_commit_message="PR_TITLE",
    merge_commit_title="MERGE_MESSAGE",
    squash_merge_commit_message="COMMIT_MESSAGES",
    squash_merge_commit_title="COMMIT_OR_PR_TITLE",
    vulnerability_alerts=True,
    # vulnerability_alerts=True,
    # allow_squash_merge=True,
)
oidc_sub_customization_template = (
    github.ActionsRepositoryOidcSubjectClaimCustomizationTemplate(
        f"{name}-repo-oidc-sub-customization",
        repository=tools_repo.name,
        use_default=True,
        # include_claim_keys=[
        #     "repo",
        #     "context",
        #     "job_workflow_ref",
        # ],
    )
)

name = "bingokta"
bingokta_repo = github.Repository(
    name,
    name=name,
    allow_merge_commit=False,
    allow_update_branch=True,
    delete_branch_on_merge=True,
    description="Bingo with Okta, but in Colombia",
    has_downloads=True,
    has_issues=True,
    has_projects=False,
    has_wiki=True,
    merge_commit_message="PR_TITLE",
    merge_commit_title="MERGE_MESSAGE",
    squash_merge_commit_message="COMMIT_MESSAGES",
    squash_merge_commit_title="PR_TITLE",
    vulnerability_alerts=True,
    # vulnerability_alerts=True,
    # allow_squash_merge=True,
)
oidc_sub_customization_template = (
    github.ActionsRepositoryOidcSubjectClaimCustomizationTemplate(
        f"{name}-repo-oidc-sub-customization",
        repository=bingokta_repo.name,
        use_default=True,
        # include_claim_keys=[
        #     "repo",
        #     "context",
        #     "job_workflow_ref",
        # ],
    )
)

name = "iamme-iamme"
iamme_repo = github.Repository(
    name,
    name="IAMme-IAMme",
    allow_merge_commit=False,
    allow_update_branch=True,
    delete_branch_on_merge=True,
    description="IAMme is a tool designed to visualize the connections between entities within an Okta tenant",
    has_downloads=True,
    has_issues=True,
    has_projects=False,
    has_wiki=False,
    merge_commit_message="PR_TITLE",
    merge_commit_title="MERGE_MESSAGE",
    squash_merge_commit_message="COMMIT_MESSAGES",
    squash_merge_commit_title="PR_TITLE",
    vulnerability_alerts=True,
    web_commit_signoff_required=True,
    # vulnerability_alerts=True,
    # allow_squash_merge=True,
)
oidc_sub_customization_template = (
    github.ActionsRepositoryOidcSubjectClaimCustomizationTemplate(
        f"{name}-repo-oidc-sub-customization",
        repository=iamme_repo.name,
        use_default=True,
        # include_claim_keys=[
        #     "repo",
        #     "context",
        #     "job_workflow_ref",
        # ],
    )
)

name = "goflat"
goflat_repo = github.Repository(
    name,
    name=name,
    allow_merge_commit=False,
    allow_update_branch=True,
    delete_branch_on_merge=True,
    description="Flatten complex JSON structures to a one-dimensional map (JSON key/value).",
    has_downloads=True,
    has_issues=True,
    has_projects=False,
    has_wiki=False,
    merge_commit_message="PR_TITLE",
    merge_commit_title="MERGE_MESSAGE",
    squash_merge_commit_message="COMMIT_MESSAGES",
    squash_merge_commit_title="COMMIT_OR_PR_TITLE",
    vulnerability_alerts=True,
    web_commit_signoff_required=False,
    # vulnerability_alerts=True,
    # allow_squash_merge=True,
)
oidc_sub_customization_template = (
    github.ActionsRepositoryOidcSubjectClaimCustomizationTemplate(
        f"{name}-repo-oidc-sub-customization",
        repository=goflat_repo.name,
        use_default=True,
        # include_claim_keys=[
        #     "repo",
        #     "context",
        #     "job_workflow_ref",
        # ],
    )
)
