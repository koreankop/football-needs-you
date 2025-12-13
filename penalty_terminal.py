#!/usr/bin/env python3
"""
Football Needs You! - Terminal Edition
A fun penalty shootout game for the command line
"""

import random
import time
import sys

class PenaltyGame:
    def __init__(self):
        self.goals = 0
        self.attempts = 0

    def clear_screen(self):
        """Clear the terminal screen"""
        print("\033[2J\033[H", end='')

    def print_header(self):
        """Print game header"""
        print("=" * 60)
        print("⚽" * 30)
        print("=" * 60)
        print("         FOOTBALL NEEDS YOU! - PENALTY SHOOTOUT")
        print("=" * 60)
        print("⚽" * 30)
        print("=" * 60)
        print()

    def print_scoreboard(self):
        """Display current score"""
        success_rate = (self.goals / self.attempts * 100) if self.attempts > 0 else 0
        print(f"\n📊 SCOREBOARD:")
        print(f"   Goals: {self.goals} | Attempts: {self.attempts} | Success Rate: {success_rate:.1f}%")
        print()

    def draw_goal(self):
        """Draw the goal"""
        print("                    🧤 GOALKEEPER")
        print()
        print("        ╔═══════════════════════════════════╗")
        print("        ║                                   ║")
        print("        ║  [1] LEFT  [2] CENTER  [3] RIGHT  ║")
        print("        ║                                   ║")
        print("        ╚═══════════════════════════════════╝")
        print()
        print("                      ⚽ BALL")
        print()

    def animate_shot(self, player_choice, keeper_choice):
        """Animate the penalty shot"""
        directions = {1: "LEFT", 2: "CENTER", 3: "RIGHT"}

        print(f"\n🎯 You shoot to the {directions[player_choice]}!")
        time.sleep(0.5)

        print("⚽ Ball is rolling...")
        for _ in range(3):
            print(".", end='', flush=True)
            time.sleep(0.3)
        print()

        print(f"🧤 Goalkeeper dives to the {directions[keeper_choice]}!")
        time.sleep(0.5)

        return player_choice != keeper_choice

    def display_result(self, is_goal):
        """Display the result of the shot"""
        print("\n" + "=" * 60)
        if is_goal:
            print("🎉🎉🎉 GOOOOOAAAALLLLL!!! ⚽⚽⚽")
            print("=" * 60)
            print("The goalkeeper couldn't stop it! Amazing shot!")
        else:
            print("🧤🧤🧤 SAVED!!! ❌❌❌")
            print("=" * 60)
            print("The goalkeeper read your mind! What a save!")
        print("=" * 60)
        time.sleep(1.5)

    def play_round(self):
        """Play one round of penalty shootout"""
        self.draw_goal()

        # Get player choice
        while True:
            try:
                choice = input("Where do you want to shoot? (1=Left, 2=Center, 3=Right, Q=Quit): ").strip().upper()

                if choice == 'Q':
                    return False

                player_choice = int(choice)
                if player_choice in [1, 2, 3]:
                    break
                else:
                    print("❌ Invalid choice! Please enter 1, 2, or 3.")
            except ValueError:
                print("❌ Invalid input! Please enter 1, 2, or 3.")

        # Goalkeeper randomly chooses
        keeper_choice = random.randint(1, 3)

        # Increment attempts
        self.attempts += 1

        # Animate and determine result
        is_goal = self.animate_shot(player_choice, keeper_choice)

        if is_goal:
            self.goals += 1

        self.display_result(is_goal)

        return True

    def show_final_stats(self):
        """Show final game statistics"""
        self.clear_screen()
        self.print_header()

        print("\n🏆 FINAL STATISTICS 🏆")
        print("=" * 60)
        print(f"   Total Goals Scored: {self.goals}")
        print(f"   Total Attempts: {self.attempts}")

        if self.attempts > 0:
            success_rate = (self.goals / self.attempts) * 100
            print(f"   Success Rate: {success_rate:.1f}%")
            print()

            if success_rate >= 80:
                print("   🌟 LEGENDARY! You're a penalty master!")
            elif success_rate >= 60:
                print("   ⭐ EXCELLENT! Great shooting skills!")
            elif success_rate >= 40:
                print("   ✨ GOOD! Keep practicing!")
            else:
                print("   💪 KEEP TRYING! Practice makes perfect!")

        print("=" * 60)
        print("\nThanks for playing Football Needs You! ⚽")
        print()

    def run(self):
        """Main game loop"""
        self.clear_screen()
        self.print_header()

        print("\n👋 Welcome to the Penalty Shootout Terminal Game!")
        print("\n📋 HOW TO PLAY:")
        print("   • Choose where to shoot: 1 (Left), 2 (Center), or 3 (Right)")
        print("   • The goalkeeper will randomly dive to one direction")
        print("   • Score as many goals as you can!")
        print("   • Type 'Q' anytime to quit and see your stats")
        print()
        input("Press ENTER to start playing... ")

        # Main game loop
        while True:
            self.clear_screen()
            self.print_header()
            self.print_scoreboard()

            if not self.play_round():
                break

            print("\n" + "-" * 60)
            input("Press ENTER for next penalty... ")

        # Show final statistics
        self.show_final_stats()

if __name__ == "__main__":
    try:
        game = PenaltyGame()
        game.run()
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted! Thanks for playing! ⚽")
        sys.exit(0)
