import pandas as pd

print('''
--------------------------------------------------------------------------------

Welcome to Ren Energy Presentation Maker

--------------------------------------------------------------------------------

The program is currently using example data in order to create the presentaiton.

--------------------------------------------------------------------------------

The program will give the filepath to the presentaiton when it is complete.

--------------------------------------------------------------------------------

''')

factory_data = Generate.example
supplier_data = Generate.setupSupplierData(factory_data)

filepath = str(Path.home() / "Downloads") + '/Supplier_and_Factory_Presentation.pptx'
Generate.save_prs(Generate.Generate_Presentation(),filepath)
print(f'File has been saved as {filepath}')
