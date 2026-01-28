import numpy as np 
import matplotlib.pyplot as plt

# Data was extracted by hand over multiple iterations
# MiniZinc 
minizinc_data = {
    "N": np.array([1, 5, 8, 10, 12, 15, 17, 20, 25]),
    "T (ms)": np.array([228, 240, 254, 260, 270, 300, 370, 561, 688]),
    "label" : "Boolean Minizinc model"
}

# QUBO
qubo_data = { 
    "N" : np.array([1, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 75, 80, 85, 90]),
    "T (microsec)" : np.array([266, 780, 1440, 2320, 3193, 5766, 6915, 16443, 88936, 175888, 329728, 460054, 580126, 702506, 879597]),
    "T (ms)" : np.array([0.266, 0.780, 1.440, 2.320, 3.193, 5.766, 6.915, 16.443, 88.936, 175.888, 329.728, 460.054, 580.126, 702.506, 879.597]),
    "label" : "QUBO model"
}

# Baseline MiniZinc model
baseline_data = {
    "N" : np.array([1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 200, 250, 300, 400]),
    "T (ms)" : np.array([296, 312, 330, 333, 368, 447, 341, 353, 354, 452, 347, 369, 366, 391, 615 ,331, 392, 530, 789, 1448]),
    "label": "Baseline Minizinc model"
}

# Graph variables
IS_LOG_SCALE = False
MODELS_TO_PLOT = [baseline_data, qubo_data]

# Plotting graph
plt.figure(0)
if (IS_LOG_SCALE):
    plt.yscale('log')

for model in MODELS_TO_PLOT:
    plt.plot(model["N"], model["T (ms)"], marker='o', label=model["label"])

plt.xlabel("Number of Queens (N)")
plt.ylabel("Execution Time (ms)")
plt.title("Execution Time vs Number of Queens")
plt.legend()
plt.grid(True)
plt.show()