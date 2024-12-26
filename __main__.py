"""Pulumi project to manage `notdodo` public repositories"""


from notdodo_github import PublicRepository

PublicRepository(
    name="github",
    oidc_claims=[
        "repo",
        "context",
        "job_workflow_ref",
    ],
    topics=[
        "pulumi",
        "iac",
        "github",
    ],
)

PublicRepository(
    name="erfiume_bot",
    oidc_claims=[
        "repo",
        "context",
        "job_workflow_ref",
    ],
)

PublicRepository(
    name="github-actions",
)

PublicRepository(
    name="notdodo",
    description="About",
)


PublicRepository(
    name="pulumi-k8s",
    description="Pulumi deployments for Kubernetes",
    topics=[
        "infrastructure-as-code",
        "kubernetes",
        "kubernetes-cluster",
        "pulumi",
        "security",
    ],
)


PublicRepository(
    name="sparktrail",
    description="Query AWS CloudTrail using Spark (python) to perform analysis",
)

PublicRepository(
    name="tools",
    description="List of tools",
    topics=[
        "active-directory",
        "blueteam",
        "hacking-tools",
        "pentest",
        "redteam-tools",
        "scanner",
    ],
)

PublicRepository(
    name="bingokta",
    description="Bingo with Okta, but in Colombia",
    topics=[
        "2fa",
        "okta",
        "rust",
    ],
)

PublicRepository(
    name="IAMme-IAMme",
    description="IAMme is a tool designed to visualize the connections between entities within an Okta tenant",
    topics=[
        "graph",
        "iam",
        "okta",
    ],
)

PublicRepository(
    name="goflat",
    description="Flatten complex JSON structures to a one-dimensional map (JSON key/value).",
    topics=[
        "flattener",
        "golang",
        "json",
        "slices",
        "structs",
    ],
)
