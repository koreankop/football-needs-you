#!/usr/bin/env python3
"""
Football Needs You! - Terminal Demo
A demo of the penalty shootout game
"""

import random
import time

def print_header():
    """Print game header"""
    print("=" * 60)
    print("⚽" * 30)
    print("=" * 60)
    print("         FOOTBALL NEEDS YOU! - PENALTY SHOOTOUT")
    print("=" * 60)
    print("⚽" * 30)
    print("=" * 60)
    print()

def draw_goal():
    """Draw the goal"""
    print("                    🧤 GOALKEEPER")
    print()
    print("        ╔═══════════════════════════════════╗")
    print("        ║                                   ║")
    print("        ║    LEFT    CENTER      RIGHT      ║")
    print("        ║                                   ║")
    print("        ╚═══════════════════════════════════╝")
    print()
    print("                      ⚽ BALL")
    print()

def play_demo_round(round_num, goals, attempts):
    """Play one demo round"""
    directions = ["LEFT", "CENTER", "RIGHT"]

    print(f"\n{'='*60}")
    print(f"ROUND {round_num}")
    print(f"{'='*60}\n")

    draw_goal()

    # Random choices
    player_choice = random.choice(directions)
    keeper_choice = random.choice(directions)

    print(f"🎯 You shoot to the {player_choice}!")
    time.sleep(0.8)

    print("⚽ Ball is rolling", end='')
    for _ in range(3):
        print(".", end='', flush=True)
        time.sleep(0.4)
    print()

    print(f"🧤 Goalkeeper dives to the {keeper_choice}!")
    time.sleep(0.8)

    attempts += 1
    is_goal = player_choice != keeper_choice

    print("\n" + "=" * 60)
    if is_goal:
        print("🎉🎉🎉 GOOOOOAAAALLLLL!!! ⚽⚽⚽")
        print("=" * 60)
        print("The goalkeeper couldn't stop it! Amazing shot!")
        goals += 1
    else:
        print("🧤🧤🧤 SAVED!!! ❌❌❌")
        print("=" * 60)
        print("The goalkeeper read your mind! What a save!")
    print("=" * 60)

    success_rate = (goals / attempts * 100)
    print(f"\n📊 Current Stats: Goals: {goals} | Attempts: {attempts} | Success: {success_rate:.1f}%\n")

    time.sleep(1.5)
    return goals, attempts

def main():
    """Run the demo game"""
    print_header()

    print("👋 Welcome to the Penalty Shootout Demo!")
    print("\nWatch as the computer plays 5 penalty kicks!\n")
    time.sleep(2)

    goals = 0
    attempts = 0
    num_rounds = 5

    for round_num in range(1, num_rounds + 1):
        goals, attempts = play_demo_round(round_num, goals, attempts)

    # Final stats
    print("\n" + "🏆" * 60)
    print("\n🏆 FINAL STATISTICS 🏆")
    print("=" * 60)
    print(f"   Total Goals Scored: {goals}")
    print(f"   Total Attempts: {attempts}")

    success_rate = (goals / attempts) * 100
    print(f"   Success Rate: {success_rate:.1f}%")
    print()

    if success_rate >= 80:
        print("   🌟 LEGENDARY! Penalty master!")
    elif success_rate >= 60:
        print("   ⭐ EXCELLENT! Great skills!")
    elif success_rate >= 40:
        print("   ✨ GOOD! Solid performance!")
    else:
        print("   💪 KEEP TRYING! Practice makes perfect!")

    print("=" * 60)
    print("\n⚽ Thanks for watching! Open index.html in a browser to play interactively! ⚽\n")

if __name__ == "__main__":
    main()
