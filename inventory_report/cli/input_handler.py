from typing import List
from inventory_report.inventory import Inventory
from inventory_report.importers import CsvImporter, JsonImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def process_report_request(file_paths: List[str], report_type: str) -> str:
    try:
        # ----- Chooses the type of file -----
        if report_type == "simple":
            report = SimpleReport()
        elif report_type == "complete":
            report = CompleteReport()
        else:
            raise ValueError("Report type is invalid.")

        # ----- Process of each file -----
        for path in file_paths:
            if path.endswith(".csv"):
                importer = CsvImporter
            elif path.endswith(".json"):
                importer = JsonImporter
            else:
                # Ignore not supported extensions
                continue

            # Build the inventory using the correct one
            inventory = Inventory(importer)
            inventory.import_data(path)

            # Add to file
            report.add_inventory(inventory)

        # ----- Creates and returns the file -----
        return report.generate()

    except ValueError:
        raise ValueError("Report type is invalid.")


                

 

    
    
