"""Pulumi resources to create and configure repositories"""

from __future__ import annotations

import re

import pulumi
import pulumi_github as github

# Regular expression for validating GitHub repository names
GITHUB_REPO_NAME_REGEX = re.compile(r"^[\w.-]+$")


def _pulumi_error(message: str, resource: pulumi.Resource | None = None) -> None:
    pulumi.error(message, resource)
    raise ValueError(message)


def _pulumi_warning(message: str, resource: pulumi.Resource | None = None) -> None:
    pulumi.warn(message, resource)


def format_resource_name(name: str, resource: pulumi.Resource | None = None) -> str:
    """
    Formats a string to be used as a Pulumi resource name.

    :param name: The proposed name of the resource.
    :param resource: The Pulumi resource for context in case of errors.
    :return: A formatted, valid Pulumi resource name.
    :raises NameError: If the name is invalid.
    """
    if GITHUB_REPO_NAME_REGEX.match(name):
        return name.lower().replace(" ", "-")
    error_message = (
        "Invalid repository name. Only alphanumeric, '.', '-' and '_' are allowed."
    )
    _pulumi_error(error_message, resource)


class PublicRepository(pulumi.ComponentResource):
    """
    A Pulumi component resource to create a public GitHub repository with customizable options.

    :param name: The name of the repository to create.
    :param repo_opts: `ResourceOptions` for configuring the GitHub repository resource.
    :param opts: `ResourceOptions` for configuring this custom resource.
    """

    def __init__(
        self,
        name: str,
        default_oidc_claims: bool | None = True,
        oidc_claims: list[str] | None = None,
        opts: pulumi.ResourceOptions | None = None,
    ):
        """class init"""
        self.name = name
        self.resource_name = f"{format_resource_name(name, self)}-repository"
        super().__init__(
            "notdodo:github:PublicRepository", self.resource_name, {}, opts
        )

        self.repository = github.Repository(
            self.resource_name,
            name=name,
            has_downloads=True,
            has_issues=True,
            has_projects=True,
            has_wiki=True,
            vulnerability_alerts=True,
            opts=pulumi.ResourceOptions.merge(
                opts, pulumi.ResourceOptions(parent=self)
            ),
        )

        if not oidc_claims:
            oidc_claims = []
        if default_oidc_claims and len(oidc_claims) > 0:
            _pulumi_warning(
                "Specified `default_oidc_claims` with `default_oidc_claims` to `True` -> switching `default_oidc_claims` to `False`",
                self.repository,
            )
            default_oidc_claims = False

        self.oidc_claims = (
            github.ActionsRepositoryOidcSubjectClaimCustomizationTemplate(
                f"{self.resource_name}-oidc-sub-claims",
                repository=self.repository.name,
                use_default=default_oidc_claims,
                include_claim_keys=oidc_claims,
                opts=pulumi.ResourceOptions.merge(
                    opts,
                    pulumi.ResourceOptions(
                        parent=self.repository, delete_before_replace=True
                    ),
                ),
            )
        )

        self.register_outputs(
            {"repository": self.repository, "oidc_claims": self.oidc_claims}
        )
