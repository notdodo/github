"""Pulumi resources to create and configure repositories"""

from __future__ import annotations

import re

import pulumi
import pulumi_github as github

# Regular expression for validating GitHub repository names
GITHUB_REPO_NAME_REGEX = re.compile(r"^[\w.-]+$")


def format_resource_name(name: str, resource: pulumi.Resource | None) -> str:
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
    pulumi.error(error_message, resource)
    raise NameError(error_message)


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
        repo_opts: pulumi.ResourceOptions | None = None,
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
                repo_opts or pulumi.ResourceOptions(),
                pulumi.ResourceOptions(parent=self),
            ),
        )

        self.register_outputs({"repository": self.repository})
