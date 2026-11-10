#!/usr/bin/env python3
"""
Eukaryotic Ribosomal Viscoelastic Shunt (ERVS) - Advanced Visual Simulation
Models stress-triggered perinuclear phase-locking under hydrodynamic shear vectors
and generates visual stress vs. impedance curves.
"""

import math

def run_simulation_and_plot():
    # Attempt import of matplotlib for plotting
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("[!] Matplotlib not installed. Run 'pip install matplotlib' to generate charts.")
        plt = None

    print("--- ERVS BIOMECHANICAL SHUNT SIMULATION v2.0 ---")
    
    # Parameters
    lamina_threshold_mpa = 4.5  # Envelope rupture threshold (MPa)
    baseline_density = 5.0      # Ribosomal density (particles/um^3)
    
    # Generate data points across shear gradient (0 to 8 MPa)
    shear_vectors = [i * 0.1 for i in range(0, 81)]
    impedance_curve = []
    
    for shear in shear_vectors:
        if shear >= lamina_threshold_mpa * 0.7:
            # Non-linear shear-thickening phase change (viscoelastic impedance surge)
            z_impedance = (baseline_density * 14.2) * (1 + math.log10(1 + (shear - 3.15)))
        else:
            # Baseline fluid state
            z_impedance = baseline_density * 1.5
        impedance_curve.append(z_impedance)

    print(f"[*] Simulation complete. Threshold: {lamina_threshold_mpa} MPa.")
    print(f"[*] Peak Viscoelastic Impedance: {max(impedance_curve):.2f} kPa·s")

    # Generate Chart if matplotlib is available
    if plt:
        plt.figure(figsize=(8, 5))
        plt.plot(shear_vectors, impedance_curve, label="Viscoelastic Impedance (Z)", color="#d9534f", linewidth=2.5)
        plt.axvline(x=lamina_threshold_mpa * 0.7, color="#f0ad4e", linestyle="--", label="Shunt Trigger (3.15 MPa)")
        plt.axvline(x=lamina_threshold_mpa, color="#d9534f", linestyle=":", label="Lamina Rupture Point (4.5 MPa)")
        
        plt.title("ERVS Phase-Locking: Hydrodynamic Shear vs. Perinuclear Impedance", fontsize=12, fontweight='bold')
        plt.xlabel("Hydrodynamic Shear Stress Vector (MPa)", fontsize=10)
        plt.ylabel("Viscoelastic Impedance Z (kPa·s)", fontsize=10)
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.legend(loc="upper left")
        
        output_filename = "ervs_phase_diagram.png"
        plt.savefig(output_filename, dpi=300, bbox_inches='tight')
        print(f"[+] Saved high-res plot to '{output_filename}'")
        plt.show()

if __name__ == "__main__":
    run_simulation_and_plot()