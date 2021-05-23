import random 

# Starting questions
# This would be on the site in an html text box
numQuestions = int(input("How many questions do you want? ")) #done in front-end, as a numeric keypad or scrolling thing, or perhaps infinite?
#element = ["name", "symbol", period, group, state, name, reactivity, most common charge]
hydrogen = ["hydrogen", "H", 1, 1, "gas", "hydride", 2, 1] #HOFBRINCL
helium = ["helium", "He", 1, 8, "gas", None, None, None] #Noble
lithium = ["lithium", "Li", 2, 1, "solid", None, 8, 1]
beryllium = ["beryllium", "Be", 2, 2, "solid", None, 5, 2]
boron = ["boron", "B", 2, 3, "solid", None, 1, 3]
carbon = ["carbon", "C", 2, 4, "solid", "carbide", 3, -4]
nitrogen = ["nitrogen", "N", 2, 5, "gas", "nitride", None, -3] #HOFBRINCL
oxygen = ["oxygen", "O", 2, 6, "gas", "oxide", None, -2] #HOFBRINCL
fluorine = ["fluorine", "F", 2, 7, "gas", "fluoride", 3, -1] #HOFBRINCL
neon = ["neon","Ne", 2, 8, "gas", None, None, None] #Noble
sodium = ["sodium", "Na", 3, 1, "solid", None, 9, 1]
magnesium = ["magnesium","Mg", 3, 2, "solid", None, 6, 2]
aluminum = ["aluminum", "Al", 3, 3, "solid", None, 4, 3]
silicon = ["silicon", "Si", 3, 4, "solid", None, 0, 4] #What is the charge of a silicon ion? 
phosphorous = ["phosphorous", "P", 3, 5, "solid", "phosphide", 0, -3]
sulfur = ["sulfur", "S", 3, 6, "solid", "sulfide", 0, -2]
chlorine = ["chlorine", "Cl", 3, 7, "gas", "chloride", 4, -1] #HOFBRINCL
argon = ["argon", "Ar", 3, 8, "gas", None, None, None] #Noble
potassium = ["potassium", "K", 4, 1, "solid", None, 10, 1]
calcium = ["calcium", "Ca", 4, 2, "solid", None, 7, 2]
bromine = ["bromine", "Br", 4, 7, "liquid", "bromide", 2, -1] #HOFBRINCL
iodine = ["iodine", "I", 5, 7, "solid", "iodide", 1, -1] #HOFBRINCL
ELEMENTS = [hydrogen, helium, lithium, beryllium, boron, carbon, nitrogen, oxygen, fluorine, neon, sodium, magnesium, aluminum, silicon, phosphorous, sulfur, chlorine, argon, potassium, calcium]
HOFBRINCL = [hydrogen, oxygen, fluorine, bromine, iodine, nitrogen, chlorine]
 
nitrate = ["NO3", -1]
chloride= ["Cl", -1]
sulfate = ["SO4", -2]
acetate = ["C2H3O2", -1]
sodium_ion = ["Na", 1]
potassium_ion = ["K", 1]
ammonium = ["NH4", 1]
carbonate = ["CO3", -2]
phosphate = ["PO4", -3]
hydroxide = ["OH", -1]
sulfide = ["S", -2]
IONS = [nitrate, chloride, sulfate, acetate, sodium_ion, potassium_ion, ammonium, carbonate, phosphate, hydroxide, sulfide]
 
#Various metal ions
lead_ion = ["Pb", 2]
copper_ion = ["Cu", 1]
silver_ion = ["Ag", 1]
mercury_ion = ["Hg", 2]
calcium_ion = ["Ca", 2]
strontium_ion = ["Sr", 2]
barium_ion = ["Ba", 2]

metal_ions = [lead_ion , silver_ion, mercury_ion, calcium_ion, strontium_ion, barium_ion]
 
all_ions = metal_ions + IONS
ALL = ELEMENTS + IONS
Group1 = []
Group2 = []
 
#list of ions
for i in ELEMENTS:
   if i[2] == 1:
       Group1.append(i)
   if i[2] == 2:
       Group2.append(i)

#print(Group1, Group2)

metals = []

#list of metals
for i in ELEMENTS:
  if i[4] == "solid":
    metals.append(i)
#halogens
halogens = []
for i in ELEMENTS:
  if i[3] == 7:
    halogens.append(i)

#Noble
Noble = []
for i in ELEMENTS:
  if i[3] == 8:
    Noble.append(i)
    ELEMENTS.remove(i)
#cation
cation = []
for i in ELEMENTS:
  if i[3] < 4:
    cation.append(i)
#print(cation)    
#anion
anion = []
for i in ELEMENTS:
  if i[3] >= 4:
    anion.append(i)
