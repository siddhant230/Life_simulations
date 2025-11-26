import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import json
from src.worlds.simple_vector_world import SimpleVectorWorld  # Import the world module


class FreeWillSimulation:
    def __init__(self, N, K, RANDOM_SAMPLE_SIZE, FREE_WILL_CHOICE, ACTION_SET):
        self.N = N
        self.K = K
        self.FREE_WILL_CHOICE = FREE_WILL_CHOICE
        self.ACTION_SET = ACTION_SET
        self.SAMPLE_SIZE = RANDOM_SAMPLE_SIZE
        # Initialize the SimpleVectorWorld
        self.world = SimpleVectorWorld(N, ACTION_SET)

        self.init_simulation()
        # Initialize final_states to ensure it exists before run_simulation
        self.final_states = self.initial_states.copy()

    def init_simulation(self):
        np.random.seed(42)
        self.world.initialize_actors()
        self.k_indices = np.random.choice(self.N, size=self.K, replace=False)
        self.initial_states = self.world.initial_states.copy()

    def run_step(self):
        """Applies the 'Free Will' override to the deterministic baseline."""
        deterministic_states = self.world.initial_states.copy()
        self.final_states = deterministic_states.copy()
        self.final_states[self.k_indices] = self.FREE_WILL_CHOICE
        self.world.current_states = self.final_states.copy()

    def calculate_percentages(self):
        self.baseline_percentage = (
            np.sum(self.initial_states == self.FREE_WILL_CHOICE) / self.N) * 100
        self.majority_percentage = (
            np.sum(self.final_states == self.FREE_WILL_CHOICE) / self.N) * 100

        np.random.seed(None)  # Allow for true randomness in sampling
        random_sample_indices = np.random.choice(
            self.N, size=self.SAMPLE_SIZE, replace=False)
        random_sample = self.final_states[random_sample_indices]

        self.random_percentage = (
            np.sum(random_sample == self.FREE_WILL_CHOICE) / self.SAMPLE_SIZE) * 100

    def calculate_free_will_influence(self):
        self.free_will_influence = self.majority_percentage - self.baseline_percentage
        self.random_influence = self.random_percentage - self.baseline_percentage

    def prepare_data_for_plotting(self):
        self.data_baseline = [self.baseline_percentage,
                              self.baseline_percentage, self.baseline_percentage]
        self.data_influence = [
            0, self.free_will_influence, self.random_influence]
        self.df = pd.DataFrame({
            'Method': ['Baseline', 'Majority (Actual)', 'Random Sample (Perceived)'],
            'Baseline': self.data_baseline,
            'Free Will Influence': self.data_influence
        })

    def plot_stacked_bars(self, filename, save_dir="output"):
        plt.figure(figsize=(12, 7))

        bars_baseline = plt.bar(
            self.df['Method'], self.df['Baseline'], color='gray', label='Deterministic Baseline')
        bars_influence = plt.bar(self.df['Method'], self.df['Free Will Influence'],
                                 bottom=self.df['Baseline'], color='darkblue', label='Free Will Influence')

        # Add Total Labels
        for i, bar in enumerate(bars_influence):
            total_height = self.df['Baseline'][i] + \
                self.df['Free Will Influence'][i]
            plt.text(bar.get_x() + bar.get_width()/2, total_height + 0.5,
                     f'{total_height:.2f}%', ha='center', va='bottom', fontsize=10)

        # Add Influence Labels
        for i, bar in enumerate(bars_influence):
            influence_height = self.df['Free Will Influence'][i]
            if influence_height > 0.05:
                text_y = bar.get_y() + bar.get_height() / 2
                label = f'+{influence_height:.2f}%'
                if i == 1:
                    label += '\n(Free Will)'
                plt.text(bar.get_x() + bar.get_width()/2, text_y, label, ha='center',
                         va='center', color='white', fontweight='bold', fontsize=9)

        plt.title(
            f'Free Will Impact vs. Deterministic Baseline (N={self.N:,}, K={self.K:,})')
        plt.ylabel(f'Percentage of States set to "{self.FREE_WILL_CHOICE}"')
        max_total = max(self.df['Baseline'] + self.df['Free Will Influence'])
        plt.ylim(0, max_total * 1.2)
        plt.legend(loc='upper left')
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        # os.makedirs(save_dir, exist_ok=True)
        plot_filename_stacked = f'{save_dir}/{filename}/{filename}_simulation.png'
        print("##", plot_filename_stacked)
        plt.savefig(plot_filename_stacked)
        plt.close()

    def save_fields(self, run_name, save_dir=None):
        fields = {
            'N': self.N,
            'K': self.K,
            'FREE_WILL_CHOICE': self.FREE_WILL_CHOICE,
            'ACTION_SET': self.ACTION_SET.tolist(),
            'RANDOM_SAMPLE_SIZE': self.SAMPLE_SIZE,
            'baseline_percentage': float(self.baseline_percentage),
            'majority_percentage': float(self.majority_percentage),
            'random_percentage': float(self.random_percentage),
            'free_will_influence': float(self.free_will_influence),
            'random_influence': float(self.random_influence)
        }
        with open(f'{save_dir}/{run_name}/fields.json', 'w') as f:
            json.dump(fields, f, indent=4)

    def run_simulation(self, run_name, show_metrics=True, save_dir=None):
        """Main method to run a single instance of the simulation."""
        print(f"--- Running Simulation: {run_name} ---")

        self.init_simulation()
        self.run_step()

        self.calculate_percentages()
        self.calculate_free_will_influence()
        self.prepare_data_for_plotting()
        print("****", save_dir)
        self.plot_stacked_bars(run_name, save_dir=save_dir)
        self.save_fields(run_name, save_dir=save_dir)

        if show_metrics:
            print("\n--- Results Summary ---")
            print(f"Directory Created: {run_name}")
            print(f"Baseline Percentage: {self.baseline_percentage:.4f}%")
            print(
                f"Actual Free Will Influence (Majority): +{self.free_will_influence:.4f}%")
            print(
                f"Perceived Free Will Influence (Random Sample): +{self.random_influence:.4f}%")
            print(f"Plot saved to: {run_name}/{run_name}_simulation.png")

        return self.df
