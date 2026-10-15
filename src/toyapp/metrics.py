"""Basic throughput metrics. Starting point for work item TOY-1."""


def units_per_hour(units: float, hours: float) -> float:
    """Return units handled per hour.

    Raises ValueError for negative inputs. Zero hours is handled in TOY-1.
    """
    if units < 0 or hours < 0:
        raise ValueError("units and hours must be non-negative")
    return units / hours
