# js_charge_diff.py
This script plots the valence charge difference using output formatting from a bader analysis using VASP code.

If you want to try, please make sure that valence charges from you pseudopotentials
are inside the dictionary in the main program. If they are not covered, please add it.

## How to add my valence charges ?

For example: If you have 4 Ti and 3 Se, you should edit the js_charge_diff.py such that:

### before editing:

def charge_values(element):
    x = {'Au':11.,'C':4,'H':1,'N':5}
    return x[element]

### after editing:
def charge_values(element):
    x = {'Au':11.,'C':4,'H':1,'N':5, 'Ti':3, 'Se':3}
    return x[element]


## How to run the script ?

### This command will run the script in the folder ./melamine_hex_bader/ and return the atoms where the valence charge difference is greater than .5 (c.u)
python charge_diff.py -i ./melamine_hex_bader/ -g .5

### Important:

-i or --input (mandatory) ; Folder with files ACF.dat and POSCAR.

-g or --greater (not mandatory) ; Return the atoms with valence charge difference which are greater than a specified value.

-l or --lower (not mandatory) ; Return the atoms with valence charge difference which are lower than a specified value"

#### You just need POSCAR and ACF.dat in the folder.


