"""Sphinx configuration."""
project = "MPTbot"
author = "Matt Shirley"
copyright = "2023, Matt Shirley"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
