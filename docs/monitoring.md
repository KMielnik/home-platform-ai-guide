# Monitoring that helps a household

Monitoring is an evidence system. It should answer “is the important thing
working, and what changed?” without requiring an operator to stare at a wall of
metrics.

## Four useful layers

| Layer | Questions | Example checks |
| --- | --- | --- |
| Reachability | Can the endpoint be reached? | DNS, TCP/HTTPS, Assist endpoint |
| Service health | Is the application ready? | health endpoint, systemd state, container health |
| Data freshness | Is it still doing useful work? | latest backup, last sensor update, queue age |
| Capacity and hardware | Is failure becoming likely? | free space, temperature, memory pressure, battery/UPS |

Record the observation time and the vantage point. A localhost check can pass
while the room, LAN, or remote operator cannot reach the service.

## Alert design

Each alert should answer:

- what is wrong;
- how long it has been wrong;
- why it matters;
- what the first recovery step is;
- where the runbook lives.

Group dependent failures so one dead host does not generate twenty identical
notifications. Keep an audit trail for maintenance and suppress expected
short windows during a planned change.

## Test the monitor

A check is not trusted until it has seen a controlled failure. Stop a disposable
test service, fill a temporary test filesystem, or use a synthetic endpoint;
then confirm the alert and recovery transition. Do not deliberately break the
only home-control path merely to make a dashboard turn red.

## Evidence beats dashboards

Dashboards are for fast orientation. Dated reports, logs, and tests explain
what happened. Keep enough evidence to compare a regression against the last
known-good state, but avoid collecting personal data that no operator needs.

