from barcode import EAN13
from barcode.writer import ImageWriter

num_of_barcodes=int(input("How many Barcodes you need?"))
numbers=range(num_of_barcodes)

for i in numbers:
    id=input("Give 12 digit number for your barcode id:")
    my_code=EAN13(id,writer=ImageWriter)
    name=id
    my_code.save(id)