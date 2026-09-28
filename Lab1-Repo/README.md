# Lab 1 — Requirements Engineering & UML Use-Case Modelling

**Problem Statement #23 — Smart Cities, Transport & Logistics**
**System:** Hyperlocal Courier Dispatch & Tracking Engine

An on-demand package delivery platform that assigns local parcel pickups to the
nearest delivery rider, optimizes multi-stop routing, and enforces OTP
verification at the destination.

## Contents

| Folder | Deliverable |
|---|---|
| `requirements/` | Requirements Table — 5 FRs (FR-001–FR-005) + 2 NFRs (NFR-001–NFR-002) with ID, Type, Description, Priority, Acceptance Criteria, Rationale |
| `diagrams/` | UML Use-Case Diagram (actors, use cases, `«include»` and `«extend»` relationships) |
| `use-case-flow/` | Use-Case Flow Specification for UC-05 (Complete Delivery) — preconditions, postconditions, main success scenario, alternate flow |

## Actors
- **Sender Client** — creates courier requests, tracks delivery
- **Delivery Rider** — accepts matches, executes pickup/route/drop-off
- **Recipient** — verifies destination OTP to confirm delivery

## Use Cases
- UC-01 Request Courier Pickup *(«include» UC-02)*
- UC-02 Match Nearest Rider *(«extend» by UC-03)*
- UC-03 Optimize Multi-Stop Route
- UC-04 Track Delivery Status
- UC-05 Complete Delivery *(«include» UC-06)*
- UC-06 Verify Destination OTP

## Author
[Vaibhava L] — PES University, Dept. of CSE
