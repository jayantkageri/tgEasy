# tgEasy - Easy for a brighter Shine. A monkey pather add-on for Pyrogram
# Copyright (C) 2021 - 2022 Jayant Hegde Kageri <https://github.com/jayantkageri>

# This file is part of tgEasy.

# tgEasy is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# tgEasy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with tgEasy.  If not, see <http://www.gnu.org/licenses/>.

import re

from setuptools import find_packages, setup

with open("tgEasy/__init__.py", encoding="utf-8") as f:
    version = re.findall(r"__version__ = \"(.+)\"", f.read())[0]

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

with open("requirements.txt", encoding="utf-8") as f:
    requires = f.read().splitlines()

setup(
    name="tgEasy",
    version=version,
    description="Easy for a brighter Shine, A Monkey Patcher add-on for Pyrogram",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/jayantkageri/tgEasy",
    download_url="https://github.com/jayantkageri/tgEasy/releases/latest",
    author="Jayant Hegde Kageri",
    author_email="jayantkageri@gmail.com",
    license="LGPLv3+",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="telegram chat messenger mtproto api client library python pyrogram tgeasy",
    project_urls={
        "Tracker": "https://github.com/jayantkageri/tgEasys/issues",
        "Community": "https://telegram.me/tgEasyNews",
        "Source": "https://github.com/jayantkageri/tgEasy",
        "Documentation": "https://github.com/jayantkageri/tgEasy#documatation",
    },
    python_requires="~=3.6",
    packages=find_packages(),
    zip_safe=False,
    install_requires=requires,
)
