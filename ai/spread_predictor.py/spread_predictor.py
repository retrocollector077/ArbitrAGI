import numpy as np

def predict_spread(history):
    """
    Calculate a simple trend-to-volatility score for the spread history.
    Args:
        history (list or np.ndarray): List of recent spread values.
        
    Returns:
        float: Score representing trend over volatility. Higher indicates stronger trend.
    """
    if len(history) < 10:
        # Not enough data to analyze
        return 0.0

    # Convert to numpy array for consistency
    data = np.array(history[-10:])

    trend = np.mean(data)
    volatility = np.std(data)

    # Avoid division by zero
    score = trend / (volatility + 1e-6)

    return score