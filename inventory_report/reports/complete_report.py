from inventory_report.reports.simple_report import SimpleReport
from datetime import date
from collections import Counter


class CompleteReport(SimpleReport):

    def generate(self) -> str:
        closestdate = ""
        maior = ""
        FabricacaoAntiga = ""

        produtos = []

        # ALL THE INVENTORIES TOGETHER
        for inventory in self.Reports:
            produtos.extend(inventory.data)

        hoje = date.today()

        # ----- OLDEST DATE OF FABRICATION -----
        for c in range(0, len(produtos)):
            if c == 0:
                FabricacaoAntiga = produtos[c]["data_de_fabricacao"]
            elif produtos[c]["data_de_fabricacao"] < FabricacaoAntiga:
                FabricacaoAntiga = produtos[c]["data_de_fabricacao"]

        # ----- CLOSEST DATE OF EXIPRATION -----
        for c in range(0, len(produtos)):
            validade = date.fromisoformat(produtos[c]["data_de_validade"])
            if validade >= hoje:
                if closestdate == "":
                    closestdate = produtos[c]["data_de_validade"]
                elif produtos[c]["data_de_validade"] < closestdate:
                    closestdate = produtos[c]["data_de_validade"]

        # ----- COMPANY WITH THE BIGGEST INVENTORY -----
        empresas = []
        for c in range(0, len(produtos)):
            empresas.append(produtos[c]["nome_da_empresa"])

        contador = Counter(empresas)
        maior = contador.most_common(1)[0][0]

        # ----- DETAILS PER COMPANY -----
        detalhamento = ""
        for empresa, quantidade in contador.items():
            detalhamento += f"- {empresa}: {quantidade}\n"

        return (
            f"Oldest manufacturing date: {FabricacaoAntiga}\n"
            f"Closest expiration date: {closestdate}\n"
            f"Company with the largest inventory: {maior}\n"
            f"Stocked products by company:\n"
            f"{detalhamento.rstrip()}"
        )
     

    
   
        
