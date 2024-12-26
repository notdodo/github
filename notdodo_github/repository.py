"""Pulumi resources to create and configure repositories"""

from __future__ import annotations

from enum import StrEnum

import pulumi
import pulumi_github as github

from .helpers import format_resource_name


class GitIgnore(StrEnum):
    """GitIgnore file templates"""

    AL = "AL"
    ACTIONSCRIPT = "Actionscript"
    ADA = "Ada"
    AGDA = "Agda"
    ANDROID = "Android"
    APPENGINE = "AppEngine"
    APPCELERATORTITANIUM = "AppceleratorTitanium"
    ARCHLINUXPACKAGES = "ArchLinuxPackages"
    AUTOTOOLS = "Autotools"
    BALLERINA = "Ballerina"
    C = "C"
    CPP = "C++"
    CFWHEELS = "CFWheels"
    CMAKE = "CMake"
    CUDA = "CUDA"
    CAKEPHP = "CakePHP"
    CHEFCOOKBOOK = "ChefCookbook"
    CLOJURE = "Clojure"
    CODEIGNITER = "CodeIgniter"
    COMMONLISP = "CommonLisp"
    COMPOSER = "Composer"
    CONCRETE5 = "Concrete5"
    COQ = "Coq"
    CRAFTCMS = "CraftCMS"
    D = "D"
    DM = "DM"
    DART = "Dart"
    DELPHI = "Delphi"
    DRUPAL = "Drupal"
    ECU_TEST = "ECU-TEST"
    EPISERVER = "EPiServer"
    EAGLE = "Eagle"
    ELISP = "Elisp"
    ELIXIR = "Elixir"
    ELM = "Elm"
    ERLANG = "Erlang"
    EXPRESSIONENGINE = "ExpressionEngine"
    EXTJS = "ExtJs"
    FANCY = "Fancy"
    FINALE = "Finale"
    FIREBASE = "Firebase"
    FLAXENGINE = "FlaxEngine"
    FORCEDOTCOM = "ForceDotCom"
    FORTRAN = "Fortran"
    FUELPHP = "FuelPHP"
    GWT = "GWT"
    GCOV = "Gcov"
    GITBOOK = "GitBook"
    GITHUBPAGES = "GitHubPages"
    GO = "Go"
    GODOT = "Godot"
    GRADLE = "Gradle"
    GRAILS = "Grails"
    HASKELL = "Haskell"
    IAR = "IAR"
    IGORPRO = "IGORPro"
    IDRIS = "Idris"
    JBOSS = "JBoss"
    JENKINS_HOME = "JENKINS_HOME"
    JAVA = "Java"
    JEKYLL = "Jekyll"
    JOOMLA = "Joomla"
    JULIA = "Julia"
    KICAD = "KiCad"
    KOHANA = "Kohana"
    KOTLIN = "Kotlin"
    LABVIEW = "LabVIEW"
    LARAVEL = "Laravel"
    LEININGEN = "Leiningen"
    LEMONSTAND = "LemonStand"
    LILYPOND = "Lilypond"
    LITHIUM = "Lithium"
    LUA = "Lua"
    MAGENTO = "Magento"
    MAVEN = "Maven"
    MERCURY = "Mercury"
    METAPROGRAMMINGSYSTEM = "MetaProgrammingSystem"
    MODELICA = "Modelica"
    NANOC = "Nanoc"
    NIM = "Nim"
    NODE = "Node"
    OCAML = "OCaml"
    OBJECTIVEC = "Objective-C"
    OPA = "Opa"
    OPENCART = "OpenCart"
    ORACLEFORMS = "OracleForms"
    PACKER = "Packer"
    PERL = "Perl"
    PHALCON = "Phalcon"
    PLAYFRAMEWORK = "PlayFramework"
    PLONE = "Plone"
    PRESTASHOP = "Prestashop"
    PROCESSING = "Processing"
    PURESCRIPT = "PureScript"
    PYTHON = "Python"
    QOOXDOO = "Qooxdoo"
    QT = "Qt"
    R = "R"
    ROS = "ROS"
    RACKET = "Racket"
    RAILS = "Rails"
    RAKU = "Raku"
    RESCRIPT = "ReScript"
    RHODESRHOMOBILE = "RhodesRhomobile"
    RUBY = "Ruby"
    RUST = "Rust"
    SCONS = "SCons"
    SASS = "Sass"
    SCALA = "Scala"
    SCHEME = "Scheme"
    SCRIVENER = "Scrivener"
    SDCC = "Sdcc"
    SEAMGEN = "SeamGen"
    SKETCHUP = "SketchUp"
    SMALLTALK = "Smalltalk"
    STELLA = "Stella"
    SUGARCRM = "SugarCRM"
    SWIFT = "Swift"
    SYMFONY = "Symfony"
    SYMPHONYCMS = "SymphonyCMS"
    TEX = "TeX"
    TERRAFORM = "Terraform"
    TEXTPATTERN = "Textpattern"
    TURBOGEARS2 = "TurboGears2"
    TWINCAT3 = "TwinCAT3"
    TYPO3 = "Typo3"
    UNITY = "Unity"
    UNREALENGINE = "UnrealEngine"
    VVVV = "VVVV"
    VISUALSTUDIO = "VisualStudio"
    WAF = "Waf"
    WORDPRESS = "WordPress"
    XOJO = "Xojo"
    YEOMAN = "Yeoman"
    YII = "Yii"
    ZENDFRAMEWORK = "ZendFramework"
    ZEPHIR = "Zephir"
    ZIG = "Zig"


