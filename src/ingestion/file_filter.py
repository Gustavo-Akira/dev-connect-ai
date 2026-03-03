from pathlib import Path

ALLOWED_EXTENSIONS = {
    ".py",
    ".md",
    ".yaml",
    ".yml",
    ".json",
    ".xml",
    ".html",
    ".css",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".java",
    ".go",
}

IGNORED_DIRECTORIES = {
    ".git",
    "node_modules",
    "target",
    "dist",
    "build",
    "__pycache__",
}


def filter_files(file_path: Path) -> bool:
    if any(part in IGNORED_DIRECTORIES for part in file_path.parts):
        return False

    return file_path.suffix.lower() in ALLOWED_EXTENSIONS