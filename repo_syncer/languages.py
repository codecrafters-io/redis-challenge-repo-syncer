from dataclasses import dataclass

from jinja2 import Template, StrictUndefined


@dataclass
class FileFromTemplate:
    path: str
    template_path: str
    is_executable: bool = False

    def render(self, context: dict = None):
        if context is None:
            context = {}

        with open(f"repo_syncer/templates/{self.template_path}") as f:
            raw_contents = f.read()

        template = Template(raw_contents, undefined=StrictUndefined)
        return template.render(**context)


@dataclass
class Language:
    name: str
    repo: str
    source_file: str
    required_executables: [str]

    files: [FileFromTemplate]


F = FileFromTemplate


PYTHON_LANGUAGE = Language(
    name="Python",
    repo="codecrafters-io/redis-starter-py",
    source_file="app/main.py",
    required_executables=["python (3.8)"],
    files=[
        F("README.md", "README.md"),
        F("codecrafters.yml", "codecrafters.yml"),
        F("app/main.py", "python/app/main.py"),
        F("spawn_redis_server.sh", "python/spawn_redis_server.sh", is_executable=True),
    ],
)

# SWIFT_LANGUAGE = Language(
#     name="Swift",
#     repo="codecrafters-io/redis-starter-swift",
#     source_file="app/main.swift",
#     required_executables=["swift (5.1)"],
#     files=[
#         F("README.md", "README.md"),
#         F("codecrafters.yml", "codecrafters.yml"),
#         F("app/main.swift", "swift/app/main.swift"),
#         F("Makefile", "swift/Makefile"),
#         F("spawn_redis_server.sh", "swift/spawn_redis_server.sh", is_executable=True),
#     ],
# )

GO_LANGUAGE = Language(
    name="Go",
    repo="codecrafters-io/redis-starter-golang",
    source_file="app/server.go",
    required_executables=["go"],
    files=[
        F("README.md", "README.md"),
        F("codecrafters.yml", "codecrafters.yml"),
        F("spawn_redis_server.sh", "go/spawn_redis_server.sh", is_executable=True),
        F("app/server.go", "go/app/server.go"),
    ],
)

C_LANGUAGE = Language(
    name="C",
    repo="codecrafters-io/redis-starter-c",
    source_file="app/server.c",
    required_executables=["gcc"],
    files=[
        F("README.md", "README.md"),
        F("codecrafters.yml", "codecrafters.yml"),
        F("spawn_redis_server.sh", "c/spawn_redis_server.sh", is_executable=True),
        F("app/server.c", "c/app/server.c"),
    ],
)

PHP_LANGUAGE = Language(
    name="PHP",
    repo="codecrafters-io/redis-starter-php",
    source_file="app/main.php",
    required_executables=["php (7.4)"],
    files=[
        F("README.md", "README.md"),
        F("codecrafters.yml", "codecrafters.yml"),
        F("app/main.php", "php/app/main.php"),
        F("spawn_redis_server.sh", "php/spawn_redis_server.sh", is_executable=True),
    ],
)
