import math

def main():

    name = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303" ]
    radius_cm = ["6.83", "7.78", "8.73", "10.32", "10.79", "13.02", "5.40", "6.83", "15.72", "6.83", "7.62", "8.10" ]
    height_cm = ["10.16", "11.91", "11.59", "11.91", "17.78", "14.29", "8.89", "7.62", "17.78", "12.38", "11.27", "11.11" ]

    for i in range(len(radius_cm)):

        storage_efficiency = cylinder_volume(float(radius_cm[i]), float(height_cm[i])) / cylinder_surface_area(float(radius_cm[i]), float(height_cm[i]))

        print(f"{name[i]} {storage_efficiency:.1f}")


def cylinder_volume(radius, height):
    cylinder_volume = math.pi * radius ** 2 * height
    return cylinder_volume

def cylinder_surface_area(radius, height):

    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area



main()