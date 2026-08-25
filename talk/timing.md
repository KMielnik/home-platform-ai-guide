# Timing

The speaker-note durations in [`slides.md`](slides.md) are the source of
truth. There are 35 slides and their notes sum to **39:30 (39.5 minutes)**;
demo and questions are additional time. The exact full-deck section sums are:

| Slides | Note time |
| --- | ---: |
| 1–5 | 5:15 |
| 6–12 | 9:00 |
| 13–20 | 9:15 |
| 21–26 | 7:00 |
| 27–32 | 6:15 |
| 33–35 | 2:45 |
| **1–35** | **39:30** |

## Exact 30:00 slide cut

Present these slide ranges and omit the listed deep dives:

```text
1–13, 15, 17–19, 21–24, 30, 32–35
```

The omitted deep dives are slides 14, 16, 20, 25–29, and 31. Their note time is
9:30, so the remaining slides are exactly **30:00** while preserving the core
voice sequence on slides 21–24. This is a slide-only cut; add demo or questions
only if the event provides extra time.

## Exact 45:00 live-demo variant

Use the full deck except slides 14–16, which removes 3:30 from 39:30 and
leaves 36:00 of slides. Then use:

| Component | Time |
| --- | ---: |
| Slides 1–13 and 17–35 | 36:00 |
| Live demo | 5:00 |
| Questions | 4:00 |
| **Total** | **45:00** |

When live setup is unreliable, use the six-artifact offline fallback in
[`demo-plan.md`](demo-plan.md) for the five-minute demo slot.

## Optional all-slides fallback variant

If every slide is important, use all 39:30 of slides, a 3:00 fallback demo,
and 2:30 of questions:

| Component | Time |
| --- | ---: |
| Slides 1–35 | 39:30 |
| Offline fallback | 3:00 |
| Questions | 2:30 |
| **Total** | **45:00** |

Do not add the demo or questions to the 39:30 slide total when describing the
deck itself.

## Section cues

- Slides 1–5: make the audience recognize the “fun became a platform” moment.
- Slides 6–12: establish the central design pattern and safe agent loop.
- Slides 13–20: show that operations and recovery are part of the product.
- Slides 21–26: make voice and model routing concrete without product worship.
- Slides 27–32: show useful extensions and where human judgment remains.
- Slides 33–35: give attendees an adaptive starting point and a memorable close.
