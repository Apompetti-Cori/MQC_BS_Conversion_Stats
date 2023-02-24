#!/usr/bin/env python

""" MultiQC example plugin module """

from __future__ import print_function
from collections import OrderedDict
import logging

from multiqc import config
from multiqc.plots import table
from multiqc.modules.base_module import BaseMultiqcModule

# Initialise the main MultiQC logger
log = logging.getLogger('multiqc')


headers = OrderedDict()

headers['Percent_Methylated_All'] = {
    'suffix': '%',
    'format': '{:,.2f}'
}

headers['Percent_Methylated_CpG'] = {
    'suffix': '%',
    'format': '{:,.2f}'
}

headers['Lambda_Percent_Methylated_All'] = {
    'suffix': '%',
    'format': '{:,.2f}'}

headers['Lambda_Percent_Methylated_CpG'] = {
    'suffix': '%',
    'format': '{:,.2f}'
}

headers['Methylated_All'] = {
    'hidden': True 
}        

headers['Unmethylated_All'] = {
    'hidden': True      
} 

headers['Methylated_CpG'] = {
    'hidden': True      
} 

headers['Unmethylated_CpG'] = {
    'hidden': True      
} 

headers['Methylated_nonCpG'] = {
    'hidden': True      
} 

headers['Unmethylated_nonCpG'] = {
    'hidden': True      
} 

headers['Percent_Methylated_nonCpG'] = {
    'hidden': True,
    'suffix': '%',
    'format': '{:,.2f}'
}

headers['Lambda_Methylated_All'] = {
    'hidden': True      
}

headers['Lambda_Unmethylated_All'] = {
    'hidden': True      
}

headers['Lambda_Methylated_CpG'] = {
    'hidden': True      
}

headers['Lambda_Unmethylated_CpG'] = {
    'hidden': True      
}

headers['Lambda_Methylated_nonCpG'] = {
    'hidden': True      
}

headers['Lambda_Unmethylated_nonCpG'] = {
    'hidden': True      
}

headers['Lambda_Percent_Methylated_nonCpG'] = {
    'hidden': True,
    'suffix': '%',
    'format': '{:,.2f}'
}

headers['z'] = {
    'hidden': True      
}

headers['Z'] = {
    'hidden': True      
}

headers['x'] = {
    'hidden': True      
}

headers['X'] = {
    'hidden': True      
}

headers['h'] = {
    'hidden': True      
}

headers['H'] = {
    'hidden': True      
}

headers['u'] = {
    'hidden': True      
}

headers['U'] = {
    'hidden': True      
}

headers['z_lambda'] = {
    'hidden': True      
}

headers['Z_lambda'] = {
    'hidden': True      
}

headers['x_lambda'] = {
    'hidden': True      
}

headers['X_lambda'] = {
    'hidden': True      
}

headers['h_lambda'] = {
    'hidden': True      
}

headers['H_lambda'] = {
    'hidden': True      
}

headers['u_lambda'] = {
    'hidden': True      
}

headers['U_lambda'] = {
    'hidden': True      
}

class MultiqcModule(BaseMultiqcModule):

    def __init__(self):

        # Halt execution if we've disabled the plugin
        if config.kwargs.get('disable_plugin', True):
            return None

        # Initialise the parent module Class object
        super(MultiqcModule, self).__init__(
            name = 'bs_conversion_stats',
            target = "bs_conversion_stats",
            anchor = 'bs_conversion_stats',
            href = 'https://github.com/Apompetti-Cori/MQC_BS_Conversion_Stats',
            info = "module to generate stats relating to bisulfite conversion."
        )

        # Find and load any input files for this module
        self.bs_conversion_stats_data = dict()
        for f in self.find_log_files('bs_conversion_stats/reports'):
            parsed_data = self.parse_reports(f['f'])
            if parsed_data is not None:
                s_name = self.clean_s_name(f['fn'], root=None)
                if s_name in self.bs_conversion_stats_data:
                    log.debug("Duplicate sample name found! Overwriting: {}".format(f['s_name']))
                self.add_data_source(f)
                self.bs_conversion_stats_data[s_name] = parsed_data

        # Filter out samples matching ignored sample names
        self.bs_conversion_stats_data = self.ignore_samples(self.bs_conversion_stats_data)

        # Nothing found - raise a UserWarning to tell MultiQC
        if len(self.bs_conversion_stats_data) == 0:
            log.debug("Could not find any reports in {}".format(config.analysis_dir))
            raise UserWarning

        log.info("Found {} reports".format(len(self.bs_conversion_stats_data)))

        # Write parsed report data to a file
        self.write_data_file(self.bs_conversion_stats_data, 'multiqc_my_example')

        #Create a very basic table
        table_html = table.plot(self.bs_conversion_stats_data, headers)

        #Add a report section with said table
        self.add_section(
            description = 'Basic table',
            helptext = '''
            Filler help text
            ''',
            plot = table_html
        )
    
    def parse_reports(self, raw_data):
        """ Takes in the file contents from self.find_log_files"""

        parsed_data = dict()
        lines = raw_data.split("\n")
        headers = lines[0].split("\t")
        data_list = lines[1].split("\t")
        for data,header in zip(data_list,headers):
            if header == "Sample_Name":
                continue
            else:
                if isinstance(data, str):
                    parsed_data[header] = data
                else:
                    parsed_data[header] = data

        if len(parsed_data) == 0: return None
        return parsed_data
