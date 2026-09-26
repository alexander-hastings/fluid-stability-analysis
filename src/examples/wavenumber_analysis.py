import numpy as np
import matplotlib.pyplot as plt

from src.dispersion_relation import dispersion_relation


# Model parameters
rho1 = 3.0
rho2 = 1.0

U1 = 5.0
U2 = 2.0

wall_mass = 1.5
tension = 0.1
bending = 0.0

# Range of wavenumbers
k_values = np.linspace(0.01, 2.0, 1000)


# Evaluate both branches of the dispersion relation
omega_plus, omega_minus = dispersion_relation(
    k=k_values,
    rho1=rho1,
    rho2=rho2,
    U1=U1,
    U2=U2,
    wall_mass=wall_mass,
    tension=tension,
    bending=bending,
)


# Plot the imaginary components
plt.figure(figsize=(8, 5))

plt.plot(
    k_values,
    omega_plus.imag,
    label=r"$\mathrm{Im}(\omega_+)$",
)

plt.plot(
    k_values,
    omega_minus.imag,
    label=r"$\mathrm{Im}(\omega_-)$",
)

plt.axhline(0, linewidth=0.8, linestyle="--")

plt.xlabel(r"Wavenumber $k$")
plt.ylabel(r"$\mathrm{Im}(\omega)$")
plt.title("Growth Rate vs Wavenumber")

plt.legend()
plt.tight_layout()
plt.show()
