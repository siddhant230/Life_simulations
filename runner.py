import os
import numpy as np
from src.simulations_exps.free_will import FreeWillSimulation


def main(output_dir="output"):
    # --- Configuration Parameters ---
    N = 100000        # Total States
    K = 250         # Free Will States (10% influence)
    RANDOM_SAMPLE_SIZE = 500  # Observer Sample Size
    FREE_WILL_CHOICE = 'east'
    ACTION_SET = np.array(['east', 'west', 'north', 'south'])
    os.makedirs(output_dir, exist_ok=True)
    RUN_NAME = f'{FreeWillSimulation.__name__}_Run'

    # --- Execution ---
    sim = FreeWillSimulation(
        N=N,
        K=K,
        RANDOM_SAMPLE_SIZE=RANDOM_SAMPLE_SIZE,
        FREE_WILL_CHOICE=FREE_WILL_CHOICE,
        ACTION_SET=ACTION_SET
    )

    results_df = sim.run_simulation(
        RUN_NAME, show_metrics=True, save_dir=output_dir)

    print("\n--- Final Results DataFrame ---")
    print(results_df)


if __name__ == "__main__":
    main()
