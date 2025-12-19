def detect_regressions(current, previous, threshold_ms=0.5):
    delta = current - previous
    return {
        name: val
        for name, val in delta.items()
        if val > threshold_ms
    }
