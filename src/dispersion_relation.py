import numpy as np


def dispersion_relation(
    k,
    rho1,
    rho2,
    U1,
    U2,
    wall_mass,
    tension=0.0,
    bending=0.0,
    gravity=9.81,
):
    """
    Compute the two branches of the dispersion relation.

    Parameters
    ----------
    k : float or np.ndarray
        Wavenumber.
    rho1, rho2 : float
        Fluid densities.
    U1, U2 : float
        Fluid velocities.
    wall_mass : float
        Wall mass parameter.
    tension : float, optional
        Wall tension parameter.
    bending : float, optional
        Wall bending resistance.
    gravity : float, optional
        Gravitational acceleration.

    Returns
    -------
    omega_plus, omega_minus : complex or np.ndarray
        The two frequency branches.
    """

    denominator = rho1 + rho2 + wall_mass

    base_frequency = (
        k * (rho1 * U1 + rho2 * U2) / denominator
    )

    discriminant = (
        k**2
        * (
            (rho1 * U1 + rho2 * U2) ** 2 / denominator**2
            - (rho1 * U1**2 + rho2 * U2**2) / denominator
        )
        + k
        / denominator
        * (
            gravity * (rho1 - rho2)
            + tension * k
            + bending * k**3
        )
    )

    sqrt_discriminant = np.sqrt(discriminant + 0j)

    omega_plus = base_frequency + sqrt_discriminant
    omega_minus = base_frequency - sqrt_discriminant

    return omega_plus, omega_minus
