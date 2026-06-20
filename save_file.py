"""
Simple file save helper for the Hospital Management System
Saves patient information to a plain TXT file using only open(), write(), close().

Usage example:
    from save_file import save_patient_list
    save_patient_list(list_of_patient_objects, 'patients.txt')

Each line in the file will contain: pid | name | age | phone | address | symptom | severity\n
This module intentionally keeps I/O simple for teaching purposes.
"""


def save_patient_list(patients, filename="patients.txt"):
    """Save a list (iterable) of Patient objects to a text file.

    Args:
        patients: iterable of Patient objects (must have attributes: pid, name, age, phone, address, symptom, severity)
        filename: target filename (default: patients.txt)
    Returns:
        None
    """
    # Open the file for writing (overwrites existing file)
    f = open(filename, "w", encoding="utf-8")

    # Write a simple header line
    f.write("pid | name | age | phone | address | symptom | severity\n")

    for p in patients:
        # Prepare a safe line: convert attributes to string and replace newlines
        line = (
            str(p.pid).replace("\n", " ") + " | " +
            str(p.name).replace("\n", " ") + " | " +
            str(getattr(p, "age", "")).replace("\n", " ") + " | " +
            str(getattr(p, "phone", "")).replace("\n", " ") + " | " +
            str(getattr(p, "address", "")).replace("\n", " ") + " | " +
            str(getattr(p, "symptom", "")).replace("\n", " ") + " | " +
            str(getattr(p, "severity", ""))
        )
        f.write(line + "\n")

    # Close the file to ensure data is flushed
    f.close()


if __name__ == "__main__":
    print("This module provides save_patient_list(patients, filename) to save patients to a TXT file.")
    print("Import and call save_patient_list() from your application code.")
