# main.py

from patient import Patient
from triage_patient import Emergency_queue


# Create queue
queue = Emergency_queue()
# Create patients
# 1 = Critical
# 2 = Urgent
# 3 = Moderate
# 4 = Normal
p1 = Patient("P101","Tom",10020,4)
p2 = Patient("P102","Anna",-20,1)
p3 = Patient("P103","Jack",30,2)
p4 = Patient("P104","Lisa",19,4)
# Add patients
queue.add_patient(p1)
queue.add_patient(p2)
queue.add_patient(p3)
queue.add_patient(p4)
# Display queue
queue.display_queue()
# Peek next patient
print("\n--- Peek Patient ---")
next_patient = queue.peek()
if next_patient:
    print(
        f"Next Patient: "
        f"{next_patient.pid} - "
        f"{next_patient.name}"
    )
# Update severity
print("\n--- Update Severity ---")

queue.update_patient_severity(
    "P104",
    1
)


# Display queue again
queue.display_queue()


# Remove next patient
print("\n--- Remove Patient ---")

queue.call_next_patient()


# Display queue again
queue.display_queue()


