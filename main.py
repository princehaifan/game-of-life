#!/usr/bin/env python3
# Game of Life - Main Entry Point

import sys

from player import Player
from dice import Dice


def main():

    print("\n" + "="*70)
    print("🎮 WELCOME TO THE GAME OF LIFE 🎮".center(70))
    print("="*70)

    # Get players
    while True:
        try:
            num_players = int(input("\n📊 Enter number of players (2-4): "))
            if 2 <= num_players <= 4:
                break
            print("❌ Please enter 2-4 players")
        except ValueError:
            print("❌ Invalid input")

    # Get player names
    players = []
    for i in range(num_players):
        name = input(f"👥 Enter Player {i+1} name: ").strip()
        if name:
            players.append(Player(name))

    print("\n" + "="*70)
    print("🎯 GAME STARTED!".center(70))
    print("="*70)

    # Show players
    print(f"\n👥 Players ({len(players)}):")
    for i, p in enumerate(players, 1):
        print(f"   {i}. {p.name} - Position: {p.position}, Cash: ${p.finances:,}")

    # Initialize game
    dice = Dice()
    current_player = 0
    max_turns = 10

    # Game loop
    for turn in range(max_turns):
        player = players[current_player]

        print(f"\n{'='*70}")
        print(f"🎲 {player.name.upper()}'S TURN (Turn {turn+1}/{max_turns})".center(70))
        print(f"{'='*70}")
        print(f"   📍 Position: {player.position}")
        print(f"   💰 Cash: ${player.finances:,}")

        try:
            input("\n   Press ENTER to spin the spinner...")
            spin_value = dice.spin()
            player.move(spin_value)
            print(f"\n   🎲 Spun: {spin_value}")
            print(f"   ➡️  Moved to position: {player.position}")
            print(f"   💰 Cash: ${player.finances:,}")
        except Exception as e:
            print(f"❌ Error: {e}")

        current_player = (current_player + 1) % len(players)

    # Game Over
    print("\n" + "="*70)
    print("🏁 GAME OVER! 🏁".center(70))
    print("="*70)

    # Determine winner
    winner = max(players, key=lambda p: p.finances)
    print(f"\n🏆 WINNER: {winner.name.upper()}".center(70))
    print(f"💰 Final Cash: ${winner.finances:,}".center(70))

    # Final standings
    print(f"\n{'FINAL STANDINGS:'.center(70)}")
    print("-" * 70)
    sorted_players = sorted(players, key=lambda p: p.finances, reverse=True)
    for rank, p in enumerate(sorted_players, 1):
        medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else "  "
        print(f"{medal} {p.name:20} - Cash: ${p.finances:>12,}")

    print("\n" + "="*70)
    print("✨ Thanks for playing The Game of Life! ✨".center(70))
    print("="*70 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 Game cancelled\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Fatal error: {e}\n")
        sys.exit(1)