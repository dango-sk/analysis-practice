strategy_config = {
    "window": 20,
    "num_std": 2,
    "long_allocation_pct": 0.5,
    "short_allocation_pct": 0.5,
    "strength_power": 1.0, # (z_score - std)^strength power 
    "strength_cap": 3.0, # z_score와 std 값의 cap을 둠 , min(z - std , cap)
    "fallback_enabled": True,
    "fallback_top_n": 2,
    "fallback_frac_cap": 0.5,
}