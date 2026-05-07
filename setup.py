from pathlib import Path

from setuptools import setup

ROOT = Path(__file__).parent
long_description = (ROOT / "README.md").read_text(encoding="utf-8")

setup(
    name="janeway-file-editor",
    version="0.1.0",
    description="A Django file editor app for Janeway.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Open Library of Humanities",
    url="https://github.com/openlibhums/file_editor",
    license="AGPL-3.0-or-later",
    packages=["file_editor", "file_editor.migrations"],
    package_dir={
        "file_editor": ".",
        "file_editor.migrations": "migrations",
    },
    include_package_data=True,
    install_requires=["Django"],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
