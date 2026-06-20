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
        ("1", "➕ Add Medical History"),
        ("2", "🗑️  Delete Last Medical Record"),
        ("3", "📖 Display Medical History"),
        ("4", "🔍 Find Patient History"),
        ("5", "📝 Register Patient"),
        ("6", "🔎 Find Patient"),
        ("7", "✏️  Update Patient"),
        ("8", "📤 Discharge Patient"),
        ("9", "📊 Display All Patients"),
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
        return default


def safe_input(prompt):
    """Get text input with formatting"""
    user_input = input(f"  {Color.BOLD}{Color.YELLOW}→{Color.END} {prompt}").strip()
    return user_input


def input_symptoms(prompt="Symptoms (comma-separated): "):
    """Get multiple symptoms as comma-separated input and clean them"""
    user_input = input(f"  {Color.BOLD}{Color.YELLOW}→{Color.END} {prompt}").strip()
    if not user_input:
        return ""
    # Split by comma, strip whitespace from each symptom, and rejoin
    symptoms = [s.strip() for s in user_input.split(",") if s.strip()]
    return ", ".join(symptoms)
