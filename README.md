# Sensor Event Processing System

A Python-based event processing simulator built to practice **Data Structures, Algorithms, system design, and PostgreSQL integration**.

## Description

The system simulates how sensor events are created, queued, processed, stored, recovered, and persisted in a database.

### Data Structures

* **Circular Queue**: stores incoming events using FIFO
* **Array**: stores recent sensor readings
* **Stack**: supports recovery of the most recently processed event
* **PostgreSQL**: stores persistent event history

## Technologies

* Python
* Pydantic
* PostgreSQL
* psycopg
* Data Structures & Algorithms

## Main Features

* Create and queue sensor events
* Process events using FIFO
* Store recent readings
* Recover the last processed event
* Persist events in PostgreSQL
* Handle queue, stack, and array errors

## Project Structure

```text
sensor-event-processing-system/
├── main.py
├── operations.py
├── schemas.py
├── queue.py
├── customarray.py
├── customstack.py
├── database.py
├── requirements.txt
└── README.md

```

## Status

**In development**

The project is being built incrementally to explore data structures, complexity, failure handling, and practical software design.
