import os

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq

from src.dispersion_relation import (
    dispersion_discriminant,
    dispersion_relation,
)


# ---------------------------------------------------------------------
# Model parameters
# ---------------------------------------------------------------------

rho1 = 3.0
rho2 = 1.0

U1 = 5.0
U2 = 2.0

wall_mass = 1.5
tension = 0.1
bending = 0.0
gravity = 9.81


# ---------------------------------------------------------------------
# Wavenumber range
# ---------------------------------------------------------------------

k_values = np.linspace(0.01, 2.0, 1000)


# ---------------------------------------------------------------------
# Evaluate dispersion relation
# ---------------------------------------------------------------------

omega_plus, omega_minus = dispersion_relation(
    k=k_values,
    rho1=rho1,
    rho2=rho2,
    U1=U1,
    U2=U2,
    wall_mass=wall_mass,
    tension=tension,
    bending=bending,
    gravity=gravity,
)


# ---------------------------------------------------------------------
# Find critical wavenumber
# ---------------------------------------------------------------------

def discriminant_at_k(k):
    """Evaluate the discriminant for a single wavenumber."""

    return dispersion_discriminant(
        k=k,
        rho1=rho1,
        rho2=rho2,
        U1=U1,
        U2=U2,
        wall_mass=wall_mass,
        tension=tension,
        bending=bending,
        gravity=gravity,
    )


# Evaluate discriminant over the grid
discriminant_values = dispersion_discriminant(
    k=k_values,
    rho1=rho1,
    rho2=rho2,
    U1=U1,
    U2=U2,
    wall_mass=wall_mass,
    tension=tension,
    bending=bending,
    gravity=gravity,
)

# Find neighbouring grid points where the discriminant changes sign
sign_changes = np.where(
    np.sign(discriminant_values[:-1])
    != np.sign(discriminant_values[1:])
)[0]

if len(sign_changes) > 0:
    index = sign_changes[0]

    k_left = k_values[index]
    k_right = k_values[index + 1]

    # Refine the root using Brent's method
    k_critical = brentq(
        discriminant_at_k,
        k_left,
        k_right,
    )

    print(f"Critical wavenumber: k_c = {k_critical:.6f}")

else:
    k_critical = None
    print("No stability boundary found in the selected range.")


# ---------------------------------------------------------------------
# Plot growth rates
# ---------------------------------------------------------------------

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

plt.axhline(
    0,
    linewidth=0.8,
    linestyle="--",
)

if k_critical is not None:
    plt.axvline(
        k_critical,
        linewidth=1,
        linestyle="--",
        color="black",
        label=fr"$k_c = {k_critical:.3f}$",
    )

plt.xlabel(r"Wavenumber $k$")
plt.ylabel(r"$\mathrm{Im}(\omega)$")
plt.title("Growth Rate vs Wavenumber")

plt.legend()
plt.tight_layout()


# ---------------------------------------------------------------------
# Save figure
# ---------------------------------------------------------------------

os.makedirs("figures", exist_ok=True)

plt.savefig(
    "figures/wavenumber_stability.png",
    dpi=300,
    bbox_inches="tight",
)

plt.show()
