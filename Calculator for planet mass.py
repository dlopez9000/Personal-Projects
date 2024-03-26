def calculate_planet_mass(radius, density):
    radius_meters = radius * 1000  # 1 kilometer = 1000 meters

    # Formula for calculating the volume of a sphere: V = 4/3 * π * r^3
    volume = (4 / 3) * 3.14159 * (radius_meters ** 3)

    mass = volume * density
    return mass


def main():

    radius_km = float(input("Enter radius of the planet (in kilometers): "))
    density = float(input("Enter average density of the planet (in kg/m^3): "))

    mass = calculate_planet_mass(radius_km, density)

    print(f"The mass of the planet is: {mass:.2e} kilograms.")


if __name__ == "__main__":
    main()
