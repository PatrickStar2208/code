"""
Menu display module for Hospital Patient Management System
Handles all UI and menu-related functionality
"""

import os


class Color:
    """ANSI color codes for terminal output"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def clear_screen():
    """Clear terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')


def print_header(text):
    """Print a formatted header"""
    print(f"\n{Color.BOLD}{Color.CYAN}{'='*60}{Color.END}")
    print(f"{Color.BOLD}{Color.CYAN}  {text:^54}  {Color.END}")
    print(f"{Color.BOLD}{Color.CYAN}{'='*60}{Color.END}\n")


def print_section(text):
    """Print a formatted section title"""
    print(f"\n{Color.BOLD}{Color.BLUE}{'─'*60}{Color.END}")
    print(f"{Color.BOLD}{Color.BLUE}  {text}{Color.END}")
    print(f"{Color.BOLD}{Color.BLUE}{'─'*60}{Color.END}\n")


def print_success(text):
    """Print success message"""
    print(f"\n{Color.GREEN}{Color.BOLD}✓ {text}{Color.END}\n")


def print_error(text):
    """Print error message"""
    print(f"\n{Color.RED}{Color.BOLD}✗ {text}{Color.END}\n")


def print_info(text):
    """Print info message"""
    print(f"\n{Color.CYAN}ℹ {text}{Color.END}\n")


def display_menu():
    """Display the main menu with nice formatting"""
    print_header("🏥 HOSPITAL PATIENT MANAGEMENT SYSTEM 🏥")
    
    print(f"{Color.BOLD}{Color.YELLOW}📋 MAIN MENU:{Color.END}\n")
    
    menu_items = [
        ("1", "📝 Register Patient"),
        ("2", "🔎 Find Patient"),
        ("3", "✏️  Update Patient"),
        ("4", "📤 Discharge Patient"),
        ("5", "📊 Display All Patients"),
        ("6", "➕ Add Medical History"),
        ("7", "🗑️  Delete Medical Record"),
        ("8", "📖 Display Medical History"),
        ("9", "🔍 Find Patient History"),
        ("10", "🛠️ Update Medical History"),
        ("11", "🚑 Process Next Patient"),
        ("12", "💾 Save Patients to File"),
        ("13", "💾 Save Medical History to File"),
        ("0", "🚪 Exit"),
    ]
    
    for num, title in menu_items:
        if num == "0":
            print(f"\n  {Color.RED}{Color.BOLD}[{num}] {title}{Color.END}")
        else:
            print(f"  {Color.CYAN}{Color.BOLD}[{num}] {Color.END}{title}")
    
    print(f"\n{Color.BOLD}{Color.CYAN}{'─'*60}{Color.END}\n")


def input_int(prompt, default=None):
    """Get integer input with formatting"""
    try:
        user_input = input(f"  {Color.BOLD}{Color.YELLOW}→{Color.END} {prompt}").strip()
        return int(user_input) if user_input else default
    except ValueError:
        print_error("Please enter a valid integer!")
        return default
    except EOFError:
        print_error("Input ended unexpectedly. Returning to menu.")
        return -1  # Return invalid choice to trigger error handling


def input_age(prompt="Age: "):
    """Get a positive integer age from user. Returns None if blank or invalid."""
    try:
        user_input = input(f"  {Color.BOLD}{Color.YELLOW}→{Color.END} {prompt}").strip()
        if not user_input:
            return None
        age = int(user_input)
        if age < 0:
            print_error("Age cannot be negative!")
            return None
        if age > 150:
            print_error("Age seems unrealistic (max 150)!")
            return None
        if age > 0:
            return age
        else:
            print_error("Age must be greater than 0!")
            return None
    except ValueError:
        print_error("Please enter a valid age (integer)!")
        return None
    except EOFError:
        print_error("Input ended unexpectedly. Age not set.")
        return None


def input_phone(prompt="Phone: "):
    """Get a phone string containing only digits and common phone chars."""
    try:
        user_input = input(f"  {Color.BOLD}{Color.YELLOW}→{Color.END} {prompt}").strip()
        if not user_input:
            return None
        if len(user_input) > 20:
            print_error("Phone number is too long (max 20 characters)!")
            return None
        if len(user_input) < 7:
            print_error("Phone number is too short (min 7 characters)!")
            return None
        allowed = set("0123456789+- ()")
        if all(c in allowed for c in user_input):
            return user_input
        else:
            print_error("Phone contains invalid characters! Use only: 0-9, +, -, space, ( )")
            return None
    except EOFError:
        print_error("Input ended unexpectedly. Phone not set.")
        return None


def input_address(prompt="Address: "):
    """Get a non-empty address string; returns None if blank."""
    try:
        user_input = input(f"  {Color.BOLD}{Color.YELLOW}→{Color.END} {prompt}").strip()
        if not user_input:
            return None
        if len(user_input) > 100:
            print_error("Address is too long (max 100 characters)!")
            return None
        if len(user_input) < 3:
            print_error("Address is too short (min 3 characters)!")
            return None
        return user_input
    except EOFError:
        print_error("Input ended unexpectedly. Address not set.")
        return None


def safe_input(prompt):
    """Get text input with formatting"""
    try:
        user_input = input(f"  {Color.BOLD}{Color.YELLOW}→{Color.END} {prompt}").strip()
        return user_input
    except EOFError:
        print_error("Input ended unexpectedly. Empty string returned.")
        return ""


def input_symptoms(prompt="Symptoms (comma-separated): "):
    """Get multiple symptoms as comma-separated input and clean them"""
    try:
        user_input = input(f"  {Color.BOLD}{Color.YELLOW}→{Color.END} {prompt}").strip()
        if not user_input:
            return ""
        if len(user_input) > 200:
            print_error("Symptoms text is too long (max 200 characters)!")
            return ""
        # Split by comma, strip whitespace from each symptom, and rejoin
        symptoms = [s.strip() for s in user_input.split(",") if s.strip()]
        return ", ".join(symptoms)
    except EOFError:
        print_error("Input ended unexpectedly. No symptoms entered.")
        return ""
