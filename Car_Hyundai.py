from Vehicles.fourwheeler.Car import Car

if __name__ == "__main__":

    c1 = Car('i10', 'Hyundai')
    print(c1.get_status())

    c1.start()
    print(c1.get_status())

    c1.speedup(90)
    print(c1.get_status())

    c1.slowdown(30)
    print(c1.get_status())

    c1.slowdown(70)
    print(c1.get_status())
