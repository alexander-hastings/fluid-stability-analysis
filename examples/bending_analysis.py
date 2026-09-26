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
tension = 0.0
gravity = 9.81


# ---------------------------------------------------------------------
# Bending-resistance range
# ---------------------------------------------------------------------

bending_values = np.linspace(0.0, 3000.0, 1000)


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
    tension=tension,
    bending=bending_values,
    gravity=gravity,
)


# ---------------------------------------------------------------------
# Find critical bending resistance
# ---------------------------------------------------------------------

def discriminant_at_bending(bending):
    """Evaluate the discriminant at a single bending-resistance value."""

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
    tension=tension,
    bending=bending_values,
    gravity=gravity,
)

sign_changes = np.where(
    np.sign(discriminant_values[:-1])
    != np.sign(discriminant_values[1:])
)[0]

if len(sign_changes) > 0:
    index = sign_changes[0]

    bending_left = bending_values[index]
    bending_right = bending_values[index + 1]

    bending_critical = brentq(
        discriminant_at_bending,
        bending_left,
        bending_right,
    )

    print(
        f"Critical bending resistance: "
        f"K_c = {bending_critical:.6f}"
    )

else:
    bending_critical = None
    print("No stability boundary found in the selected bending range.")


# ---------------------------------------------------------------------
# Plot growth rates
# ---------------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    bending_values,
    omega_plus.imag,
    label=r"$\mathrm{Im}(\omega_+)$",
)

plt.plot(
    bending_values,
    omega_minus.imag,
    label=r"$\mathrm{Im}(\omega_-)$",
)

plt.axhline(
    0,
    linewidth=0.8,
    linestyle="--",
)

if bending_critical is not None:
    plt.axvline(
        bending_critical,
        linewidth=1,
        linestyle="--",
        color="black",
        label=fr"$\bar{{K}}_c = {bending_critical:.2f}$",
    )

plt.xlabel(r"Bending resistance $\bar{K}$")
plt.ylabel(r"$\mathrm{Im}(\omega)$")
plt.title("Growth Rate vs Bending Resistance")

plt.legend()
plt.tight_layout()


# ---------------------------------------------------------------------
# Save figure
# ---------------------------------------------------------------------

os.makedirs("figures", exist_ok=True)

plt.savefig(
    "figures/bending_stability.png",
    dpi=300,
    bbox_inches="tight",
)

plt.show()