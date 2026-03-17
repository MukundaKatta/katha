"""CLI for Katha."""
from __future__ import annotations
import click
from rich.console import Console
from .stories.ramayana import RamayanaStories
from .stories.mahabharata import MahabharataStories
from .stories.puranas import PuranaStories
from .generator.characters import CharacterDatabase
from .generator.narrator import StoryNarrator
from .generator.morals import MoralExtractor
from .report import KathaReport
from .models import AgeGroup

console = Console()


@click.group()
def cli() -> None:
    """Katha - AI Indian Mythology Stories."""
    pass


@cli.command()
@click.argument("source", type=click.Choice(["ramayana", "mahabharata", "puranas"]))
@click.option("--age", "-a", type=click.Choice(["children", "middle", "teen", "adult", "all"]), default="all")
def stories(source: str, age: str) -> None:
    """List stories from a source."""
    report = KathaReport()
    age_group = AgeGroup(age)
    if source == "ramayana":
        eps = RamayanaStories().get_for_age(age_group)
    elif source == "mahabharata":
        eps = MahabharataStories().get_for_age(age_group)
    else:
        eps = PuranaStories().get_for_age(age_group)
    report.display_episode_list(eps, f"{source.title()} Stories")


@cli.command()
@click.argument("title")
@click.option("--age", "-a", type=click.Choice(["children", "middle", "teen", "adult", "all"]), default="all")
def tell(title: str, age: str) -> None:
    """Tell a specific story."""
    narrator = StoryNarrator()
    age_group = AgeGroup(age)
    for db in [RamayanaStories(), MahabharataStories(), PuranaStories()]:
        ep = db.get_episode(title)
        if ep:
            narration = narrator.narrate(ep, age_group)
            console.print(f"\n{narration}")
            return
    console.print(f"[red]Story not found: {title}[/red]")


@cli.command()
@click.argument("name")
def character(name: str) -> None:
    """Show character details."""
    db = CharacterDatabase()
    report = KathaReport()
    c = db.get_character(name)
    if c:
        report.display_character(c)
    else:
        results = db.search_characters(name)
        if results:
            report.display_character(results[0])
        else:
            console.print(f"[red]Character not found: {name}[/red]")


@cli.command()
@click.option("--role", "-r", default=None, help="Filter by role")
def characters(role: str | None) -> None:
    """List all characters."""
    db = CharacterDatabase()
    report = KathaReport()
    if role:
        chars = db.get_by_role(role)
    else:
        chars = db.get_all_characters()
    report.display_character_list(chars)


@cli.command()
@click.argument("title")
def moral(title: str) -> None:
    """Extract the moral from a story."""
    extractor = MoralExtractor()
    report = KathaReport()
    for db in [RamayanaStories(), MahabharataStories(), PuranaStories()]:
        ep = db.get_episode(title)
        if ep:
            m = extractor.extract_moral(ep)
            report.display_moral(m)
            return
    console.print(f"[red]Story not found: {title}[/red]")


if __name__ == "__main__":
    cli()
