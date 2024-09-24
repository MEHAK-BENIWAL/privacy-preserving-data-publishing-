import numpy as np

def laplace_mechanism(value, sensitivity, epsilon):
    """Apply Laplace noise to a value."""
    noise = np.random.laplace(0, sensitivity/epsilon)
    return value + noise

# Apply differential privacy to the 'age' column
df['age_dp'] = df['age'].apply(lambda x: laplace_mechanism(x, sensitivity=1, epsilon=1.0))
