# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Robotics Training Center'
copyright = 'CMU'
author = 'Manufacturing Futures Institute'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': -1,
}
html_logo = 'files/white-logo-shadow.png'
html_favicon = 'files/white-logo.ico'
html_static_path = ['_static']

html_css_files = [
    'custom.css',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css',
]

# -- top-right github link configuration -------------------------------------

html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "cmu-mfi", # Username
    "github_repo": "rtc", # Repo name
    "github_version": "master", # Version
    "conf_py_path": "/doc/", # Path in the checkout to the docs root
}
