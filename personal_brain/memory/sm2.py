def calculate_sm2(repetitions: int, ease_factor: float, interval_days: float, quality: int):
    """
    SuperMemo-2 (SM-2) Spaced Repetition Algorithm.
    quality: 0-5 grade (5=perfect, 3=pass, 0=total blackout)
    """
    quality = max(0, min(5, quality))
    if quality >= 3:
        if repetitions == 0:
            new_interval = 1.0
        elif repetitions == 1:
            new_interval = 6.0
        else:
            new_interval = interval_days * ease_factor
        new_repetitions = repetitions + 1
    else:
        new_repetitions = 0
        new_interval = 1.0

    # EF' = EF + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02))
    new_ef = ease_factor + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
    new_ef = max(1.3, new_ef)
    return new_repetitions, round(new_ef, 3), round(new_interval, 2)
