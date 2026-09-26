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

# Identify the onset of instability
growth_rate = omega_plus.imag

unstable = np.where(growth_rate > 1e-8)[0]

if len(unstable) > 0:
    critical_index = unstable[0]
    k_critical = k_values[critical_index]
    print(f"Critical wavenumber: k_c = {k_critical:.4f}")
else:
    k_critical = None
    print("No instability detected in the selected wavenumber range.")

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

if k_critical is not None:
    plt.axvline(
        k_critical,
        linestyle="--",
        linewidth=1,
        label=fr"$k_c \approx {k_critical:.3f}$",
    )

plt.xlabel(r"Wavenumber $k$")
plt.ylabel(r"$\mathrm{Im}(\omega)$")
plt.title("Growth Rate vs Wavenumber")

plt.legend()
plt.tight_layout()
plt.show()
