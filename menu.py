"""
Menu display module for Hospital Patient Management System
Handles all UI and menu-related functionality
"""

import os


class InputCancelledError(Exception):
    """Raised when the user enters invalid input for the current action."""


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
        ("6", "🗑️  Delete Medical Record"),
        ("7", "📖 Display Medical History"),
        ("8", "🔍 Find Patient History"),
        ("9", "📝 Add New Medical Record"),
        ("10", "🚑 Process Next Patient"),
        ("11", "📥 Display Queue"),
        ("0", "🚪 Exit"),
    ]
    
    for num, title in menu_items:
        if num == "0":
            print(f"\n  {Color.RED}{Color.BOLD}[{num}] {title}{Color.END}")
        else:
            print(f"  {Color.CYAN}{Color.BOLD}[{num}] {Color.END}{title}")
    
    print(f"\n{Color.BOLD}{Color.CYAN}{'─'*60}{Color.END}\n")


def input_int(prompt, default=None, allow_blank=False):
    """Get integer input with formatting."""
    try:
        user_input = input(f"  {Color.BOLD}{Color.YELLOW}→{Color.END} {prompt}").strip()
        if not user_input:
            if allow_blank:
                return default
            raise InputCancelledError("Input cancelled. Returning to menu.")
        return int(user_input)
    except ValueError as exc:
        raise InputCancelledError("Please enter a valid integer!") from exc
    except EOFError as exc:
        raise InputCancelledError("Input ended unexpectedly. Returning to menu.") from exc


def input_age(prompt="Age: ", allow_blank=False):
    """Get a positive integer age from user."""
    try:
        user_input = input(f"  {Color.BOLD}{Color.YELLOW}→{Color.END} {prompt}").strip()
        if not user_input:
            if allow_blank:
                return None
            raise InputCancelledError("Age input cancelled. Returning to menu.")
        age = int(user_input)
        if age < 0:
            raise InputCancelledError("Age cannot be negative!")
        if age > 150:
            raise InputCancelledError("Age seems unrealistic (max 150)!")
        if age > 0:
            return age
        raise InputCancelledError("Age must be greater than 0!")
    except ValueError as exc:
        raise InputCancelledError("Please enter a valid age (integer)!") from exc
    except EOFError as exc:
        raise InputCancelledError("Input ended unexpectedly. Age not set.") from exc


def input_phone(prompt="Phone: ", allow_blank=False):
    """Get a phone string containing only digits and common phone chars."""
    try:
        user_input = input(f"  {Color.BOLD}{Color.YELLOW}→{Color.END} {prompt}").strip()
        if not user_input:
            if allow_blank:
                return None
            raise InputCancelledError("Phone input cancelled. Returning to menu.")
        if len(user_input) > 20:
            raise InputCancelledError("Phone number is too long (max 20 characters)!")
        if len(user_input) < 7:
            raise InputCancelledError("Phone number is too short (min 7 characters)!")
        allowed = set("0123456789+- ()")
        if all(c in allowed for c in user_input):
            return user_input
        raise InputCancelledError("Phone contains invalid characters! Use only: 0-9, +, -, space, ( )")
    except EOFError as exc:
        raise InputCancelledError("Input ended unexpectedly. Phone not set.") from exc


def input_address(prompt="Address: ", allow_blank=False):
    """Get a non-empty address string."""
    try:
        user_input = input(f"  {Color.BOLD}{Color.YELLOW}→{Color.END} {prompt}").strip()
        if not user_input:
            if allow_blank:
                return None
            raise InputCancelledError("Address input cancelled. Returning to menu.")
        if len(user_input) > 100:
            raise InputCancelledError("Address is too long (max 100 characters)!")
        if len(user_input) < 3:
            raise InputCancelledError("Address is too short (min 3 characters)!")
        return user_input
    except EOFError as exc:
        raise InputCancelledError("Input ended unexpectedly. Address not set.") from exc


def safe_input(prompt, allow_blank=False):
    """Get text input with formatting."""
    try:
        user_input = input(f"  {Color.BOLD}{Color.YELLOW}→{Color.END} {prompt}").strip()
        if not user_input and not allow_blank:
            raise InputCancelledError("Input cancelled. Returning to menu.")
        return user_input
    except EOFError as exc:
        raise InputCancelledError("Input ended unexpectedly. Empty string returned.") from exc


def input_symptoms(prompt="Symptoms (comma-separated): ", allow_blank=True):
    """Get multiple symptoms as comma-separated input and clean them."""
    try:
        user_input = input(f"  {Color.BOLD}{Color.YELLOW}→{Color.END} {prompt}").strip()
        if not user_input:
            if allow_blank:
                return ""
            raise InputCancelledError("Symptoms input cancelled. Returning to menu.")
        if len(user_input) > 200:
            raise InputCancelledError("Symptoms text is too long (max 200 characters)!")
        symptoms = [s.strip() for s in user_input.split(",") if s.strip()]
        return ", ".join(symptoms)
    except EOFError as exc:
        raise InputCancelledError("Input ended unexpectedly. No symptoms entered.") from exc
