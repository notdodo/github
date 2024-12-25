"""Pulumi resources to create and configure repositories"""

from __future__ import annotations

import pulumi
import pulumi_github as github

from .helpers import format_resource_name


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
        oidc_claims: list[str] | None = None,
        opts: pulumi.ResourceOptions | None = None,
    ):
        """class init"""
        default_oidc_claims = False
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
            default_oidc_claims = True

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
