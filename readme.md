# 🌍 Multi-Hop Influence Simulation Repository

This repository explores complex behavioral and philosophical models—such as **Free Will**, **Working Memory**, and **Hierarchical Worldview**—by implementing them within a scalable agent-based simulation framework.

The core objective is to model how localized individual agency interacts with and is perceived within a vast, deterministic causal universe.

-----

## 💡 Core Experiments

This repository houses different simulation experiments, each exploring a foundational philosophical or cognitive model. Detailed explanations are provided in the dedicated documentation within the `docs/` folder (not shown in this file structure).

### [1\. The Multi-Hop Influence Model (Free Will)](docs/free_will.md)

This experiment models **Compatibilism**, demonstrating that **free will** is a genuine, albeit minuscule, input into an overwhelmingly large, deterministic system. The influence is highly localized and rapidly diminishes across the system's vast scale.

### 2\. Working Memory (Future)

Planned experiments will introduce dynamic **memory** storage and recall mechanisms to simulate cognitive limitations and learning in agents.

### 3\. Hierarchical Worldview (Future)

Planned experiments will explore how agents process and interact with the **Vast Causal Universe ($N$)** by imposing layered, **hierarchical worldview** structures instead of a flat vector representation.

-----

## ⚙️ Repository Structure

The code is organized to separate the model's environment (Worlds), the decision-making entities (Actors), and the experimental orchestration (Simulations/Runner).

```
.
├── output/
│   └── FreeWillSimulation_Run/
│       ├── fields.json             # Key simulation metrics and parameters
│       └── FreeWillSimulation_Run_simulation.png # Stacked bar plot of results
├── src/
│   ├── actors/
│   │   └── simple_actor.py         # Basic Actor definition
│   ├── memory/
│   │   └── simple_memory.py        # Placeholder for Working Memory implementation
│   ├── simulations_exps/
│   │   └── free_will.py            # Contains the core Simulation class for the Free Will experiment
│   └── worlds/
│       └── simple_vector_world.py  # Defines the World as a large vector (the N entities)
└── runner.py                       # Main execution file for setting parameters and starting a run
```

-----

## 🚀 Getting Started

### Prerequisites

You need the necessary Python packages installed:

```bash
pip install -r requirements.txt
```

### Running the Simulation

1.  Navigate to the root directory of the repository.
2.  Adjust the simulation parameters ($\mathbf{N}$, $\mathbf{K}$, $\mathbf{RANDOM\_SAMPLE\_SIZE}$, etc.) within `runner.py` to configure the **Free Will** experiment run.
3.  Execute the runner:

<!-- end list -->

```bash
python runner.py
```

### Output

The results—including the final percentage changes and a visualization of the actual vs. perceived free will influence—will be saved in the `output/` directory under a run-specific folder name.

-----

## 🔮 Future Development

This framework is designed to be modular to facilitate more complex behavioral simulations:

  * **Working Memory:** Implement dynamic memory storage and recall for actors (`src/memory`).
  * **Hierarchical Worldview:** Develop actors that process the `SimpleVectorWorld` in an organized, hierarchical manner.
  * **Relations/Communication:** Introduce systems for actors to influence each other (modeling the 1-Hop, 2-Hop influence).