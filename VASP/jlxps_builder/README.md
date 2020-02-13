# jlxps_builder scripts
This script helps you to extract the half-core hole eigenenergies using pseudopotentials. The script help you to setup the calculations and convolve the discrete signals with gaussians to generate the core hole eigenenergies.

First you need to create a folder xps-icorelevel10-static with the main POSCAR, INCAR, KPOINTS, POTCAR and *.sh to submit your calculations. Please check the example of a Ruthenium Complex with +2 charge.

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


