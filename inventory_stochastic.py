"""
Inventory Management - Stochastic Demand Simulation

This script simulates inventory management performance using different
safety stock levels and calculates service metrics (CSL, IFR).
"""

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats


def calculate_reorder_point_csl(D_day, sigma, LD, csl=0.95):
    """
    Calculate reorder point using Cycle Service Level approach.

    CSL = P(demand during LT <= s)
    """
    # Average demand during lead time
    mu_ld = D_day * LD

    # Standard deviation during lead time
    sigma_ld = sigma * math.sqrt(LD)

    # k factor from CSL
    k = stats.norm.ppf(csl)

    # Reorder point
    s = mu_ld + k * sigma_ld

    return s, k, mu_ld, sigma_ld


def calculate_reorder_point_ifr(D_day, sigma, LD, Q, ifr=0.99):
    """
    Calculate reorder point using Item Fill Rate approach.

    IFR = 1 - E(shortage)/Q
    Uses the Unit Normal Loss Function.
    """
    # Average demand during lead time
    mu_ld = D_day * LD

    # Standard deviation during lead time
    sigma_ld = sigma * math.sqrt(LD)

    # Expected shortage per cycle
    expected_shortage = (1 - ifr) * Q

    # Unit normal loss (L(z) = expected_shortage / sigma_ld)
    L_z = expected_shortage / sigma_ld

    # Find k iteratively (simplified)
    for k in np.arange(-3, 4, 0.01):
        # Standard normal loss function: L(z) = phi(z) - z*(1-Phi(z))
        L_k = stats.norm.pdf(k) - k * (1 - stats.norm.cdf(k))
        if L_k <= L_z:
            break

    # Reorder point
    s = mu_ld + k * sigma_ld

    return s, k, mu_ld, sigma_ld


def simulate_inventory(demand, s, Q, initial_inventory=None):
    """
    Simulate inventory levels over time.

    Parameters:
    - demand: array of daily demand
    - s: reorder point
    - Q: order quantity
    - initial_inventory: starting inventory (default: s + Q/2)

    Returns:
    - DataFrame with simulation results
    """
    if initial_inventory is None:
        initial_inventory = s + Q / 2

    n_days = len(demand)
    inventory = np.zeros(n_days)
    stockouts = np.zeros(n_days)
    orders = np.zeros(n_days)

    inventory[0] = initial_inventory
    pending_order = 0
    order_arrival = -1
    LD = 2  # Lead time

    for t in range(1, n_days):
        # Check for order arrival
        if t == order_arrival:
            inventory[t - 1] += pending_order
            pending_order = 0

        # Satisfy demand
        if inventory[t - 1] >= demand[t]:
            inventory[t] = inventory[t - 1] - demand[t]
        else:
            stockouts[t] = demand[t] - inventory[t - 1]
            inventory[t] = 0

        # Check reorder point
        if inventory[t] <= s and pending_order == 0:
            orders[t] = Q
            pending_order = Q
            order_arrival = t + LD

    return pd.DataFrame({
        "day": range(n_days),
        "demand": demand,
        "inventory": inventory,
        "stockouts": stockouts,
        "orders": orders,
    })


def calculate_metrics(simulation_df, Q):
    """Calculate service metrics from simulation."""
    total_demand = simulation_df["demand"].sum()
    total_stockouts = simulation_df["stockouts"].sum()
    n_cycles = simulation_df["orders"].sum() / Q

    # Item Fill Rate
    ifr = 1 - (total_stockouts / total_demand) if total_demand > 0 else 1

    # Cycle Service Level (approx)
    cycles_with_stockout = (simulation_df["stockouts"] > 0).sum()
    csl = 1 - (cycles_with_stockout / max(n_cycles, 1))

    # Average inventory
    avg_inventory = simulation_df["inventory"].mean()

    return {
        "IFR": ifr,
        "CSL": csl,
        "avg_inventory": avg_inventory,
        "total_stockouts": total_stockouts,
        "n_orders": int(simulation_df["orders"].sum() / Q),
    }


