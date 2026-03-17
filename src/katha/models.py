"""Pydantic models for Katha."""
from __future__ import annotations
from pydantic import BaseModel, Field
from enum import Enum


class Source(str, Enum):
    RAMAYANA = "Ramayana"
    MAHABHARATA = "Mahabharata"
    BHAGAVATA_PURANA = "Bhagavata Purana"
    VISHNU_PURANA = "Vishnu Purana"
    SHIVA_PURANA = "Shiva Purana"
    DEVI_BHAGAVATA = "Devi Bhagavata"
    MARKANDEYA_PURANA = "Markandeya Purana"
    PADMA_PURANA = "Padma Purana"
    MATSYA_PURANA = "Matsya Purana"
    GARUDA_PURANA = "Garuda Purana"
    SKANDA_PURANA = "Skanda Purana"
    PANCHATANTRA = "Panchatantra"


class AgeGroup(str, Enum):
    CHILDREN = "children"       # 4-8
    MIDDLE = "middle"           # 8-12
    TEEN = "teen"               # 12-16
    ADULT = "adult"             # 16+
    ALL = "all"


class Character(BaseModel):
    name: str
    aliases: list[str] = Field(default_factory=list)
    description: str
    role: str = ""  # hero, villain, mentor, deity, etc.
    source: list[Source] = Field(default_factory=list)
    relationships: dict[str, str] = Field(default_factory=dict)  # name -> relationship
    key_traits: list[str] = Field(default_factory=list)
    weapons_items: list[str] = Field(default_factory=list)


class Episode(BaseModel):
    title: str
    source: Source
    kanda_parva: str = ""  # Which book/section
    summary: str
    characters: list[str] = Field(default_factory=list)
    moral: str = ""
    age_group: AgeGroup = AgeGroup.ALL
    sequence_order: int = 0


class Story(BaseModel):
    title: str
    source: Source
    summary: str
    episodes: list[Episode] = Field(default_factory=list)
    characters: list[str] = Field(default_factory=list)
    themes: list[str] = Field(default_factory=list)


class Moral(BaseModel):
    story_title: str
    lesson: str
    explanation: str
    life_application: str = ""
