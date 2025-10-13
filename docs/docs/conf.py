# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'xense'
copyright = '2025, 千觉机器人科技(上海)有限公司'
author = 'IRonman'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_tabs.tabs']



templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 3
}
html_static_path = ['_static']
html_css_files = ['custom.css','rst-tips.css','rst-note.css','container_step.css']
html_js_files = ['custom.js']
html_context = {
    'source_url_prefix': "https://github.com/XenseRobotics/xensesdk",
    'source_suffix': "",  # 移除自动添加的文件后缀（如 .rst）
    'conf_py_path': "",   # 清空配置文件路径，避免自动拼接
}

# multi-language docs
language = 'en'
locale_dirs = ['./locales/']   # path is example but recommended.
gettext_compact = False  # optional.
gettext_uuid = True  # optional.

# EPUB options
epub_show_urls = 'footnote'

