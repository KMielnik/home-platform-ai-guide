# Benchmark the experience you actually need

Model cards and hardware specifications are useful inputs, not an answer. A
voice system is judged by end-to-end interaction: wake-word time, recognition,
intent resolution, response latency, and whether the room can hear the result.

## A small benchmark set

Create a sanitized phrase set covering:

- short one-device controls;
- a room-qualified control;
- a brightness or temperature adjustment;
- a status question;
- a normal conversational question;
- both supported languages and common accents;
- a deliberately ambiguous phrase.

Measure cold and warm latency, success rate, clarification rate, CPU/GPU
memory, power, and failure behavior. Repeat in quiet and realistic noise.

## Compare routing, not just models

Evaluate at least:

```text
local STT → Assist → local TTS
local STT → Assist → cloud conversation → TTS
cloud STT → Assist → cloud conversation → TTS
```

Keep deterministic control out of a comparison if the model is not needed for
it. The best system may use different routes for different intents.

## Record reproducibly

For each run capture model/version, hardware role, language, sample count,
latency percentiles, failure examples without recordings, and date. Do not
publish private audio or unredacted transcripts.

