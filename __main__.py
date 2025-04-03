"""Pulumi project to manage `notdodo` public repositories"""

from notdodo_github import GitIgnore, License, PublicRepository

PublicRepository(
    name="github",
    description="Manage notdodo public repositories.",
    enabled_github_actions=[
        "snok/install-poetry@*",
    ],
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
    description="Bot per leggere i livelli idrometrici dei fiumi dell'Emilia Romagna riportati da allertameteo.regione.emilia-romagna.it.",
    homepage_url="https://t.me/erfiume_bot",
    license_template=License.GPL_3,
    enabled_github_actions=[
        "aws-actions/*",
        "jaxxstorm/action-install-gh-release@*",
        "mlugg/setup-zig@*",
        "snok/install-poetry@*",
        "swatinem/rust-cache@*",
        "tj-actions/changed-files@*",
    ],
    oidc_claims=[
        "repo",
        "context",
        "job_workflow_ref",
    ],
    topics=[
        "emilia-romagna",
        "livello-fiumi",
        "telegram",
        "rust",
        "pulumi",
    ],
)

PublicRepository(
    name="github-actions",
    description="Collection of custom GHA and reusable workflows.",
    enabled_github_actions=[
        "aquasecurity/setup-trivy@*",
        "aquasecurity/trivy-action@*",
        "docker/*",
        "snok/install-poetry@*",
        "tj-actions/changed-files@*",
    ],
    topics=[
        "github-actions",
        "reusable-workflows",
        "cicd-security",
    ],
)

PublicRepository(
    name="notdodo",
    description="About",
    enabled_github_actions=[
        "jamesgeorge007/github-activity-readme@*",
    ],
)


PublicRepository(
    name="pulumi-k8s",
    description="Pulumi deployments for Kubernetes",
    topics=[
        "infrastructure-as-code",
        "kubernetes",
        "pulumi",
        "security",
    ],
)


PublicRepository(
    name="sparktrail",
    description="Query AWS CloudTrail using Spark (python) to perform analysis",
    license_template=License.GPL_3,
    topics=[
        "aws",
        "cloudtrail",
        "log",
        "spark",
    ],
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
    enabled_github_actions=[
        "aws-actions/configure-aws-credentials@*",
        "jaxxstorm/action-install-gh-release@*",
        "mlugg/setup-zig@*",
        "swatinem/rust-cache@*",
    ],
    gitignore_template=GitIgnore.RUST,
    license_template=License.GPL_3,
    topics=[
        "2fa",
        "okta",
        "rust",
    ],
)

PublicRepository(
    name="IAMme-IAMme",
    description="IAMme is a tool designed to visualize the connections between entities within an Okta tenant",
    license_template=License.GPL_3,
    enabled_github_actions=[
        "aquasecurity/setup-trivy@*",
        "aquasecurity/trivy-action@*",
        "docker/build-push-action@*",
        "docker/login-action@*",
        "docker/metadata-action@*",
        "docker/setup-buildx-action@*",
        "docker/setup-qemu-action@*",
        "golangci/golangci-lint-action@*",
        "securego/gosec@*",
    ],
    topics=[
        "graph",
        "iam",
        "okta",
    ],
)

PublicRepository(
    name="goflat",
    description="Flatten complex JSON structures to a one-dimensional map (JSON key/value).",
    license_template=License.GPL_3,
    topics=[
        "flattener",
        "json",
        "golang",
    ],
)

PublicRepository(
    name="proxmox",
    description="Manage my ProxmoxVE node",
    topics=[
        "proxmox",
        "terraform",
    ],
)
