"""Tests for Katha."""
import pytest
from katha.stories.ramayana import RamayanaStories
from katha.stories.mahabharata import MahabharataStories
from katha.stories.puranas import PuranaStories
from katha.generator.characters import CharacterDatabase
from katha.generator.narrator import StoryNarrator
from katha.generator.morals import MoralExtractor
from katha.models import AgeGroup, Source


class TestRamayanaStories:
    def test_20_plus_episodes(self):
        rs = RamayanaStories()
        assert len(rs.get_all_episodes()) >= 20

    def test_get_episode(self):
        rs = RamayanaStories()
        ep = rs.get_episode("Golden Deer")
        assert ep is not None
        assert "Maricha" in ep.characters

    def test_by_kanda(self):
        rs = RamayanaStories()
        bala = rs.get_by_kanda("Bala")
        assert len(bala) >= 2

    def test_by_character(self):
        rs = RamayanaStories()
        hanuman_eps = rs.get_by_character("Hanuman")
        assert len(hanuman_eps) >= 4

    def test_children_stories(self):
        rs = RamayanaStories()
        kids = rs.get_for_age(AgeGroup.CHILDREN)
        assert len(kids) >= 5


class TestMahabharataStories:
    def test_20_plus_episodes(self):
        ms = MahabharataStories()
        assert len(ms.get_all_episodes()) >= 20

    def test_get_episode(self):
        ms = MahabharataStories()
        ep = ms.get_episode("Dice")
        assert ep is not None

    def test_by_character(self):
        ms = MahabharataStories()
        krishna_eps = ms.get_by_character("Krishna")
        assert len(krishna_eps) >= 3


class TestPuranaStories:
    def test_20_plus_episodes(self):
        ps = PuranaStories()
        assert len(ps.get_all_episodes()) >= 20

    def test_get_episode(self):
        ps = PuranaStories()
        ep = ps.get_episode("Samudra Manthan")
        assert ep is not None

    def test_by_source(self):
        ps = PuranaStories()
        bhagavata = ps.get_by_source(Source.BHAGAVATA_PURANA)
        assert len(bhagavata) >= 5

    def test_children_stories(self):
        ps = PuranaStories()
        kids = ps.get_for_age(AgeGroup.CHILDREN)
        assert len(kids) >= 5


class TestTotalStories:
    def test_60_plus_total(self):
        total = (len(RamayanaStories().get_all_episodes()) +
                 len(MahabharataStories().get_all_episodes()) +
                 len(PuranaStories().get_all_episodes()))
        assert total >= 60


class TestCharacterDatabase:
    def test_50_plus_characters(self):
        db = CharacterDatabase()
        assert db.get_character_count() >= 50

    def test_get_character(self):
        db = CharacterDatabase()
        rama = db.get_character("Rama")
        assert rama is not None
        assert "Raghava" in rama.aliases

    def test_get_by_alias(self):
        db = CharacterDatabase()
        c = db.get_character("Govinda")
        assert c is not None
        assert c.name == "Krishna"

    def test_search(self):
        db = CharacterDatabase()
        results = db.search_characters("warrior")
        assert len(results) >= 3

    def test_by_role(self):
        db = CharacterDatabase()
        heroes = db.get_by_role("hero")
        assert len(heroes) >= 10
        deities = db.get_by_role("deity")
        assert len(deities) >= 10


class TestStoryNarrator:
    def test_narrate_children(self):
        rs = RamayanaStories()
        ep = rs.get_all_episodes()[0]
        narrator = StoryNarrator()
        text = narrator.narrate(ep, AgeGroup.CHILDREN)
        assert "Once upon a time" in text

    def test_narrate_adult(self):
        ms = MahabharataStories()
        ep = ms.get_all_episodes()[0]
        narrator = StoryNarrator()
        text = narrator.narrate(ep, AgeGroup.ADULT)
        assert "contemplation" in text.lower() or "dharma" in text.lower()

    def test_story_intro(self):
        narrator = StoryNarrator()
        intro = narrator.get_story_intro("Ramayana")
        assert "Valmiki" in intro


class TestMoralExtractor:
    def test_extract_moral(self):
        rs = RamayanaStories()
        ep = rs.get_all_episodes()[0]
        extractor = MoralExtractor()
        moral = extractor.extract_moral(ep)
        assert moral.lesson != ""
        assert moral.explanation != ""
        assert moral.life_application != ""

    def test_extract_all(self):
        ps = PuranaStories()
        extractor = MoralExtractor()
        morals = extractor.extract_all_morals(ps.get_all_episodes())
        assert len(morals) >= 15
