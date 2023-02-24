#!/usr/bin/env python
"""
BS Conversion Stats plugin for MultiQC, showing how to structure code
and plugin hooks to work effectively with the main MultiQC code.
For more information about MultiQC, see http://multiqc.info
"""

from setuptools import setup, find_packages

version = '0.1'

setup(
    name = 'bs_conversion_stats',
    version = version,
    author = 'Anthony Pompetti',
    author_email = 'apompetti@coriell.org',
    description = "BS Conversion Stats MultiQC plugin",
    long_description = __doc__,
    keywords = 'bioinformatics',
    url = '',
    download_url = 'https://github.com/Apompetti-Cori/MQC_BS_Conversion_Stats',
    license = '',
    packages = find_packages(),
    include_package_data = True,
    install_requires = [
        'multiqc'
    ],
    entry_points = {
        'multiqc.modules.v1': [
            'bs_conversion_stats = bs_conversion_stats.modules.bs_conversion_stats:MultiqcModule',
        ],
        'multiqc.cli_options.v1': [
            'disable_plugin = bs_conversion_stats.cli:disable_plugin'
        ],
        'multiqc.hooks.v1': [
            'execution_start = bs_conversion_stats.custom_code:bs_conversion_stats_execution_start'
        ]
    },
    classifiers = [
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Bio-Informatics'
    ],
)