#!/usr/bin/env python
""" MultiQC example plugin functions
We can add any custom Python functions here and call them
using the setuptools plugin hooks.
"""

from __future__ import print_function
from pkg_resources import get_distribution
import logging

from multiqc.utils import report, util_functions, config

# Initialise the main MultiQC logger
log = logging.getLogger('multiqc')

# Save this plugin's version number (defined in setup.py) to the MultiQC config
config.bs_conversion_stats_version = get_distribution("bs_conversion_stats").version

# Add default config options for the things that are used in MultiQC_NGI
def bs_conversion_stats_execution_start():
    """ Code to execute after the config files and
    command line flags have been parsedself.
    This setuptools hook is the earliest that will be able
    to use custom command line flags.
    """

    # Halt execution if we've disabled the plugin
    if config.kwargs.get('disable_plugin', True):
        return None

    log.info("Running Example MultiQC Plugin v{}".format(config.bs_conversion_stats_version))

    # Add to the main MultiQC config object.
    # User config files have already been loaded at this point
    #   so we check whether the value is already set. This is to avoid
    #   clobbering values that have been customised by users.

    # Add to the search patterns used by modules
    if 'bs_conversion_stats/reports' not in config.sp:
        config.update_dict( config.sp, { 'bs_conversion_stats/reports': { 'fn': '*.conversion-stats.tsv' } } )

    # Some additional filename cleaning
    config.fn_clean_exts.extend([
        '.conversion-stats'
    ])