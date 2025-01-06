"""Pulumi resources to create and configure repositories"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import pulumi
import pulumi_github as github

from .github_actions import DEFAULT_ALLOWED_GITHUB_ACTIONS
from .helpers import format_resource_name

if TYPE_CHECKING:
    from .gitignore import GitIgnore
    from .license import License


class PublicRepository(pulumi.ComponentResource):
    """
    A Pulumi component resource to create a public GitHub repository with customizable options.

    :param name [str]: The name of the repository to create.
    :param description [str | None]: A short description of the repository.
    :param gitignore_template [GitIgnore | None]: The `.gitignore` template to use.
    :param github_actions_enabled [list[str] | None]: List of allowed GitHub Actions patterns.
    :param homepage_url [str | None]: URL for the repository homepage.
    :param license_template [License | None]: License template for the repository.
    :param oidc_claims [list[str] | None]: OIDC claims for GitHub Actions.
    :param topics [list[str] | None]: List of topics for the repository.
    :param repo_opts [pulumi.ResourceOptions | None]: Pulumi resource options for the GitHub repository.
    :param opts [pulumi.ResourceOptions | None]: Pulumi resource options for the custom resource.
    """

    def __init__(  # noqa: PLR0913
        self,
        name: str,
        description: str | None = None,
        gitignore_template: GitIgnore | None = None,
        enabled_github_actions: list[str] | None = None,
        homepage_url: str | None = None,
        license_template: License | None = None,
        oidc_claims: list[str] | None = None,
        topics: list[str] | None = None,
        repo_opts: pulumi.ResourceOptions | None = None,
        default_branch: str = "main",
        opts: pulumi.ResourceOptions | None = None,
    ):
        """
        Initialize the PublicRepository class.
        """

        self.name = name
        self.default_branch = default_branch
        self.resource_name = f"{format_resource_name(name, self)}-repository"
        super().__init__(
            "notdodo:github:PublicRepository", self.resource_name, {}, opts
        )
        topics = topics or []

        self.repository = github.Repository(
            self.resource_name,
            name=name,
            allow_merge_commit=False,
            allow_squash_merge=True,
            allow_update_branch=True,
            auto_init=True,
            delete_branch_on_merge=True,
            description=description,
            gitignore_template=gitignore_template,
            has_discussions=False,
            has_downloads=False,
            has_issues=True,
            has_projects=False,
            has_wiki=False,
            homepage_url=homepage_url or f"https://github.com/notdodo/{name}",
            license_template=license_template,
            security_and_analysis=github.RepositorySecurityAndAnalysisArgs(
                secret_scanning=github.RepositorySecurityAndAnalysisSecretScanningArgs(
                    status="enabled",
                ),
                secret_scanning_push_protection=github.RepositorySecurityAndAnalysisSecretScanningPushProtectionArgs(
                    status="enabled",
                ),
            ),
            squash_merge_commit_message="BLANK",
            squash_merge_commit_title="PR_TITLE",
            topics=topics,
            vulnerability_alerts=True,
            web_commit_signoff_required=True,
            opts=pulumi.ResourceOptions.merge(
                repo_opts, pulumi.ResourceOptions(parent=self)
            ),
        )

        self.__branch_and_environment()
        self.oidc_claims = self.__oidc_claims(oidc_claims)
        self.__actions(enabled_github_actions)

        github.RepositoryDependabotSecurityUpdates(
            f"{self.resource_name}-dependabot-security",
            enabled=True,
            repository=self.repository.name,
            opts=pulumi.ResourceOptions(parent=self.repository),
        )

        self.register_outputs(
            {"repository": self.repository, "oidc_claims": self.oidc_claims}
        )

    def __branch_and_environment(self) -> None:
        github.Branch(
            f"{self.resource_name}-{self.default_branch}-branch",
            branch=self.default_branch,
            repository=self.repository.name,
            opts=pulumi.ResourceOptions(parent=self.repository),
        )
        github.BranchDefault(
            f"{self.resource_name}-branch-default",
            branch=self.default_branch,
            repository=self.repository.name,
            opts=pulumi.ResourceOptions(parent=self.repository),
        )

        github.RepositoryEnvironment(
            f"{self.resource_name}-{self.default_branch}-environment",
            repository=self.repository.name,
            environment=self.default_branch,
            opts=pulumi.ResourceOptions(parent=self.repository),
        )

    def __oidc_claims(
        self,
        oidc_claims: list[str] | None = None,
    ) -> github.ActionsRepositoryOidcSubjectClaimCustomizationTemplate:
        default_oidc_claims = oidc_claims is None
        return github.ActionsRepositoryOidcSubjectClaimCustomizationTemplate(
            f"{self.resource_name}-oidc-sub-claims",
            repository=self.repository.name,
            use_default=default_oidc_claims,
            include_claim_keys=oidc_claims,
            opts=pulumi.ResourceOptions(
                parent=self.repository, delete_before_replace=True
            ),
        )

    def __actions(self, enabled_github_actions: list[str] | None = None) -> None:
        if enabled_github_actions:
            enabled_github_actions.extend(DEFAULT_ALLOWED_GITHUB_ACTIONS)
        else:
            enabled_github_actions = DEFAULT_ALLOWED_GITHUB_ACTIONS
        enabled_github_actions.sort()
        github.ActionsRepositoryPermissions(
            f"{self.resource_name}-actions-allowed",
            enabled=True,
            allowed_actions="selected",
            allowed_actions_config=github.ActionsRepositoryPermissionsAllowedActionsConfigArgs(
                github_owned_allowed=True,
                patterns_alloweds=enabled_github_actions,
                verified_allowed=False,
            ),
            repository=self.repository.name,
            opts=pulumi.ResourceOptions(parent=self.repository),
        )

        github.RepositoryFile(
            f"{self.resource_name}-enforced-workflow-gitleaks",
            repository=self.repository.name,
            branch=self.default_branch,
            file=".github/workflows/run-gitleaks.yml",
            content=Path.open(Path(".github/workflows/run-gitleaks.yml")).read(),
            commit_message="[sec]: enforce Gitleaks workflow",
            commit_author="notdodo",
            commit_email="6991986+notdodo@users.noreply.github.com",
            overwrite_on_create=True,
            opts=pulumi.ResourceOptions(parent=self.repository),
        )

        github.RepositoryFile(
            f"{self.resource_name}-enforced-workflow-infra-scan",
            repository=self.repository.name,
            branch=self.default_branch,
            file=".github/workflows/repo-infra-scan.yml",
            content=Path.open(Path(".github/workflows/repo-infra-scan.yml")).read(),
            commit_message="[sec]: enforce static scan of infra files workflow",
            commit_author="notdodo",
            commit_email="6991986+notdodo@users.noreply.github.com",
            overwrite_on_create=True,
            opts=pulumi.ResourceOptions(parent=self.repository),
        )

        github.RepositoryFile(
            f"{self.resource_name}-enforced-workflow-cleanup-branch",
            repository=self.repository.name,
            branch=self.default_branch,
            file=".github/workflows/repo-branch-cleanup.yml",
            content=Path.open(Path(".github/workflows/repo-branch-cleanup.yml")).read(),
            commit_message="[enh]: enforce auto clean up of PR cache workflow",
            commit_author="notdodo",
            commit_email="6991986+notdodo@users.noreply.github.com",
            overwrite_on_create=True,
            opts=pulumi.ResourceOptions(parent=self.repository),
        )

        github.RepositoryFile(
            f"{self.resource_name}-enforced-codeowners",
            repository=self.repository.name,
            branch=self.default_branch,
            file=".github/CODEOWNERS",
            content=Path.open(Path(".github/CODEOWNERS")).read(),
            commit_message="[enh]: set CODEOWNERS",
            commit_author="notdodo",
            commit_email="6991986+notdodo@users.noreply.github.com",
            overwrite_on_create=True,
            opts=pulumi.ResourceOptions(parent=self.repository),
        )
