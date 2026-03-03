from inventory_report.reports.report import Report
from inventory_report.inventory import Inventory
from datetime import date
from collections import Counter


class SimpleReport(Report):

    def __init__(self):
        self.Reports = []

    def add_inventory(self, inventory: Inventory):
        self.Reports.append(inventory)

    def generate(self) -> str:
        closestdate = ""
        maior = ""
        FabricacaoAntiga = ""

        produtos = []

        # Gathering all the products into the inventories
        for inventory in self.Reports:
            produtos.extend(inventory.data)

        hoje = date.today()

        # ----- Oldest manufacturing date -----
        for c in range(0, len(produtos)):
            if c == 0:
                FabricacaoAntiga = produtos[c]["data_de_fabricacao"]
            elif produtos[c]["data_de_fabricacao"] < FabricacaoAntiga:
                FabricacaoAntiga = produtos[c]["data_de_fabricacao"]

        # ----- Closest date of expiration -----
        for c in range(0, len(produtos)):
            validade = date.fromisoformat(produtos[c]["data_de_validade"])
            if validade >= hoje:
                if closestdate == "":
                    closestdate = produtos[c]["data_de_validade"]
                elif produtos[c]["data_de_validade"] < closestdate:
                    closestdate = produtos[c]["data_de_validade"]

        # ----- Company With the biggest inventory -----
        empresas = []
        for c in range(0, len(produtos)):
            empresas.append(produtos[c]["nome_da_empresa"])

        contador = Counter(empresas)
        maior = contador.most_common(1)[0][0]

        return (
            f"Oldest manufacturing date: {FabricacaoAntiga}\n"
            f"Closest expiration date: {closestdate}\n"
            f"Company with the largest inventory: {maior}")