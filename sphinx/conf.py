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
# documentation root, use os.path.abspath to make it absolute.

# Inject the parent directory into Python's active system path-matrix
# with '..' telling Python to step up into the repository root:
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------

project = 'Sphinx Sandbox: Code and Docs'
copyright = '2026, Elliria'
author = 'Elliria'

# -- General configuration ---------------------------------------------------

# Provide the location for the theme assets in the resources sub-directory:
templates_path = ['resources/templates']
html_static_path = ['resources/static']
extensions = [
    'sphinx.ext.autodoc',  # The engine that executes the code to grab docstrings
    'sphinx.ext.viewcode', # Adds handy "[source]" links to your compiled site
    'sphinx.ext.githubpages',  # Bypass Jekyll blocking bugs to enable GitHub Pages
]

# Provide the location for the master document:
master_doc = 'index'

html_theme = 'sphinx_rtd_theme'
