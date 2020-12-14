#!/usr/bin/env python
#   -*- coding: utf-8 -*-

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'bookstore',
        version = '0.1',
        description = '',
        long_description = '',
        long_description_content_type = None,
        classifiers = [
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python'
        ],
        keywords = '',

        author = 'Adityavikram Rajawat, Yash Jain',
        author_email = 'adityavikram.rajawat@st.niituniversity.in, y',
        maintainer = '',
        maintainer_email = '',

        license = 'MIT License',

        url = '',
        project_urls = {},

        scripts = [],
        packages = [
            '.',
            'gamestore'
        ],
        namespace_packages = [],
        py_modules = [
            '__init__',
            'gamestore_tests'
        ],
        entry_points = {},
        data_files = [],
        package_data = {},
        install_requires = ['flask'],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        python_requires = '',
        obsoletes = [],
    )
