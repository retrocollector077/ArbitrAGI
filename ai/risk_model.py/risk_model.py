def should_trade(spread, balance, position_size, params=None):
    """
    Decide whether to proceed with a trade based on risk factors.
    
    Args:
        spread (float): Current spread value.
        balance (float): Available account balance.
        position_size (float): Current position size.
        params (dict): Optional parameters for thresholds.
        
    Returns:
        bool: True if trade is recommended, False otherwise.
    """
    # Default thresholds
    default_params = {
        'min_spread': 0.3,
        'min_balance': 100,
        'max_position': 5,  # Max units of position allowed
    }
    
    if params:
        default_params.update(params)
    
    if spread < default_params['min_spread']:
        return False
    
    if balance < default_params['min_balance']:
        return False
    
    if abs(position_size) >= default_params['max_position']:
        return False
    
    return True