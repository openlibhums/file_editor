# file_editor
A Django file editor app for Janeway.

## Installation

Install directly from the [Open Library of Humanities](https://github.com/openlibhums) GitHub repository:

```bash
pip install git+https://github.com/openlibhums/file_editor.git
```

Then add it to your Django project's `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # ...
    "file_editor",
]
```

Finally, include the app's URLs in `src/core/include_urls.py`:

```python
path("file-editor/", include("file_editor.urls")),
```
