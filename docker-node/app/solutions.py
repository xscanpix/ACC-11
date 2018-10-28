import os
  abspath = os.path.abspath('xml')
  for filename in os.listdir('msh/xml'):
    temp = abspath
    solution_name = filename.replace("r0a","")
    solution_name = filename.replace("n200.xml","")
    os.system('./airfoil 10 0.001 10. 1 '+temp+' ' + solution_name):