class License(StrEnum):
    """Available Licenses"""

    AFL_3 = "afl-3"
    AGPL_3 = "agpl-3"
    APACHE_2 = "apache-2"
    ARTISTIC_2 = "artistic-2"
    BLUEOAK_1 = "blueoak-1"
    BSD_0 = "0bsd"
    BSD_2_CLAUSE = "bsd-2-clause"
    BSD_2_CLAUSE_PATENT = "bsd-2-clause-patent"
    BSD_3_CLAUSE = "bsd-3-clause"
    BSD_3_CLAUSE_CLEAR = "bsd-3-clause-clear"
    BSD_4_CLAUSE = "bsd-4-clause"
    BSL_1 = "bsl-1"
    CC_BY_4 = "cc-by-4"
    CC_BY_SA_4 = "cc-by-sa-4"
    CC0_1 = "cc0-1"
    CECILL_2 = "cecill-2"
    CERN_OHL_P_2 = "cern-ohl-p-2"
    CERN_OHL_S_2 = "cern-ohl-s-2"
    CERN_OHL_W_2 = "cern-ohl-w-2"
    ECL_2 = "ecl-2"
    EPL_1 = "epl-1"
    EPL_2 = "epl-2"
    EUPL_1 = "eupl-1"
    GFDL_1 = "gfdl-1"
    GPL_2 = "gpl-2"
    GPL_3 = "gpl-3"
    ISC = "isc"
    LGPL_2 = "lgpl-2"
    LGPL_3 = "lgpl-3"
    LPPL_1 = "lppl-1"
    MIT = "mit"
    MIT_0 = "mit-0"
    MPL_2 = "mpl-2"
    MS_PL = "ms-pl"
    MS_RL = "ms-rl"
    MULANPSL_2 = "mulanpsl-2"
    NCSA = "ncsa"
    ODBL_1 = "odbl-1"
    OFL_1 = "ofl-1"
    OSL_3 = "osl-3"
    POSTGRESQL = "postgresql"
    UNLICENSE = "unlicense"
    UPL_1 = "upl-1"
    VIM = "vim"
    WTFPL = "wtfpl"
    ZLIB = "zlib"


class PublicRepository(pulumi.ComponentResource):
    """
    A Pulumi component resource to create a public GitHub repository with customizable options.

    :param name: The name of the repository to create.
    :param repo_opts: `ResourceOptions` for configuring the GitHub repository resource.
    :param opts: `ResourceOptions` for configuring this custom resource.
    """

    def __init__(  # noqa: PLR0913
        self,
        name: str,
        description: str | None = None,
        gitignore_template: GitIgnore | None = None,
        homepage_url: str | None = None,
        license_template: License | None = None,
        oidc_claims: list[str] | None = None,
        topics: list[str] | None = None,
        repo_opts: pulumi.ResourceOptions | None = None,
        opts: pulumi.ResourceOptions | None = None,
    ):
        """class init"""
        default_oidc_claims = False
        self.name = name
        self.default_branch = "main"
        self.resource_name = f"{format_resource_name(name, self)}-repository"
        super().__init__(
            "notdodo:github:PublicRepository", self.resource_name, {}, opts
        )
        topics = topics if topics else []

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
            homepage_url=(
                homepage_url if homepage_url else f"https://github.com/notdodo/{name}"
            ),
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

        if not oidc_claims:
            default_oidc_claims = True

        self.oidc_claims = (
            github.ActionsRepositoryOidcSubjectClaimCustomizationTemplate(
                f"{self.resource_name}-oidc-sub-claims",
                repository=self.repository.name,
                use_default=default_oidc_claims,
                include_claim_keys=oidc_claims,
                opts=pulumi.ResourceOptions(
                    parent=self.repository, delete_before_replace=True
                ),
            )
        )

        github.RepositoryDependabotSecurityUpdates(
            f"{self.resource_name}-dependabot-security",
            enabled=True,
            repository=self.repository.name,
            opts=pulumi.ResourceOptions(parent=self.repository),
        )

        self.register_outputs(
            {"repository": self.repository, "oidc_claims": self.oidc_claims}
        )
