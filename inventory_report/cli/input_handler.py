from typing import List
from inventory_report.inventory import Inventory
from inventory_report.importers import CsvImporters,JsonImporter
from reports.simple_report import SimpleReport
from reports.complete_report import Complete
def process_report_request(file_paths:List[str],report_type:str)->str:
                try:
                      with open(file_paths,"r") as file:
                            return """ Process the report given a list of file paths and a report type,
                                     and returns the result.
                                           """
                
                except ValueError:
                     print("Report type is invalid")

                

 

    
    