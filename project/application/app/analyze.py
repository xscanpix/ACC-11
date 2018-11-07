import os
import matplotlib.pyplot as plt

def calc_drag_lift(file):
    with open(file) as infile:
        rows = infile.readlines()
        #print(rows[len(rows)-1])
        row = rows[len(rows)-1].split("\t")
        lift = row[1]
        drag = row[2].replace("\n","")
        lift = float(lift)
        drag = float(drag)
        lift_drag = lift/drag

        return (lift_drag)
        

def plot(drag_lift, angles):
    plt.xlabel('Angle')
    plt.ylabel('Lift/Drag Ratio')
    plt.title('The Lift/Drag Ratio for different angles')
    plt.plot(angles, drag_lift)
    #plt.show()

    plt.savefig('lift_drag_ratio.png')


def result():
    angles = []
    lift_drag_ratios = []
    for dirName, subdirList, fileList in os.walk("result"):
        for file in fileList:
            if file == "drag_ligt.m":
                angle = dirName.replace("result/r0a","")
                angle = angle.replace("n200_results","")
                angle = int(angle)
                path = os.path.abspath(dirName+"/"+file)
                lift_drag = calc_drag_lift(path)
                angles.append(angle)
                lift_drag_ratios.append(lift_drag)

    plot(lift_drag_ratios, angles)
        
