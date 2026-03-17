"""StoryNarrator generating age-appropriate retellings."""
from __future__ import annotations
from ..models import Episode, AgeGroup


class StoryNarrator:
    """Generate age-appropriate narrative versions of mythology episodes."""

    def narrate(self, episode: Episode, target_age: AgeGroup = AgeGroup.ALL) -> str:
        """Generate a narration of the episode appropriate for the target age group."""
        if target_age == AgeGroup.CHILDREN:
            return self._narrate_children(episode)
        elif target_age == AgeGroup.TEEN:
            return self._narrate_teen(episode)
        elif target_age == AgeGroup.ADULT:
            return self._narrate_adult(episode)
        return self._narrate_general(episode)

    def _narrate_children(self, episode: Episode) -> str:
        chars = " and ".join(episode.characters[:3])
        opening = f"Once upon a time, in the wonderful world of {episode.source.value}, there was a great story about {chars}.\n\n"
        body = episode.summary + "\n\n"
        moral = f"And the lesson we learn from this story is: {episode.moral}\n" if episode.moral else ""
        closing = "And that's how the story goes! Would you like to hear another?"
        return opening + body + moral + closing

    def _narrate_teen(self, episode: Episode) -> str:
        opening = f"[From {episode.source.value} - {episode.kanda_parva}]\n\n"
        body = episode.summary + "\n\n"
        characters_section = "Key characters: " + ", ".join(episode.characters) + "\n\n"
        moral = f"The moral: {episode.moral}\n\n" if episode.moral else ""
        reflection = "Think about how this story relates to challenges in your own life."
        return opening + body + characters_section + moral + reflection

    def _narrate_adult(self, episode: Episode) -> str:
        opening = f"[{episode.source.value} | {episode.kanda_parva}]\n\n"
        body = episode.summary + "\n\n"
        analysis = f"Central theme: {episode.moral}\n\n" if episode.moral else ""
        characters_section = "Characters involved: " + ", ".join(episode.characters) + "\n\n"
        philosophical = "This episode invites contemplation on the nature of dharma, karma, and the complexities of moral choice."
        return opening + body + analysis + characters_section + philosophical

    def _narrate_general(self, episode: Episode) -> str:
        opening = f"--- {episode.title} ---\nSource: {episode.source.value}"
        if episode.kanda_parva:
            opening += f" ({episode.kanda_parva})"
        opening += "\n\n"
        body = episode.summary + "\n\n"
        moral = f"Moral: {episode.moral}\n" if episode.moral else ""
        return opening + body + moral

    def get_story_intro(self, source_name: str) -> str:
        """Get a thematic introduction for a story source."""
        intros = {
            "Ramayana": "The Ramayana, composed by sage Valmiki, tells the eternal story of Prince Rama's journey - from his divine birth in Ayodhya to his triumphant return after vanquishing the demon king Ravana.",
            "Mahabharata": "The Mahabharata, the longest epic ever written, composed by Vyasa, chronicles the great war between the Pandavas and Kauravas - a tale of duty, honor, betrayal, and the ultimate triumph of dharma.",
            "Puranas": "The Puranas are ancient texts filled with stories of gods, goddesses, sages, and cosmic events that reveal the deepest truths of existence through captivating narratives.",
        }
        return intros.get(source_name, "Step into the timeless world of Indian mythology...")
