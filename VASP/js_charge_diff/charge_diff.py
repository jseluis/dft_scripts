###################
## Ph.D. Jose Luis L.J. Silva - "Freedom & Independence are the key ;)"
## If you want to know more about me and my work: https://jseluis.github.io/
###################

import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# This script saves *.eps and *.png as default.

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="Folder with files ACF.dat and POSCAR")
ap.add_argument("-g", "--greater", required=False, help="Return the atoms with valence charge difference which are greater than a specified value")
ap.add_argument("-l", "--lower", required=False, help="Return the atoms with valence charge difference which are lower than a specified value")
args = vars(ap.parse_args())


folder = args['input']
filename = folder+'ACF.dat'
filename_poscar = folder+'POSCAR'

with open(filename) as f:
    content = f.readlines()
# You may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

with open(filename_poscar) as poscar:
        content_poscar = poscar.readlines()
content_poscar = [y.strip() for y in content_poscar]

### Returns the valence for each element. If your elements are not defined, please add it based on the pseudopotentials
### that you used to perform the simulations

def charge_values(element):
    x = {'Au':11.,'C':4,'H':1,'N':5}
    return x[element]

##
poscar_values = []
start_poscar = 5
for value in range(2):
    for sub_values in content_poscar[start_poscar+value].split():
            poscar_values.append(sub_values)

poscar_values = np.array(poscar_values)
poscar_values = np.reshape(poscar_values,(2,-1))

## Based on the formatting of ACF.dat
charge_col = 5
columns = 7
jump = 2 # Don't change - Based on the file formatting
values = []
for j in range(len(content)-6):
    for word in content[j+jump].split():
            values.append(word)


array_content = np.array([values], dtype=np.float32)
array_content = np.reshape(array_content, (-1,columns))


y=array_content[:,charge_col-1]
x = np.arange(1, len(array_content)+1)

## Plot the charge distribution
#figure=plt.figure(num=None, figsize=(8, 6), dpi=80)
#plt.scatter(x,y,alpha=0.5,color = 'blue',linewidths=10,s = 10)

## Trick for the loops
x1 = ([0])
x2=np.array(poscar_values[1][:],dtype=np.int)
start = np.append(x1,x2)
for i in range(start.shape[0]-1):
    start[i+1] = start[i]+ start[i+1]
start = start[0:-1]

## Number of elements should be less or equal to 8. These are the possible colors for the plot.
colors = "bgrcmykw"
color_index = 0
poscar_legend = []
figure=plt.figure(num=None, figsize=(8, 6), dpi=80)
plt.ylabel('Valence charge difference (a.u)')
plt.xlabel('Atom')

## Main loop to calculate the charges and plot
diff_charge = np.copy(y)
counter = 0
for j in range(poscar_values.shape[1]):
    #print('Number of elements: ',poscar_values[1][j])
    #print('Valence Charge:',charge_values(poscar_values[0][j]))
    number_of_elements = poscar_values[1][j]
    charge_value = charge_values(poscar_values[0][j])
    for k in range(int(number_of_elements)):
        diff_charge[counter] = charge_value - diff_charge[counter]
        #print('k: ',k,"charge_diff: ",diff_charge[counter],'counter: ',counter)
        counter += 1
    poscar_legend.append(poscar_values[0][j])

    plt.scatter(x[start[j]:counter],diff_charge[start[j]:counter],alpha=0.7,c=colors[color_index],linewidths=10,s = 10)
    color_index += 1

plt.legend(poscar_legend)
plt.axhline(y=0.0, color='black', linestyle='--',alpha=.4)
plt.savefig(folder+"charge_diff.png", # file name
            dpi = 300,  # dot per inch for resolution increase value for more resolution
            quality = 300,
            format='png' # "1 <= value <= 100" 100 for best qulity
           )
plt.show()
plt.savefig(folder+"charge_diff.eps", # file name
            dpi = 300,  # dot per inch for resolution increase value for more resolution
            quality = 300,
            format='eps' # "1 <= value <= 100" 100 for best qulity
           )

if args['greater'] == None and args['lower'] == None:
    print('Great, Now check your folder ! There you can find *.png and *.eps plots')

elif args['greater']!= None:
    filter_charge = float(args['greater'])
    for i,j in enumerate(diff_charge):
        if j>filter_charge:
            print("Atom number:",i,"; Charge Difference: ",j,"(a.u)")
    print('Great, now check your folder ! There you can find both *.png and *.eps plots')

elif args['lower'] != None:
    filter_charge = float(args['lower'])
    for i,j in enumerate(diff_charge):
        if j<filter_charge:
            print("Atom number:",i,"; Charge Difference: ",j,"(a.u)")
    print('Great, now check your folder ! There you can find both *.png and *.eps plots')
    
print('Developed by Jose Luis Silva - "Freedom & Independence are the key ;)" https://jseluis.github.io/')
