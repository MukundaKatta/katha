"""MoralExtractor identifying life lessons from each story."""
from __future__ import annotations
from ..models import Episode, Moral


class MoralExtractor:
    """Extract and elaborate on life lessons from mythology stories."""

    def extract_moral(self, episode: Episode) -> Moral:
        """Extract the moral lesson from an episode with elaboration."""
        explanation = self._generate_explanation(episode)
        application = self._generate_application(episode)
        return Moral(
            story_title=episode.title,
            lesson=episode.moral or "Every story carries a lesson for those who listen carefully.",
            explanation=explanation,
            life_application=application,
        )

    def _generate_explanation(self, episode: Episode) -> str:
        """Generate an explanation of the moral."""
        moral_lower = (episode.moral or "").lower()
        if "devotion" in moral_lower or "faith" in moral_lower:
            return "This story demonstrates that sincere devotion and unwavering faith create a connection to the divine that transcends all material obstacles. When we surrender with complete trust, we receive protection and grace beyond our imagination."
        elif "duty" in moral_lower or "dharma" in moral_lower:
            return "The concept of dharma - doing what is right regardless of personal cost - is central to this story. It teaches us that fulfilling our responsibilities with integrity, even when difficult, leads to ultimate goodness."
        elif "evil" in moral_lower or "righteousness" in moral_lower:
            return "This story affirms the eternal truth that righteousness, though it may suffer temporarily, will always triumph. Evil, no matter how powerful, contains the seeds of its own destruction."
        elif "love" in moral_lower or "devotion" in moral_lower:
            return "Through this story, we see that love - whether between spouses, parent and child, or devotee and God - is the most transformative force in existence. It can overcome death, move mountains, and bridge the gap between the mortal and divine."
        elif "wisdom" in moral_lower or "knowledge" in moral_lower:
            return "Wisdom, this story teaches, is the greatest treasure. It comes not merely from study but from experience, humility, and the willingness to see truth even when it is uncomfortable."
        elif "courage" in moral_lower or "brave" in moral_lower:
            return "True courage, as shown in this story, is not the absence of fear but the determination to act rightly despite fear. It inspires us to face our own challenges with similar resolve."
        else:
            return f"This story from {episode.source.value} carries profound wisdom about the human condition. The characters and events, though set in mythological times, mirror the challenges and choices we face in our own lives."

    def _generate_application(self, episode: Episode) -> str:
        """Generate practical life application of the moral."""
        moral_lower = (episode.moral or "").lower()
        if "devotion" in moral_lower:
            return "In your daily life, practice single-pointed dedication to your goals and values. When challenges arise, hold firm to your convictions."
        elif "duty" in moral_lower:
            return "Identify your core responsibilities and fulfill them with integrity, without being swayed by what is easy or popular."
        elif "courage" in moral_lower:
            return "Face a fear this week. Take one step toward something you have been avoiding because it seemed too difficult."
        elif "love" in moral_lower:
            return "Express your love and gratitude to someone important in your life today. Do not wait for the perfect moment."
        elif "cooperation" in moral_lower:
            return "Seek collaboration even with those you disagree with. Great achievements often require working with unlikely partners."
        elif "wisdom" in moral_lower:
            return "Seek guidance from someone wiser and more experienced. True learning requires humility."
        else:
            return "Reflect on the choices of the characters in this story. Which qualities do you admire? How can you embody them in your own life?"

    def extract_all_morals(self, episodes: list[Episode]) -> list[Moral]:
        """Extract morals from a list of episodes."""
        return [self.extract_moral(ep) for ep in episodes if ep.moral]
