# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options.
# For a full list, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Imports -----------------------------------------------------------------

import os
import sys

# -- Path information---------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute. In this case,
# the parent directory is injected into Python's active system-path-matrix
# with '..' telling Python to step up into the repository root:
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------

project = 'Sphinx Sandbox: Code and Docs'
copyright = '2026, Elliria'
author = 'Elliria'

# -- General configuration ---------------------------------------------------

# List of Sphinx extension module names grouped by purpose since they're
# processed in the listed order. Both native (named 'sphinx.ext.*') and
# custom extensions are accepted:
extensions = [
    'sphinx.ext.autodoc',  # The engine that executes the code to grab docstrings
    'sphinx.ext.viewcode', # Adds handy "[source]" links to your compiled site
    'sphinx.ext.githubpages',  # Bypass Jekyll blocking bugs to enable GitHub Pages
]

# List of paths, relative to the documentation root directory, that contain
# templates:
templates_path = [
    'resources/templates',
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path, if it
# exists.
exclude_patterns = [
    '**/.DS_Store',    # Prevents Sphinx from tracking the macOS hidden **Desktop Services Store** file
    '**/__MACOSX/**',  # Prevents Sphinx from tracking macOS zip metadata directories
    '**/._*',          # Prevents Sphinx from tracking macOS AppleDouble metadata files
    '*.md',            # Prevents Sphinx from tracking all Markdown in the root directory
    '**/Thumbs.db',    # Prevents Sphinx from tracking all nested Windows thumbnail caches
    '**/.venv/**',      # Prevents Sphinx from tracking all nested virtual environments
]

# Provide the location for the master document:
master_doc = 'index'

# -- HTML configuration ------------------------------------------------------

html_theme = 'sphinx_rtd_theme'

# List of paths, relative to the documentation root directory, to custom
# static files (such as style-sheets). These files are copied over after the
# built-in static files, overwriting them:
html_static_path = [
    'resources/static',
]

