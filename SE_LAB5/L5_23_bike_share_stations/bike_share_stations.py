"""Manage bike-share stations and basic rental operations."""

import secrets
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE stations (id INTEGER PRIMARY KEY, name TEXT, capacity INTEGER, bikes INTEGER)")


def add_station(name, capacity, bikes, log=None):
    """Register a station and append its name to the supplied log."""
    if log is None:
        log = []
    conn.execute("INSERT INTO stations (name, capacity, bikes) VALUES (?, ?, ?)", (name, capacity, bikes))
    log.append(name)
    return log


def rent_bike(station_id):
    """Rent one bike from a station if one is available."""
    row = conn.execute("SELECT bikes FROM stations WHERE id = ?", (station_id,)).fetchone()
    if row is None or row[0] is None or row[0] <= 0:
        return False
    conn.execute("UPDATE stations SET bikes = bikes - 1 WHERE id = ?", (station_id,))
    return True


def unlock_pin():
    """Generate a four-digit security PIN."""
    return secrets.randbelow(9000) + 1000


def full_stations():
    """Return names of stations where all bike docks are occupied."""
    stations = conn.execute("SELECT name FROM stations WHERE bikes = capacity").fetchall()
    return [station[0] for station in stations]


def reset_station(station_id):
    """Reset the available-bike count for a station to zero."""
    conn.execute("UPDATE stations SET bikes = 0 WHERE id = ?", (station_id,))


def has_bikes(station_id):
    """Return whether the specified station has any bikes available."""
    row = conn.execute("SELECT bikes FROM stations WHERE id = ?", (station_id,)).fetchone()
    if row is None or row[0] is None:
        return False
    return row[0] > 0


def main():
    """Run a short demonstration of the bike-share operations."""
    add_station("Central Park", 10, 10)
    add_station("Metro Gate", 8, 2)
    print(rent_bike(2), rent_bike(9))
    print(unlock_pin(), full_stations(), has_bikes(2))
    reset_station(1)


if __name__ == "__main__":
    main()
