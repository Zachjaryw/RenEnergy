from Ren_Energy_Presentation_Methods import Generate
from pathlib import Path

print('''
--------------------------------------------------------------------------------

Welcome to Ren Energy Presentation Maker

--------------------------------------------------------------------------------

The program is currently using example data in order to create the presentaiton.

--------------------------------------------------------------------------------

The program will give the filepath to the presentaiton when it is complete.

--------------------------------------------------------------------------------

''')

filepath = str(Path.home() / "Downloads") + '/Supplier_and_Factory_Presentation.pptx'
Generate.save_prs(Generate.Generate_Presentation(Generate.example,
                                                 Generate.setupSupplierData(Generate.example)),filepath)
print(f'File has been saved as {filepath}')
