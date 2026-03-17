"""Report generation for Katha."""
from __future__ import annotations
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from .models import Episode, Character, Moral


class KathaReport:
    def __init__(self) -> None:
        self.console = Console()

    def display_episode(self, episode: Episode) -> None:
        self.console.print(Panel(
            f"[bold magenta]{episode.title}[/bold magenta]\n"
            f"Source: {episode.source.value} | {episode.kanda_parva}\n"
            f"Age group: {episode.age_group.value}\n\n"
            f"{episode.summary}\n\n"
            f"[bold]Characters:[/bold] {', '.join(episode.characters)}\n"
            f"[bold]Moral:[/bold] {episode.moral}",
            title="Story"))

    def display_episode_list(self, episodes: list[Episode], title: str = "Stories") -> None:
        table = Table(title=title)
        table.add_column("Title", style="bold cyan", width=30)
        table.add_column("Source", style="yellow")
        table.add_column("Characters", width=25)
        table.add_column("Moral", width=40)
        for e in episodes:
            table.add_row(e.title, e.source.value, ", ".join(e.characters[:3]), (e.moral or "")[:50])
        self.console.print(table)

    def display_character(self, character: Character) -> None:
        aliases = ", ".join(character.aliases) if character.aliases else "None"
        rels = "\n".join(f"  {k}: {v}" for k, v in character.relationships.items())
        self.console.print(Panel(
            f"[bold magenta]{character.name}[/bold magenta] ({character.role})\n"
            f"Aliases: {aliases}\n\n{character.description}\n\n"
            f"[bold]Traits:[/bold] {', '.join(character.key_traits)}\n"
            f"[bold]Relationships:[/bold]\n{rels}",
            title="Character"))

    def display_character_list(self, characters: list[Character]) -> None:
        table = Table(title="Mythological Characters")
        table.add_column("Name", style="bold cyan")
        table.add_column("Role", style="yellow")
        table.add_column("Description", width=50)
        for c in characters:
            table.add_row(c.name, c.role, c.description[:60] + "...")
        self.console.print(table)

    def display_moral(self, moral: Moral) -> None:
        self.console.print(Panel(
            f"[bold]{moral.story_title}[/bold]\n\n"
            f"[bold yellow]Lesson:[/bold yellow] {moral.lesson}\n\n"
            f"[bold cyan]Explanation:[/bold cyan] {moral.explanation}\n\n"
            f"[bold green]Life Application:[/bold green] {moral.life_application}",
            title="Life Lesson"))
