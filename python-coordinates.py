import cmath

z = complex(input())
r = abs(z)  # for vlaue of r: Distance of z to origin i.e. Sq.root[(x^2)+(y^2)]
phi = cmath.phase(z)    # phi = counter clockwise angle measured from +ve x-axis to line segment that joins z to the origin.
print(f"{r}\n{phi}")
