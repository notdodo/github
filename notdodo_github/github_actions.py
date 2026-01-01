"""
Define the list of globally allowed GitHub Actions
"""

DEFAULT_ALLOWED_GITHUB_ACTIONS = [
    "astral-sh/setup-uv@*",
    "aws-actions/aws-secretsmanager-get-secrets@*",
    "aws-actions/configure-aws-credentials@*",
    "checkmarx/kics-github-action@*",
    "docker/*",
    "gitleaks/gitleaks-action@*",
    "go-task/setup-task@*",
    "notdodo/*",
    "pulumi/*",
    "reviewdog/action-*",
    "sigstore/cosign-installer@*",
    "step-security/harden-runner@*",
]
