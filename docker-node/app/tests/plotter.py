import matplotlib.pyplot as plt




def plot(drag_lift_array, angle_array):
    plt.xlabel('Angle')
    plt.ylabel('Lift/Drag Ratio')
    plt.title('The Lift/Drag Ratio for different angles')
    plt.plot(angle, drag_lift)
    plt.show()
    plt.savefig('lift/drag_ratio.png')



#Test Values.
drag_lift = [0.8, 1.3, 1.4, 2.1, 2.4, 1.7]
angle = [0,1, 5, 10, 15, 20]
plot(drag_lift, angle)
