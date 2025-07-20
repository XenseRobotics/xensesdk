# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'xense'
copyright = '2025, IRonman'
author = 'IRonman'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_tabs.tabs']



templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_js_files = ['custom.js']
html_context = {
    "display_github": True,  # 显示 GitHub 相关链接
    "github_user": "XenseRobotics",  # 你的 GitHub 用户名
    "github_repo": "xensesdk",  # 你的 GitHub 仓库名
    "github_version": "docs",  # 分支名称，比如 main 或者 master
    "conf_py_path": "/docs/docs/source/",  # 配置文件在仓库中的路径
}

# multi-language docs
language = 'en'
locale_dirs = ['../locales/']   # path is example but recommended.
gettext_compact = False  # optional.
gettext_uuid = True  # optional.

# EPUB options
epub_show_urls = 'footnote'

