import pathlib
import os
import sys

sys.path.append(str(pathlib.Path("_extensions").resolve()))

os.environ["MPLCONFIGDIR"] = "./.matplotlib"

author = "Kayce Basques"
copyright = f"2025, {author}"
exclude_patterns = [
    ".github",
    ".gitignore",
    "_extensions",
    "BUILD.bazel",
    "MODULE.bazel",
    "MODULE.bazel.lock",
    "bazel-bin",
    "bazel-dev",
    "bazel-out",
    "bazel-testlogs",
    "bazelisk",
    "requirements.lock",
    "requirements.txt",
]
extensions = [
    "matplotlib.sphinxext.plot_directive",
    "sitemap",
    "sphinx.ext.mathjax",
    "sphinx_copybutton",
    "sphinx_genai_huggingface",
    "sphinx_reredirects",
]
html_extra_path = [
    "ai/agents/searchtools.md",
    "ai/agents/searchtools.txt",
    "rss.xml", 
]
html_permalinks_icon = "§"
html_static_path = ["_static"]
html_theme = 'basic'
project = "technicalwriting.dev"
pygments_style = "github-dark"
redirects = {
    "a11y/skip": "https://web.archive.org/web/20250225001215/https://technicalwriting.dev/a11y/skip.html",
    "data/embeddings": "../embeddings/overview.html",
    "data/intertwingularity": "../links/intertwingularity.html",
    "embeddings/overview": "../ml/embeddings/overview.html",
    "ml/plugins": "https://web.archive.org/web/20250222025828/https://technicalwriting.dev/ml/plugins.html",
    "seo/discovered-not-indexed": "https://web.archive.org/web/20250222024724/https://technicalwriting.dev/seo/discovered-not-indexed.html",
    "seo/sentry-overflow": "https://web.archive.org/web/20250221195536/https://technicalwriting.dev/seo/sentry-overflow.html",
    "src/link-text-automation": "../links/automation.html",
    "src/verbatim-wrangling": "https://web.archive.org/web/20240724083629/https://technicalwriting.dev/src/verbatim-wrangling.html",
    "ux/offline": "https://web.archive.org/web/20250221193209/https://technicalwriting.dev/ux/offline.html",
    "ux/pdf": "../links/pdf.html",
    "ux/methodology": "https://web.archive.org/web/20250225002414/https://technicalwriting.dev/ux/methodology.html",
    "ux/searchboxes": "https://web.archive.org/web/20250225002920/https://technicalwriting.dev/ux/searchboxes.html",
    "www/pdf": "../links/pdf.html",
}
release = "0.0.0"
templates_path = ["_templates"]
# https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html#configuration-options
plot_html_show_formats = False
copybutton_prompt_text = "$ "
