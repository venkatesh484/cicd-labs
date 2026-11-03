def disk_usage_status(used_gb: float, total_gb: float) -> str:
    """Return OK / WARNING / CRITICAL based on disk usage percent."""
    if total_gb <= 0:
        raise ValueError("total_gb must be positive")
    pct = used_gb / total_gb * 100
    if pct >= 90:
        return "CRITICAL"
    if pct >= 75:
        return "WARNING"
    return "OK"
