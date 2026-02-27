#!/usr/bin/env python3
"""Main entry point for the Game of Life CLI application."""
import sys
import logging

from player import Player
from dice import Dice
from game import GameManager

logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')


def main() -> None:
    """Run the Game of Life command-line interface."""
    print("\n" + "=" * 70)
    print("🎮 WELCOME TO THE GAME OF LIFE 🎮".center(70))
    print("=" * 70)

    # Get number of players
    while True:
        try:
            num_players = int(input("\n📊 Enter number of players (2-4): "))
            if 2 <= num_players <= 4:
                break
            print("❌ Please enter 2-4 players")
        except ValueError:
            print("❌ Invalid input")

    # Get player names and build Player objects
    players = []
    for i in range(num_players):
        name = input(f"👥 Enter Player {i + 1} name: ").strip()
        if name:
            players.append(Player(name))

    print("\n" + "=" * 70)
    print("🎯 GAME STARTED!".center(70))
    print("=" * 70)

    # Set up GameManager
    manager = GameManager()
    for player in players:
        manager.add_player(player)

    # Show initial player states
    print(f"\n👥 Players ({len(players)}):")
    for i, p in enumerate(players, 1):
        print(f"   {i}. {p.name} - Position: {p.position}, Cash: ${p.finances:,}")

    # Game loop
    max_turns = 10
    for turn in range(max_turns):
        player = manager.get_current_player()

        print(f"\n{'=' * 70}")
        print(f"🎲 {player.name.upper()}'S TURN (Turn {turn + 1}/{max_turns})".center(70))
        print(f"{'=' * 70}")
        print(f"   📍 Position: {player.position}")
        print(f"   💰 Cash: ${player.finances:,}")

        try:
            input("\n   Press ENTER to spin the spinner...")
            spin_value = manager.take_turn()
            print(f"\n   🎲 Spun: {spin_value}")
            print(f"   ➡️  Moved to position: {player.position}")
            print(f"   💰 Cash: ${player.finances:,}")
        except Exception as e:
            print(f"❌ Error: {e}")
            manager.next_turn()

        if manager.game_over:
            break

    # Game Over
    print("\n" + "=" * 70)
    print("🏁 GAME OVER! 🏁".center(70))
    print("=" * 70)

    # Determine winner by score
    winner = manager.determine_winner()
    if winner:
        print(f"\n🏆 WINNER: {winner.name.upper()}".center(70))
        print(f"💰 Final Cash: ${winner.finances:,}".center(70))

    # Final standings
    print(f"\n{'FINAL STANDINGS:'.center(70)}")
    print("-" * 70)
    for rank, p in enumerate(manager.get_rankings(), 1):
        medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else "  "
        print(f"{medal} {p.name:20} - Cash: ${p.finances:>12,}")

    print("\n" + "=" * 70)
    print("✨ Thanks for playing The Game of Life! ✨".center(70))
    print("=" * 70 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 Game cancelled\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Fatal error: {e}\n")
        sys.exit(1)