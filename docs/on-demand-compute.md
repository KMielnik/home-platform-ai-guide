# On-demand compute without turning the home into a mystery

An idle workstation or a machine that is powered only when needed can be a
useful optional worker for model inference, batch jobs, or experiments. It is
not automatically a reason to make home control depend on that machine.

## Separate availability classes

| Class | Must work when worker is off? | Examples |
| --- | --- | --- |
| Core | Yes | lights, locks, safety automations, climate fallback |
| Enhanced | Preferably; degrade clearly | conversational answers, image analysis |
| Batch | No | indexing, benchmarks, model downloads |

Use explicit readiness and shutdown signals. A request should fail with a
useful fallback rather than hanging while a GPU host wakes.

## Power-on sequence

```text
request → check policy and worker availability
        → wake or start worker (if allowed)
        → wait for health and model readiness
        → run bounded job
        → capture result/evidence
        → idle timeout and safe shutdown
```

Document who may wake the worker, what network access it receives, maximum
runtime, power budget, and what happens after a crash. Never put credentials for
host administration into a household voice intent.

## Benchmark the trade-off

Measure wake latency, warm latency, power, cost, noise, and reliability. A
cloud call or a smaller always-on model can be better than a complex wake path
for a five-second household request.