def plot_unit_normal_loss_function(Q, sigma_ld, ifr=0.99):
    """
    Plot and save the Unit Normal Loss Function.

    Parameters:
    - Q: Order quantity
    - sigma_ld: Standard deviation during lead time
    - ifr: Item Fill Rate target
    """
    G_k = (Q / sigma_ld) * (1 - ifr)
    print(f"Find k for G(k) = {round(G_k, 3)}")

    # Find k values and G(k)
    l1, l2 = [], []
    for n in range(1, 300):
        k = n * 0.01
        l1.append(k)
        # Unit Normal Loss Function: G(k) = phi(k) - k*(1-Phi(k))
        y = stats.norm.pdf(k) - k * (1 - stats.norm.cdf(k))
        l2.append(y)

    df_result = pd.DataFrame({'k': l1, 'G(k)': l2})
    df_result['delta'] = df_result['G(k)'] - G_k

    # k = min(delta)
    min_delta = df_result['delta'].abs().min()
    k_final = df_result[df_result['delta'].abs() == min_delta]['k'].values[0]
    print(f"Optimal k value = {k_final}")

    # Plot
    fig, ax = plt.subplots(figsize=(12, 8))
    df_result.plot(x="k", y="G(k)", ax=ax, color='blue')
    plt.xlabel('k factor')
    plt.ylabel('G(k)')
    plt.axhline(G_k, color='black', linestyle="--")
    plt.axvline(k_final, color='black', linestyle="--")
    plt.title('Unit Normal Loss Function')
    plt.savefig('unit_normal_loss_function.png', dpi=150, bbox_inches='tight')
    print("Saved visualization to 'unit_normal_loss_function.png'")
    plt.close()

    return k_final


def run_analysis():
    """Run inventory analysis with sample data."""
    print("=" * 60)
    print("INVENTORY MANAGEMENT - STOCHASTIC DEMAND SIMULATION")
    print("=" * 60)

    # Sample parameters
    D_day = 10  # Average daily demand
    sigma = 3   # Standard deviation
    LD = 2      # Lead time (days)
    Q = 50      # Order quantity

    print(f"\nParameters:")
    print(f"  Average daily demand: {D_day} units")
    print(f"  Std deviation: {sigma} units")
    print(f"  Lead time: {LD} days")
    print(f"  Order quantity: {Q} units")

    # Calculate reorder points
    print("\n" + "-" * 60)
    print("REORDER POINT CALCULATIONS")
    print("-" * 60)

    # CSL approach
    s_csl, k_csl, mu_ld, sigma_ld = calculate_reorder_point_csl(
        D_day, sigma, LD, csl=0.95
    )
    print(f"\nCSL Approach (95% service level):")
    print(f"  k = {k_csl:.4f}")
    print(f"  Reorder point (s) = {s_csl:.2f} units")

    # IFR approach
    s_ifr, k_ifr, _, _ = calculate_reorder_point_ifr(
        D_day, sigma, LD, Q, ifr=0.99
    )
    print(f"\nIFR Approach (99% fill rate):")
    print(f"  k = {k_ifr:.4f}")
    print(f"  Reorder point (s) = {s_ifr:.2f} units")

    # Plot Unit Normal Loss Function
    print("\n" + "-" * 60)
    print("UNIT NORMAL LOSS FUNCTION VISUALIZATION")
    print("-" * 60)
    plot_unit_normal_loss_function(Q, sigma_ld, ifr=0.99)

    # Compare different safety factors
    print("\n" + "-" * 60)
    print("SAFETY FACTOR COMPARISON")
    print("-" * 60)

    np.random.seed(42)
    demand = np.random.normal(D_day, sigma, 365).clip(0).astype(int)

    k_values = [0, 1, 2, 3]
    print(f"\n{'k':<5} {'s':<10} {'IFR':<10} {'Avg Inv':<12} {'Stockouts':<12}")
    print("-" * 50)

    for k in k_values:
        s = mu_ld + k * sigma_ld
        sim_df = simulate_inventory(demand, s, Q)
        metrics = calculate_metrics(sim_df, Q)
        print(
            f"{k:<5} {s:<10.1f} {metrics['IFR']*100:<10.2f}% "
            f"{metrics['avg_inventory']:<12.1f} {metrics['total_stockouts']:<12.0f}"
        )


def main():
    """Main function."""
    run_analysis()
    print("\n" + "=" * 60)
    print("SIMULATION COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
