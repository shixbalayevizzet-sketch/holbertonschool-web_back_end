#!/usr/bin/env python3
"""Returns schools matching a specific topic."""


def schools_by_topic(mongo_collection, topic):
    """Return list of schools having the given topic."""
    return list(mongo_collection.find({"topics": topic}))
