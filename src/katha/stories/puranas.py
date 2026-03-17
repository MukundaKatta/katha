"""PuranaStories with 20+ stories from various Puranas."""
from __future__ import annotations
from ..models import Episode, Source, AgeGroup


class PuranaStories:
    """20+ stories from various Puranas."""

    def __init__(self) -> None:
        self._episodes: list[Episode] = self._load_episodes()

    def _load_episodes(self) -> list[Episode]:
        return [
            Episode(title="Samudra Manthan (Churning of the Ocean)", source=Source.BHAGAVATA_PURANA, kanda_parva="Canto 8", sequence_order=1,
                    summary="Devas and Asuras cooperate to churn the cosmic ocean using Mount Mandara as the churning rod and Vasuki the serpent as the rope. Vishnu as Kurma (tortoise) supports the mountain. Fourteen treasures emerge including Amrit (nectar), Lakshmi, Halahala poison (swallowed by Shiva), and the moon.",
                    characters=["Vishnu", "Shiva", "Lakshmi", "Devas", "Asuras", "Vasuki"], moral="Great achievements require cooperation even between rivals; someone must sacrifice for the greater good", age_group=AgeGroup.CHILDREN),
            Episode(title="Narasimha Avatar - Hiranyakashipu's End", source=Source.BHAGAVATA_PURANA, kanda_parva="Canto 7", sequence_order=2,
                    summary="The demon Hiranyakashipu, granted a boon making him nearly invulnerable, terrorizes the universe. His own son Prahlada is a devoted Vishnu bhakta. After many failed attempts to kill Prahlada, Vishnu appears as Narasimha (half-man, half-lion) and kills Hiranyakashipu at twilight, on a threshold, on his lap - satisfying all conditions of the boon.",
                    characters=["Narasimha", "Prahlada", "Hiranyakashipu", "Vishnu"], moral="No power can protect the unrighteous; devotion to God is the ultimate shield", age_group=AgeGroup.CHILDREN),
            Episode(title="Prahlada's Devotion", source=Source.BHAGAVATA_PURANA, kanda_parva="Canto 7", sequence_order=3,
                    summary="Young Prahlada, son of the demon king, refuses to stop worshipping Vishnu despite his father's threats. He is thrown from cliffs, into fire, given poison, trampled by elephants, and cast into the ocean - but emerges unharmed each time through Vishnu's grace.",
                    characters=["Prahlada", "Hiranyakashipu", "Vishnu"], moral="True faith cannot be shaken by any threat or force", age_group=AgeGroup.CHILDREN),
            Episode(title="Vamana Avatar - Three Steps of Vishnu", source=Source.BHAGAVATA_PURANA, kanda_parva="Canto 8", sequence_order=4,
                    summary="The benevolent demon king Mahabali conquers the three worlds. Vishnu appears as Vamana, a dwarf Brahmin boy, and asks for three paces of land. When granted, Vamana grows cosmic and covers earth and heaven in two steps. For the third, Bali offers his own head. Vishnu sends him to rule Sutala Loka.",
                    characters=["Vamana", "Mahabali", "Vishnu"], moral="True greatness lies in humility and generosity even in defeat", age_group=AgeGroup.CHILDREN),
            Episode(title="Krishna's Birth and Escape from Mathura", source=Source.BHAGAVATA_PURANA, kanda_parva="Canto 10", sequence_order=5,
                    summary="Krishna is born in prison to Devaki and Vasudeva while the tyrant Kamsa waits to kill him. At midnight, the prison doors open, guards fall asleep, and Vasudeva carries baby Krishna across the flooding Yamuna river to safety in Gokul with Nanda and Yashoda.",
                    characters=["Krishna", "Vasudeva", "Devaki", "Kamsa", "Yashoda"], moral="Divine providence protects the righteous even in the darkest hour", age_group=AgeGroup.CHILDREN),
            Episode(title="Krishna and Putana", source=Source.BHAGAVATA_PURANA, kanda_parva="Canto 10", sequence_order=6,
                    summary="The demoness Putana, sent by Kamsa, disguises herself as a beautiful woman and tries to poison baby Krishna through her breast milk. The infant Krishna sucks the life out of her instead. Her enormous body falls, and the villagers are amazed.",
                    characters=["Krishna", "Putana", "Kamsa", "Yashoda"], moral="Evil disguised as kindness is still recognized and defeated by the divine", age_group=AgeGroup.CHILDREN),
            Episode(title="Krishna Lifts Govardhan", source=Source.BHAGAVATA_PURANA, kanda_parva="Canto 10", sequence_order=7,
                    summary="When young Krishna convinces the villagers to worship Govardhan Hill instead of Indra, the furious rain god unleashes a devastating storm. Krishna lifts the entire Govardhan mountain on his little finger and shelters all of Vrindavan underneath for seven days.",
                    characters=["Krishna", "Indra", "Nanda"], moral="True protection comes from righteousness, not from fear of powerful beings", age_group=AgeGroup.CHILDREN),
            Episode(title="Krishna's Ras Leela", source=Source.BHAGAVATA_PURANA, kanda_parva="Canto 10", sequence_order=8,
                    summary="On a full moon night in autumn, Krishna plays his flute and the gopis of Vrindavan are drawn to him. He multiplies himself to dance with each gopi individually. This cosmic dance represents the soul's longing for union with the divine.",
                    characters=["Krishna", "Radha", "Gopis"], moral="Divine love transcends all worldly attachments; God reciprocates every soul's devotion", age_group=AgeGroup.TEEN),
            Episode(title="Ganesha Gets His Elephant Head", source=Source.SHIVA_PURANA, kanda_parva="Rudra Samhita", sequence_order=9,
                    summary="Parvati creates a boy from turmeric paste to guard her bath. When Shiva returns and is denied entry by the boy, a battle ensues and Shiva beheads him. Grief-stricken Parvati demands his revival. Shiva replaces his head with that of the first creature found - an elephant. Thus Ganesha is born.",
                    characters=["Ganesha", "Shiva", "Parvati"], moral="Every obstacle in life has a higher purpose; transformation can come through crisis", age_group=AgeGroup.CHILDREN),
            Episode(title="Ganesha and the Race Around the World", source=Source.SHIVA_PURANA, kanda_parva="Rudra Samhita", sequence_order=10,
                    summary="Shiva and Parvati offer a divine fruit to whichever son circles the world first. Kartikeya rides his peacock around the globe. Ganesha simply walks around his parents and says, 'You are my world.' Impressed, Shiva gives him the fruit.",
                    characters=["Ganesha", "Kartikeya", "Shiva", "Parvati"], moral="Wisdom and devotion triumph over physical prowess", age_group=AgeGroup.CHILDREN),
            Episode(title="The Marriage of Shiva and Parvati", source=Source.SHIVA_PURANA, kanda_parva="Rudra Samhita", sequence_order=11,
                    summary="After Sati's self-immolation, she is reborn as Parvati. To win Shiva, lost in meditation after Sati's death, Parvati performs intense tapas. Kamadeva tries to awaken Shiva's desire but is burnt to ash. Eventually, Shiva is moved by Parvati's devotion and they marry.",
                    characters=["Shiva", "Parvati", "Kamadeva"], moral="True love requires patience and unwavering devotion", age_group=AgeGroup.MIDDLE),
            Episode(title="Durga Slays Mahishasura", source=Source.MARKANDEYA_PURANA, kanda_parva="Devi Mahatmya", sequence_order=12,
                    summary="The buffalo demon Mahishasura, granted the boon that no man or god can kill him, conquers heaven. The gods combine their powers to create Goddess Durga. Armed with weapons from each god, she battles Mahishasura for nine nights and slays him on the tenth day (Vijayadashami).",
                    characters=["Durga", "Mahishasura"], moral="When evil seems invincible, a new form of divine power arises to restore balance", age_group=AgeGroup.CHILDREN),
            Episode(title="The Descent of Ganga", source=Source.BHAGAVATA_PURANA, kanda_parva="Canto 9", sequence_order=13,
                    summary="King Bhagiratha performs extreme penance to bring the heavenly river Ganga to earth to liberate his ancestors' souls. Ganga, proud of her power, threatens to flood earth. Shiva catches her in his matted locks, releasing her gently. Thus Ganga flows on earth.",
                    characters=["Bhagiratha", "Ganga", "Shiva"], moral="Perseverance and humility can move heaven itself", age_group=AgeGroup.CHILDREN),
            Episode(title="Matsya Avatar - The Great Flood", source=Source.MATSYA_PURANA, kanda_parva="Chapter 1-2", sequence_order=14,
                    summary="Vishnu appears as a tiny fish (Matsya) to King Manu. The fish grows enormous and warns of an impending flood. Manu builds a boat, preserving seeds of all life. Matsya guides the boat through the deluge, tying it to a horn on his head. Life is preserved.",
                    characters=["Vishnu", "Manu", "Matsya"], moral="Heeding divine warnings and preparing wisely preserves life", age_group=AgeGroup.CHILDREN),
            Episode(title="Holika and Prahlada", source=Source.BHAGAVATA_PURANA, kanda_parva="Canto 7", sequence_order=15,
                    summary="Hiranyakashipu commands his sister Holika, who has a boon of fire immunity, to sit in a blazing fire holding Prahlada. But Prahlada's devotion to Vishnu protects him while Holika burns instead. This event is celebrated as Holi.",
                    characters=["Prahlada", "Holika", "Hiranyakashipu"], moral="Evil backfires; divine protection cannot be overcome by trickery", age_group=AgeGroup.CHILDREN),
            Episode(title="Dhruva's Penance", source=Source.BHAGAVATA_PURANA, kanda_parva="Canto 4", sequence_order=16,
                    summary="Five-year-old Prince Dhruva, hurt by his stepmother's rejection, goes to the forest to find God. Through intense meditation, he has a vision of Vishnu. Pleased, Vishnu grants him an eternal position as the Pole Star (Dhruva Tara), forever fixed in the sky.",
                    characters=["Dhruva", "Vishnu", "Suniti"], moral="Even a child's sincere devotion moves the divine; determination knows no age", age_group=AgeGroup.CHILDREN),
            Episode(title="The Story of Markandeya", source=Source.MARKANDEYA_PURANA, kanda_parva="Main narrative", sequence_order=17,
                    summary="The sage Markandeya is destined to die at age sixteen. As Yama's noose falls on him, Markandeya clings to the Shivalinga. Lord Shiva appears and kicks Yama, saving Markandeya and granting him immortality. Markandeya becomes Chiranjeevi (immortal).",
                    characters=["Markandeya", "Shiva", "Yama"], moral="Devotion to God conquers even death itself", age_group=AgeGroup.CHILDREN),
            Episode(title="Narada's Cosmic Illusion (Maya)", source=Source.BHAGAVATA_PURANA, kanda_parva="Canto 10", sequence_order=18,
                    summary="Sage Narada asks Vishnu to show him Maya (cosmic illusion). Vishnu asks him to fetch water. Narada meets a girl, marries, has children, builds a life - then a flood destroys everything. He wakes up to find Vishnu smiling beside him. Only moments have passed.",
                    characters=["Narada", "Vishnu"], moral="The material world is an illusion; attachment to it causes suffering", age_group=AgeGroup.ADULT),
            Episode(title="The Churning out of Lakshmi", source=Source.VISHNU_PURANA, kanda_parva="Book 1", sequence_order=19,
                    summary="During the Samudra Manthan, Goddess Lakshmi emerges seated on a lotus from the cosmic ocean. All devas and asuras desire her. Lakshmi chooses Vishnu as her eternal consort, establishing the divine partnership of wealth and preservation.",
                    characters=["Lakshmi", "Vishnu"], moral="True wealth belongs to those who preserve dharma", age_group=AgeGroup.ALL),
            Episode(title="Shiva Drinks the Halahala Poison", source=Source.SHIVA_PURANA, kanda_parva="Rudra Samhita", sequence_order=20,
                    summary="During the churning of the ocean, the deadly Halahala poison emerges, threatening to destroy all creation. Neither devas nor asuras dare touch it. Shiva steps forward and drinks the entire poison. Parvati holds his throat to prevent it from descending, turning his throat blue (Neelakantha).",
                    characters=["Shiva", "Parvati"], moral="True greatness means taking on suffering to protect others", age_group=AgeGroup.CHILDREN),
            Episode(title="The Ten Avatars of Vishnu (Dashavatara)", source=Source.BHAGAVATA_PURANA, kanda_parva="Various", sequence_order=21,
                    summary="Vishnu incarnates in ten forms across cosmic ages: Matsya (fish), Kurma (tortoise), Varaha (boar), Narasimha (man-lion), Vamana (dwarf), Parashurama (warrior sage), Rama (ideal king), Krishna (divine teacher), Buddha (enlightened one), and Kalki (future destroyer of evil).",
                    characters=["Vishnu"], moral="The divine adapts to the needs of each age to restore dharma", age_group=AgeGroup.ALL),
            Episode(title="Sati's Self-Immolation", source=Source.SHIVA_PURANA, kanda_parva="Rudra Samhita", sequence_order=22,
                    summary="Daksha, Sati's father, insults Shiva by not inviting him to a great yajna. Sati goes uninvited and, unable to bear the humiliation of her husband, immolates herself in the sacred fire. Shiva's grief and fury lead to the destruction of the yajna by Virabhadra.",
                    characters=["Sati", "Shiva", "Daksha", "Virabhadra"], moral="Disrespecting a righteous person invites divine wrath; pride destroys families", age_group=AgeGroup.TEEN),
        ]

    def get_all_episodes(self) -> list[Episode]:
        return self._episodes

    def get_episode(self, title: str) -> Episode | None:
        for e in self._episodes:
            if title.lower() in e.title.lower():
                return e
        return None

    def get_by_source(self, source: Source) -> list[Episode]:
        return [e for e in self._episodes if e.source == source]

    def get_by_character(self, character: str) -> list[Episode]:
        c = character.lower()
        return [e for e in self._episodes if any(c in ch.lower() for ch in e.characters)]

    def get_for_age(self, age_group: AgeGroup) -> list[Episode]:
        return [e for e in self._episodes if e.age_group in (age_group, AgeGroup.ALL)]
