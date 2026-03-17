"""MahabharataStories with 20+ key episodes."""
from __future__ import annotations
from ..models import Episode, Source, AgeGroup


class MahabharataStories:
    """20+ key episodes from the Mahabharata."""

    def __init__(self) -> None:
        self._episodes: list[Episode] = self._load_episodes()

    def _load_episodes(self) -> list[Episode]:
        return [
            Episode(title="The Birth of the Pandavas and Kauravas", source=Source.MAHABHARATA, kanda_parva="Adi Parva", sequence_order=1,
                    summary="Pandu's two wives, Kunti and Madri, invoke divine mantras. Kunti bears Yudhishthira (Dharma), Bhima (Vayu), and Arjuna (Indra). Madri bears twins Nakula and Sahadeva (Ashvini Kumaras). Meanwhile, Gandhari gives birth to 100 sons, the Kauravas, led by Duryodhana.",
                    characters=["Kunti", "Pandu", "Yudhishthira", "Bhima", "Arjuna", "Duryodhana"], moral="Divine birth carries divine responsibility", age_group=AgeGroup.ALL),
            Episode(title="Drona's Test - The Eye of the Bird", source=Source.MAHABHARATA, kanda_parva="Adi Parva", sequence_order=2,
                    summary="Guru Dronacharya tests his students' concentration by asking them to aim at a wooden bird on a tree. When asked what they see, only Arjuna answers 'Only the eye of the bird.' He alone hits the target perfectly.",
                    characters=["Arjuna", "Drona"], moral="Success requires single-pointed focus and concentration", age_group=AgeGroup.CHILDREN),
            Episode(title="Ekalavya's Sacrifice", source=Source.MAHABHARATA, kanda_parva="Adi Parva", sequence_order=3,
                    summary="The tribal boy Ekalavya, denied training by Drona, makes a clay statue of the guru and teaches himself to become a superior archer. When Drona discovers this, he demands Ekalavya's right thumb as guru dakshina, which the devoted student gives without hesitation.",
                    characters=["Ekalavya", "Drona", "Arjuna"], moral="Devotion to a teacher transcends all barriers, but the system may not be just", age_group=AgeGroup.MIDDLE),
            Episode(title="The House of Lac (Lakshagriha)", source=Source.MAHABHARATA, kanda_parva="Adi Parva", sequence_order=4,
                    summary="Duryodhana plots to kill the Pandavas by housing them in a palace made of lac and setting it ablaze. Warned by Vidura, the Pandavas escape through a secret tunnel, but the world believes them dead.",
                    characters=["Duryodhana", "Vidura", "Pandavas"], moral="Evil plots are ultimately defeated by wisdom and foresight", age_group=AgeGroup.MIDDLE),
            Episode(title="Draupadi's Swayamvara", source=Source.MAHABHARATA, kanda_parva="Adi Parva", sequence_order=5,
                    summary="At Draupadi's swayamvara, the challenge is to string a massive bow and hit a rotating fish's eye by looking only at its reflection. Arjuna, disguised as a Brahmin, succeeds. By Kunti's inadvertent command, Draupadi becomes wife to all five Pandavas.",
                    characters=["Draupadi", "Arjuna", "Kunti", "Pandavas"], moral="Skill and destiny work together", age_group=AgeGroup.TEEN),
            Episode(title="The Game of Dice", source=Source.MAHABHARATA, kanda_parva="Sabha Parva", sequence_order=6,
                    summary="Shakuni, Duryodhana's uncle, challenges Yudhishthira to a rigged game of dice. Yudhishthira gambles away his kingdom, his brothers, himself, and finally Draupadi. In the court, Dushasana drags Draupadi by her hair and attempts to disrobe her.",
                    characters=["Yudhishthira", "Shakuni", "Duryodhana", "Draupadi", "Dushasana"], moral="Gambling and attachment to honor can lead to catastrophic consequences", age_group=AgeGroup.TEEN),
            Episode(title="Draupadi's Vastraharan and Krishna's Grace", source=Source.MAHABHARATA, kanda_parva="Sabha Parva", sequence_order=7,
                    summary="As Dushasana tries to disrobe Draupadi in the royal court, she prays to Krishna. Miraculously, her sari becomes endless - no matter how much Dushasana pulls, more fabric appears. The elders sit in shameful silence. Draupadi vows her hair will remain unbound until washed with Dushasana's blood.",
                    characters=["Draupadi", "Krishna", "Dushasana", "Bhishma"], moral="God protects those who surrender completely; silence in the face of injustice is complicity", age_group=AgeGroup.TEEN),
            Episode(title="The Thirteen Years of Exile", source=Source.MAHABHARATA, kanda_parva="Vana Parva", sequence_order=8,
                    summary="The Pandavas spend twelve years in the forest and one year in disguise. During exile, they gain divine weapons, meet sages, and grow stronger. Arjuna performs penance and obtains the Pashupatastra from Lord Shiva.",
                    characters=["Pandavas", "Arjuna", "Shiva"], moral="Adversity builds strength and character for the challenges ahead", age_group=AgeGroup.MIDDLE),
            Episode(title="Arjuna and the Kirata (Shiva)", source=Source.MAHABHARATA, kanda_parva="Vana Parva", sequence_order=9,
                    summary="Arjuna performs intense penance in the Himalayas. Shiva appears disguised as a Kirata (hunter) and fights Arjuna over a wild boar they both claim to have killed. When Arjuna realizes the hunter is Shiva, he is granted the Pashupatastra.",
                    characters=["Arjuna", "Shiva"], moral="God tests devotees before granting them divine gifts", age_group=AgeGroup.MIDDLE),
            Episode(title="The Year in Disguise (Virata Parva)", source=Source.MAHABHARATA, kanda_parva="Virata Parva", sequence_order=10,
                    summary="The Pandavas spend their thirteenth year in disguise at King Virata's court. Yudhishthira becomes a dice-playing companion, Bhima a cook, Arjuna a dance teacher (Brihannala), Draupadi a maid, and the twins work in stables.",
                    characters=["Pandavas", "Draupadi", "Virata"], moral="True nobility cannot be hidden even in humble disguise", age_group=AgeGroup.MIDDLE),
            Episode(title="Krishna's Peace Mission", source=Source.MAHABHARATA, kanda_parva="Udyoga Parva", sequence_order=11,
                    summary="Before the war, Krishna goes to Hastinapura as a peace envoy. He asks for just five villages for the five Pandavas. Duryodhana refuses even a needlepoint of land. Krishna reveals his cosmic form, but Duryodhana is unmoved. War becomes inevitable.",
                    characters=["Krishna", "Duryodhana", "Pandavas"], moral="Pride and greed make people deaf to reason and wisdom", age_group=AgeGroup.TEEN),
            Episode(title="The Bhagavad Gita", source=Source.MAHABHARATA, kanda_parva="Bhishma Parva", sequence_order=12,
                    summary="On the battlefield, Arjuna sees his teachers, relatives, and friends on both sides and refuses to fight. Krishna delivers the Bhagavad Gita - 700 verses of divine wisdom covering duty, knowledge, devotion, and the nature of reality. Arjuna is transformed and takes up his bow.",
                    characters=["Krishna", "Arjuna"], moral="Fulfill your duty without attachment; the soul is eternal", age_group=AgeGroup.ALL),
            Episode(title="The Fall of Bhishma", source=Source.MAHABHARATA, kanda_parva="Bhishma Parva", sequence_order=13,
                    summary="The invincible Bhishma, who had the boon of choosing his time of death, fights for the Kauravas. On the tenth day, Shikhandi (born as Amba reborn) stands before him. Bhishma lowers his weapons, and Arjuna pierces him with arrows. Bhishma lies on a bed of arrows.",
                    characters=["Bhishma", "Arjuna", "Shikhandi", "Krishna"], moral="Even the mightiest must fall when destiny calls", age_group=AgeGroup.TEEN),
            Episode(title="The Death of Abhimanyu", source=Source.MAHABHARATA, kanda_parva="Drona Parva", sequence_order=14,
                    summary="Arjuna's sixteen-year-old son Abhimanyu enters the Chakravyuha formation knowing only how to penetrate it, not how to exit. Trapped inside, he fights seven warriors alone with extraordinary valor before being killed in an unfair combat.",
                    characters=["Abhimanyu", "Drona", "Jayadratha", "Arjuna"], moral="True heroism shines even in hopeless circumstances; breaking rules of war has consequences", age_group=AgeGroup.TEEN),
            Episode(title="Arjuna's Vow and Jayadratha's Death", source=Source.MAHABHARATA, kanda_parva="Drona Parva", sequence_order=15,
                    summary="Grief-stricken by Abhimanyu's death, Arjuna vows to kill Jayadratha before sunset or immolate himself. Krishna creates an artificial eclipse, and when Jayadratha emerges thinking Arjuna has failed, Arjuna decapitates him as the sun reappears.",
                    characters=["Arjuna", "Krishna", "Jayadratha"], moral="Divine intervention supports righteous resolve", age_group=AgeGroup.TEEN),
            Episode(title="Karna Reveals His Identity", source=Source.MAHABHARATA, kanda_parva="Shanti Parva (flashback)", sequence_order=16,
                    summary="Before the war, Kunti reveals to Karna that he is her firstborn, making him the eldest Pandava. Krishna also approaches him. Despite knowing this, Karna refuses to switch sides, bound by his loyalty to Duryodhana who honored him when all others rejected him.",
                    characters=["Karna", "Kunti", "Krishna"], moral="Loyalty and gratitude can be stronger than blood bonds", age_group=AgeGroup.ADULT),
            Episode(title="The Death of Karna", source=Source.MAHABHARATA, kanda_parva="Karna Parva", sequence_order=17,
                    summary="In the climactic duel with Arjuna, Karna's chariot wheel sinks into the earth. As he struggles to free it, remembering all the curses upon him, Krishna urges Arjuna to strike. Arjuna reluctantly kills the unarmed Karna with the Anjalika arrow.",
                    characters=["Karna", "Arjuna", "Krishna"], moral="The consequences of past actions (karma) eventually catch up with everyone", age_group=AgeGroup.ADULT),
            Episode(title="Duryodhana's Last Stand", source=Source.MAHABHARATA, kanda_parva="Shalya Parva", sequence_order=18,
                    summary="With all his brothers and allies slain, Duryodhana hides in a lake. The Pandavas find him and Bhima challenges him to a mace fight. Bhima strikes Duryodhana's thigh (against the rules), fulfilling Draupadi's vow. The dying Duryodhana accuses them of cheating.",
                    characters=["Duryodhana", "Bhima", "Krishna"], moral="Pride leads to downfall, but even villains have valid grievances", age_group=AgeGroup.ADULT),
            Episode(title="Ashwatthama's Revenge", source=Source.MAHABHARATA, kanda_parva="Sauptika Parva", sequence_order=19,
                    summary="Drona's son Ashwatthama, enraged by his father's death, attacks the Pandava camp at night and kills Draupadi's five sons while they sleep. He also launches the Brahmashirastra. Cursed by Krishna, he is condemned to wander the earth eternally.",
                    characters=["Ashwatthama", "Draupadi", "Krishna"], moral="Revenge born from grief breeds only more suffering", age_group=AgeGroup.ADULT),
            Episode(title="Bhishma's Teachings on the Bed of Arrows", source=Source.MAHABHARATA, kanda_parva="Shanti Parva", sequence_order=20,
                    summary="Lying on his bed of arrows, awaiting the auspicious moment to die, Bhishma teaches Yudhishthira about dharma, governance, duty, and philosophy. His teachings form the Shanti Parva and Anushasana Parva - two of the longest books.",
                    characters=["Bhishma", "Yudhishthira", "Krishna"], moral="Wisdom should be shared, especially at life's end", age_group=AgeGroup.ADULT),
            Episode(title="Yudhishthira's Dharma Test - The Dog at Heaven's Gate", source=Source.MAHABHARATA, kanda_parva="Svargarohana Parva", sequence_order=21,
                    summary="On the final journey to heaven, all Pandavas and Draupadi fall except Yudhishthira. A dog follows him to heaven's gate. Indra says the dog cannot enter. Yudhishthira refuses to abandon his faithful companion. The dog reveals itself as Dharma, his father.",
                    characters=["Yudhishthira", "Dharma", "Indra"], moral="Compassion for all beings is the highest dharma", age_group=AgeGroup.CHILDREN),
            Episode(title="The Story of Savitri and Satyavan", source=Source.MAHABHARATA, kanda_parva="Vana Parva (sub-story)", sequence_order=22,
                    summary="Princess Savitri chooses Satyavan as her husband despite knowing he will die within a year. When Yama comes for his soul, Savitri follows and debates with the god of death, winning boon after boon through her wisdom until Yama restores Satyavan's life.",
                    characters=["Savitri", "Satyavan", "Yama"], moral="Devoted love and intelligent courage can overcome even death", age_group=AgeGroup.CHILDREN),
            Episode(title="Nala and Damayanti", source=Source.MAHABHARATA, kanda_parva="Vana Parva (sub-story)", sequence_order=23,
                    summary="King Nala and Princess Damayanti fall in love through a swan messenger. After marriage, Nala loses everything to dice (paralleling Yudhishthira). Separated and transformed, they eventually reunite through Damayanti's unwavering love and Nala's reformed character.",
                    characters=["Nala", "Damayanti"], moral="True love endures all trials; gambling destroys kingdoms", age_group=AgeGroup.MIDDLE),
        ]

    def get_all_episodes(self) -> list[Episode]:
        return sorted(self._episodes, key=lambda e: e.sequence_order)

    def get_episode(self, title: str) -> Episode | None:
        for e in self._episodes:
            if title.lower() in e.title.lower():
                return e
        return None

    def get_by_parva(self, parva: str) -> list[Episode]:
        return [e for e in self._episodes if parva.lower() in e.kanda_parva.lower()]

    def get_by_character(self, character: str) -> list[Episode]:
        c = character.lower()
        return [e for e in self._episodes if any(c in ch.lower() for ch in e.characters)]

    def get_for_age(self, age_group: AgeGroup) -> list[Episode]:
        return [e for e in self._episodes if e.age_group in (age_group, AgeGroup.ALL)]
