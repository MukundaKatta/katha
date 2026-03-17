"""RamayanaStories with 20+ key episodes."""
from __future__ import annotations
from ..models import Episode, Source, AgeGroup


class RamayanaStories:
    """20+ key episodes from the Ramayana."""

    def __init__(self) -> None:
        self._episodes: list[Episode] = self._load_episodes()

    def _load_episodes(self) -> list[Episode]:
        return [
            Episode(title="Birth of Rama", source=Source.RAMAYANA, kanda_parva="Bala Kanda", sequence_order=1,
                    summary="King Dasharatha of Ayodhya performs the Putrakameshti Yajna. From the sacred fire emerges divine payasam. His three queens partake and four divine sons are born: Rama to Kausalya, Bharata to Kaikeyi, and Lakshmana and Shatrughna to Sumitra.",
                    characters=["Rama", "Dasharatha", "Kausalya", "Kaikeyi", "Sumitra"], moral="Divine beings come to earth with a purpose", age_group=AgeGroup.ALL),
            Episode(title="Rama Breaks Shiva's Bow", source=Source.RAMAYANA, kanda_parva="Bala Kanda", sequence_order=2,
                    summary="At the swayamvara of Princess Sita, many kings fail to even lift Lord Shiva's mighty bow Pinaka. Young Rama not only lifts it but breaks it in two, winning Sita's hand in marriage. The heavens rejoice at this divine union.",
                    characters=["Rama", "Sita", "Janaka", "Vishvamitra"], moral="True strength comes from righteousness", age_group=AgeGroup.CHILDREN),
            Episode(title="The Exile of Rama", source=Source.RAMAYANA, kanda_parva="Ayodhya Kanda", sequence_order=3,
                    summary="On the eve of Rama's coronation, Queen Kaikeyi, poisoned by her maid Manthara, demands two boons from Dasharatha: exile Rama for fourteen years and crown Bharata. Bound by his word, the king agrees. Rama accepts exile without complaint.",
                    characters=["Rama", "Kaikeyi", "Dasharatha", "Manthara", "Sita", "Lakshmana"], moral="A person of honor keeps their word, even at great personal cost", age_group=AgeGroup.ALL),
            Episode(title="Sita and Lakshmana Follow Rama", source=Source.RAMAYANA, kanda_parva="Ayodhya Kanda", sequence_order=4,
                    summary="Despite Rama's pleas, Sita refuses to stay behind, arguing that a wife's place is beside her husband. Lakshmana too insists on accompanying his brother. Together, the three enter the Dandaka forest, leaving behind royal comforts.",
                    characters=["Rama", "Sita", "Lakshmana"], moral="True love and loyalty transcend material comforts", age_group=AgeGroup.ALL),
            Episode(title="Bharata's Devotion", source=Source.RAMAYANA, kanda_parva="Ayodhya Kanda", sequence_order=5,
                    summary="Bharata returns to find his father dead and Rama exiled. Horrified by his mother's actions, he marches to the forest to bring Rama back. When Rama refuses, Bharata takes Rama's sandals, places them on the throne, and rules as Rama's regent.",
                    characters=["Bharata", "Rama"], moral="True devotion means putting others before yourself", age_group=AgeGroup.MIDDLE),
            Episode(title="Surpanakha's Humiliation", source=Source.RAMAYANA, kanda_parva="Aranya Kanda", sequence_order=6,
                    summary="The demoness Surpanakha, sister of Ravana, is attracted to Rama. When rejected, she attacks Sita. Lakshmana cuts off her nose and ears. She flies to Lanka and incites Ravana to abduct Sita, setting the stage for the great war.",
                    characters=["Surpanakha", "Rama", "Lakshmana", "Sita"], moral="Actions driven by revenge lead to greater destruction", age_group=AgeGroup.TEEN),
            Episode(title="The Golden Deer (Maricha)", source=Source.RAMAYANA, kanda_parva="Aranya Kanda", sequence_order=7,
                    summary="Ravana sends the demon Maricha in the form of a golden deer to lure Rama away from the hermitage. Sita insists Rama chase it. Maricha, dying, mimics Rama's voice calling for help, tricking Lakshmana into leaving Sita alone.",
                    characters=["Maricha", "Sita", "Rama", "Lakshmana", "Ravana"], moral="Desire for material beauty can lead to deception", age_group=AgeGroup.CHILDREN),
            Episode(title="The Abduction of Sita", source=Source.RAMAYANA, kanda_parva="Aranya Kanda", sequence_order=8,
                    summary="Ravana, disguised as a mendicant, approaches the unprotected Sita. When she crosses the protective line drawn by Lakshmana, Ravana reveals his true form and abducts her in his flying chariot Pushpaka. The vulture Jatayu fights valiantly but falls.",
                    characters=["Sita", "Ravana", "Jatayu", "Lakshmana"], moral="Courage knows no bounds when defending the righteous", age_group=AgeGroup.ALL),
            Episode(title="Jatayu's Sacrifice", source=Source.RAMAYANA, kanda_parva="Aranya Kanda", sequence_order=9,
                    summary="The aged vulture king Jatayu fights Ravana to save Sita. Though mortally wounded, he survives long enough to tell Rama that Ravana took Sita southward. Rama performs Jatayu's last rites as he would for his own father.",
                    characters=["Jatayu", "Rama", "Ravana", "Sita"], moral="Even in death, a noble soul serves others", age_group=AgeGroup.CHILDREN),
            Episode(title="Rama Meets Hanuman", source=Source.RAMAYANA, kanda_parva="Kishkindha Kanda", sequence_order=10,
                    summary="In his search for Sita, Rama encounters Hanuman near Rishyamukha mountain. Hanuman, servant of the exiled monkey king Sugriva, brokers an alliance. In exchange for helping find Sita, Rama agrees to help Sugriva reclaim his kingdom from Vali.",
                    characters=["Rama", "Hanuman", "Sugriva", "Lakshmana"], moral="Alliances built on mutual trust lead to great achievements", age_group=AgeGroup.MIDDLE),
            Episode(title="The Killing of Vali", source=Source.RAMAYANA, kanda_parva="Kishkindha Kanda", sequence_order=11,
                    summary="Sugriva challenges his brother Vali to a duel. Rama, hidden behind a tree, shoots Vali with an arrow. The dying Vali questions the morality of this act. Rama explains dharma and crowns Sugriva king of Kishkindha.",
                    characters=["Rama", "Vali", "Sugriva"], moral="Dharma is complex and sometimes requires difficult choices", age_group=AgeGroup.ADULT),
            Episode(title="Hanuman's Leap to Lanka", source=Source.RAMAYANA, kanda_parva="Sundara Kanda", sequence_order=12,
                    summary="Hanuman, son of Vayu, leaps across the vast ocean to Lanka. He overcomes obstacles: the mountain Mainaka offers rest, the serpent Surasa tests him, and the demoness Simhika tries to swallow his shadow. He reaches Lanka through sheer devotion and power.",
                    characters=["Hanuman", "Surasa", "Mainaka", "Simhika"], moral="Faith and devotion can overcome any obstacle", age_group=AgeGroup.CHILDREN),
            Episode(title="Hanuman Finds Sita", source=Source.RAMAYANA, kanda_parva="Sundara Kanda", sequence_order=13,
                    summary="In Lanka, Hanuman searches everywhere and finally finds Sita in the Ashoka grove, guarded by demonesses. He shows her Rama's ring as proof of his identity. Sita gives him her hair ornament (chudamani) to take back to Rama.",
                    characters=["Hanuman", "Sita"], moral="Hope sustains us through the darkest times", age_group=AgeGroup.CHILDREN),
            Episode(title="Hanuman Burns Lanka", source=Source.RAMAYANA, kanda_parva="Sundara Kanda", sequence_order=14,
                    summary="Captured by Indrajit, Hanuman is brought before Ravana. They set his tail on fire as punishment. But Hanuman grows his tail endlessly, then leaps across Lanka, setting the golden city ablaze with his burning tail before returning to Rama.",
                    characters=["Hanuman", "Ravana", "Indrajit"], moral="True devotees cannot be defeated by any force", age_group=AgeGroup.CHILDREN),
            Episode(title="Building the Bridge (Rama Setu)", source=Source.RAMAYANA, kanda_parva="Yuddha Kanda", sequence_order=15,
                    summary="To cross the ocean to Lanka, Rama's army of vanaras builds a bridge of floating stones. Each stone, inscribed with Rama's name, floats on the water. Nala and Nila engineer this miraculous bridge in five days.",
                    characters=["Rama", "Nala", "Nila", "Hanuman", "Sugriva"], moral="With unity and faith, even the impossible becomes possible", age_group=AgeGroup.CHILDREN),
            Episode(title="Vibhishana Joins Rama", source=Source.RAMAYANA, kanda_parva="Yuddha Kanda", sequence_order=16,
                    summary="Ravana's righteous brother Vibhishana repeatedly advises returning Sita, but is banished. He crosses over to Rama's side. Despite suspicion from others, Rama accepts him, saying anyone who seeks refuge deserves protection.",
                    characters=["Vibhishana", "Rama", "Ravana"], moral="Righteousness may mean standing alone against your own", age_group=AgeGroup.MIDDLE),
            Episode(title="The Death of Kumbhakarna", source=Source.RAMAYANA, kanda_parva="Yuddha Kanda", sequence_order=17,
                    summary="The giant Kumbhakarna, Ravana's brother, is awakened from his cosmic sleep. Despite knowing Ravana is wrong, he fights for his brother out of loyalty. Rama kills him in a fierce battle after severing his limbs one by one.",
                    characters=["Kumbhakarna", "Rama", "Ravana"], moral="Loyalty to wrong causes, even from love, leads to destruction", age_group=AgeGroup.TEEN),
            Episode(title="Lakshmana and the Sanjeevani", source=Source.RAMAYANA, kanda_parva="Yuddha Kanda", sequence_order=18,
                    summary="Indrajit's Shakti weapon strikes Lakshmana, who lies dying. Only the Sanjeevani herb from the Himalayas can save him before sunrise. Hanuman flies north but cannot identify the herb, so he lifts the entire mountain and carries it back.",
                    characters=["Lakshmana", "Hanuman", "Indrajit"], moral="No task is too great when done out of love", age_group=AgeGroup.CHILDREN),
            Episode(title="The Killing of Ravana", source=Source.RAMAYANA, kanda_parva="Yuddha Kanda", sequence_order=19,
                    summary="After a titanic battle lasting days, Rama uses the Brahmastra, guided by Agastya's counsel, to strike Ravana's navel where his life force is stored. The ten-headed king falls. Even in death, Rama honors him as a great scholar and warrior.",
                    characters=["Rama", "Ravana", "Agastya"], moral="Evil, however powerful, is ultimately defeated by righteousness", age_group=AgeGroup.ALL),
            Episode(title="Sita's Agni Pariksha", source=Source.RAMAYANA, kanda_parva="Yuddha Kanda", sequence_order=20,
                    summary="After rescue, Rama asks Sita to prove her purity by entering fire. Sita enters the flames without hesitation. Agni, the fire god, presents her unharmed, testifying to her absolute purity and chastity.",
                    characters=["Sita", "Rama", "Agni"], moral="Truth and virtue always stand vindicated", age_group=AgeGroup.ADULT),
            Episode(title="Return to Ayodhya", source=Source.RAMAYANA, kanda_parva="Yuddha Kanda", sequence_order=21,
                    summary="Rama, Sita, and Lakshmana fly back to Ayodhya in the Pushpaka Vimana. The citizens light thousands of lamps to welcome them. Rama is crowned king, beginning the golden era of Rama Rajya. This homecoming is celebrated as Diwali.",
                    characters=["Rama", "Sita", "Lakshmana", "Bharata", "Hanuman"], moral="Righteousness prevails and is celebrated by all", age_group=AgeGroup.CHILDREN),
            Episode(title="Luv and Kush", source=Source.RAMAYANA, kanda_parva="Uttara Kanda", sequence_order=22,
                    summary="In the forest hermitage of Valmiki, Sita gives birth to twin sons Luv and Kush. The twins learn the Ramayana from Valmiki himself and later sing it in Rama's court, reuniting the family.",
                    characters=["Sita", "Luv", "Kush", "Valmiki", "Rama"], moral="Truth and art preserve dharma across generations", age_group=AgeGroup.MIDDLE),
        ]

    def get_all_episodes(self) -> list[Episode]:
        return sorted(self._episodes, key=lambda e: e.sequence_order)

    def get_episode(self, title: str) -> Episode | None:
        for e in self._episodes:
            if title.lower() in e.title.lower():
                return e
        return None

    def get_by_kanda(self, kanda: str) -> list[Episode]:
        return [e for e in self._episodes if kanda.lower() in e.kanda_parva.lower()]

    def get_by_character(self, character: str) -> list[Episode]:
        c = character.lower()
        return [e for e in self._episodes if any(c in ch.lower() for ch in e.characters)]

    def get_for_age(self, age_group: AgeGroup) -> list[Episode]:
        return [e for e in self._episodes if e.age_group in (age_group, AgeGroup.ALL)]
