#   -*- coding: utf-8 -*-
from pybuilder.core import Author, use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.distutils")
use_plugin('python.install_dependencies')

name = "bookstore"
authors = [
    Author('Adityavikram Rajawat', 'adityavikram.rajawat@st.niituniversity.in'),
    Author('Yash Jain', 'y')
]
license = 'MIT License'
default_task = ['install_dependencies', 'analyze', 'publish']
version = '0.1'


@init
def set_properties(project):
    project.depends_on('flask')
