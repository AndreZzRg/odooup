# Copyright 2019 XOE Labs (<https://xoe.solutions>)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name="odooup",
    description="Odoo Project puppet master",
    long_description="\n".join(
        (
            open(os.path.join(here, "README.md")).read(),
            open(os.path.join(here, "CHANGES.md")).read(),
        )
    ),
    long_description_content_type="text/markdown",
    use_scm_version=True,
    packages=find_packages(),
    setup_requires=["setuptools-scm"],
    install_requires=["click>=7.0", "click-plugins", "future", "appdirs", "networkx"],
    license="LGPLv3+",
    author="XOE Labs",
    author_email="info@xoe.solutions",
    url="http://github.com/xoe-labs/odooup",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: "
        "GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Framework :: Odoo",
    ],
    entry_points="""
        [console_scripts]
        odooup=odooup.cli:main
        [core_package.cli_plugins]
        version=odooup.cli:version
        init=odooup.init:init
        patches=odooup.patches:patches
        whitelist=odooup.whitelist:whitelist
        clone=odooup.clone:clone
    """,
)