#print(anion)
anion.remove(silicon)

synth_negative = []
synth_positive = []
for i in ELEMENTS:
  if i[7] > 0:
    synth_positive.append(i)
  else:
    synth_negative.append(i)
#print(synth_negative, "\n", synth_positive)
#print(metals)
'''
for i in IONS:
 for j in all_ions:
   print(solubility(i, j))
'''
 
HOFBRINCL = [hydrogen, oxygen, fluorine, bromine, iodine, nitrogen, chlorine]

#Should this not also require a function to balance them, using the known charges of the ions? I could write them in, and a simple code to iterate through to find the appropriate charge; AlCl3, for instance, aluminum +3 and chlorine -1; for i in range(aluminum[charge]): charge = i; a = charge_of_the_other; a += a; if a = charge: return a #this goes to the prefix code# else: i += 1 #and the loop increases by one. This should, in theory, allow for more complex compounds with odd charges, such as Al2O3.  
#Greek Prefixes

def pre1(element1):
  n1 = abs(element1[7])
  return n1

def pre2(element2):
  n2 = abs(element2[7])
  return n2

def problem_type():
 #reactions = ["SD", "DD", "Synth", "Decomp"]
 reactions = ["Synth", "Decomp", "SD"]
 return random.choice(reactions)
 
def SD_name():
  x = random.randrange(0,1)
  if x == 0:
    metal1 = random.choice(metals)
    metal2 = random.choice(metals)
    if metal1 == metal2:
      SD_name()
    else:
      anion1 = random.choice(anion)
      print(metal1[0], "+", metal2[0], anion1[5], "-->")
      if metal1[6] > metal2[6]:
        answer = (metal2[0], "+", metal1[0], anion1[5])
        print("{} {}{}".format(metal2[0], "+", metal1[0], anion1[5]))
      else:
        print("No reaction occurs.")
  if x == 1:
    halogen1 = random.choice(halogens)
    halogen2 = random.choice(halogens)
    if halogen1 == halogen2:
      SD_name()
    else:
      cation1 = random.choice(cation)
      print(halogen1[0], "+", halogen2[0], cation1[4], "-->")
      if halogen1[6] > halogen2[6]:
        print("{} + {}{}".format(halogen2[0], "+", halogen1[0], cation1[4]))
      else:
        print("No reaction occurs.")
  return 1
 
def DD_name():
 
 return 1
 
def Synth_name():
  element0 = random.choice(synth_negative)
  element1 = random.choice(synth_positive)
  if element0 == element1:
    Synth_name()
  else:
    #add function to balance the thing to be electrically neutral, using ionic charges, to be added as the 8th element of the list. From this, find the Greek prefix. 
    n2 = pre1(element1)
    n1 = pre1(element0)
    if n1 == n2:
      n1 == ''
      n2 = "mono"
    
    if n2 == 1:
      n2 = "mono"
    if n2 == 2:
      n2 = "di"
    if n2 == 3:
      n2 = "tri"
    if n2 == 4:
      n2 = "tetra"
    if n2 == 5:
      n2 = "penta"

    if n1 == 1:
      n1 = ''
    if n1 == 2:
      n1 = "di"
    if n1 == 3:
      n1 = "tri"
    if n1 == 4:
      n1 = "tetra"
    if n1 == 5:
      n1 = "penta"
    
  print("{} + {} -->".format(element1[0], element0[0], end = ''))
  print("{}{} {}{}".format(n1, element1[0], n2, element0[5]))
  return 1
 
def Decomp_name():
  #This is just the reverse of the Synth_name() function, link it to that and reverse the order. 
  element0 = random.choice(synth_negative)
  element1 = random.choice(synth_positive)
  if element0 == element1:
    Decomp_name()
  else: 
    n2 = pre1(element1)
    n1 = pre1(element0)
    if n1 == n2:
      n1 == ''
      n2 = "mono"
    
    if n2 == 1:
      n2 = "mono"
    if n2 == 2:
      n2 = "di"
    if n2 == 3:
      n2 = "tri"
    if n2 == 4:
      n2 = "tetra"
    if n2 == 5:
      n2 = "penta"

    if n1 == 1:
      n1 = ''
    if n1 == 2:
      n1 = "di"
    if n1 == 3:
      n1 = "tri"
    if n1 == 4:
      n1 = "tetra"
    if n1 == 5:
      n1 = "penta"

  print("{}{} {}{} -->".format(n1, element1[0], n2, element0[5], end = ''))
  print("{} + {}".format(element1[0], element0[0]))


for i in range(numQuestions):
  x = problem_type()
  if x == "SD":
    SD_name()
  if x == "DD":
    DD_name()
  if x == "Synth":
    Synth_name()
  if x == "Decomp":
    Decomp_name()
