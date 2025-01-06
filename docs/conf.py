"""Configuration file for the Sphinx documentation builder."""
import os
import sys

project = 'gpuaidev-docs'
version = "0.0.1"
release = version
html_title = ""
author = "Advanced Micro Devices, Inc."
copyright = "Copyright (c) 2024 Advanced Micro Devices, Inc. All rights reserved."

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_nb',            # For integrating Jupyter notebooks
    'sphinx.ext.mathjax', # For rendering math expressions
    'sphinx_rtd_theme',   # For the Read the Docs theme
]

# Paths for templates and static files
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'sphinx/venv']

source_suffix = ['.md', '.ipynb']  
# Use Read the Docs theme
html_theme = 'sphinx_rtd_theme'

# Paths for custom static files (e.g., CSS, JS)
html_static_path = ['_static']

