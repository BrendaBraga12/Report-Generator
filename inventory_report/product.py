from dataclasses import dataclass

@dataclass
class Product:
    id:str
    product_name:str
    company_name:str
    manufacturing_date:str
    expiration_date:str
    serial_number:str
    storage_instructions:str

    def __str__(self):
        return f"The product {self.id} - {self.product_name}, with serial number {self.serial_number}, manufactured on {self.manufacturing_date}by the company {self.company_name}, valid until {self.expiration_date}, must be storage according to the following instructions:{self.storage_instructions}"


if __name__=="__main__":
    product1=Product("01","Farinha","Farinini","01-05-2021","02-06-2023","TY68 409C JJ43 AD1 PL2F","precisar ser armazenado em local protegido da luz.")

print(product1)