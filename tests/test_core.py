"""Tests for Katha."""
from src.core import Katha
def test_init(): assert Katha().get_stats()["ops"] == 0
def test_op(): c = Katha(); c.generate(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = Katha(); [c.generate() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = Katha(); c.generate(); c.reset(); assert c.get_stats()["ops"] == 0
def test_service_name(): c = Katha(); r = c.generate(); assert r["service"] == "katha"
