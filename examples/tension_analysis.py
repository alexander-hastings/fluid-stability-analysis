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

k = 0.3

rho1 = 3.0
rho2 = 1.0

U1 = 10.0
U2 = 2.0

wall_mass = 2.5
bending = 0.0
gravity = 9.81


# ---------------------------------------------------------------------
# Tension range
# ---------------------------------------------------------------------

tension_values = np.linspace(0.0, 300.0, 1000)


# ---------------------------------------------------------------------
# Evaluate dispersion relation
# ---------------------------------------------------------------------

omega_plus, omega_minus = dispersion_relation(
    k=k,
    rho1=rho1,
    rho2=rho2,
    U1=U1,
    U2=U2,
    wall_mass=wall_mass,
    tension=tension_values,
    bending=bending,
    gravity=gravity,
)


# ---------------------------------------------------------------------
# Find critical tension
# ---------------------------------------------------------------------

def discriminant_at_tension(tension):
    """Evaluate the discriminant at a single tension value."""

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


discriminant_values = dispersion_discriminant(
    k=k,
    rho1=rho1,
    rho2=rho2,
    U1=U1,
    U2=U2,
    wall_mass=wall_mass,
    tension=tension_values,
    bending=bending,
    gravity=gravity,
)

sign_changes = np.where(
    np.sign(discriminant_values[:-1])
    != np.sign(discriminant_values[1:])
)[0]

if len(sign_changes) > 0:
    index = sign_changes[0]

    tension_left = tension_values[index]
    tension_right = tension_values[index + 1]

    tension_critical = brentq(
        discriminant_at_tension,
        tension_left,
        tension_right,
    )

    print(f"Critical tension: T_c = {tension_critical:.6f}")

else:
    tension_critical = None
    print("No stability boundary found in the selected tension range.")


# ---------------------------------------------------------------------
# Plot growth rates
# ---------------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    tension_values,
    omega_plus.imag,
    label=r"$\mathrm{Im}(\omega_+)$",
)

plt.plot(
    tension_values,
    omega_minus.imag,
    label=r"$\mathrm{Im}(\omega_-)$",
)

plt.axhline(
    0,
    linewidth=0.8,
    linestyle="--",
)

if tension_critical is not None:
    plt.axvline(
        tension_critical,
        linewidth=1,
        linestyle="--",
        color="black",
        label=fr"$T_c = {tension_critical:.2f}$",
    )

plt.xlabel("Wall tension")
plt.ylabel(r"$\mathrm{Im}(\omega)$")
plt.title("Growth Rate vs Wall Tension")

plt.legend()
plt.tight_layout()


# ---------------------------------------------------------------------
# Save figure
# ---------------------------------------------------------------------

os.makedirs("figures", exist_ok=True)

plt.savefig(
    "figures/tension_stability.png",
    dpi=300,
    bbox_inches="tight",
)

plt.show()