# reate a Python program to manage bug records using a class and a dictionary.


class BugTracker:
    def __init__(self):
        self.bugs = {}

    def add_bug(self, bug_id, description, severity):
        self.bugs[bug_id] = {
            "description": description,
            "severity": severity,
            "status": "Open"
        }
        print(f"Bug ID {bug_id} added.")

    def update_status(self, bug_id, new_status):
        self.bugs[bug_id]["status"] = new_status
        print(f"Bug ID {bug_id} status updated to {new_status}.")

    def list_all_bugs(self):
        for bug_id, details in self.bugs.items():
            print(f"Bug ID: {bug_id}")
            print(f"  Description: {details['description']}")
            print(f"  Severity: {details['severity']}")
            print(f"  Status: {details['status']}")
            print()

if __name__ == "__main__":
    tracker = BugTracker()
    
    tracker.add_bug(101, "Login button not working", "High")
    tracker.add_bug(102, "Page crashes on load", "Critical")
    tracker.add_bug(103, "Typo in homepage text", "Low")
    
    print("\nAll Bugs After Addition:")
    tracker.list_all_bugs()
    
    tracker.update_status(101, "In Progress")
    tracker.update_status(102, "Closed")
    
    print("\nAll Bugs After Status Updates:")
    tracker.list_all_bugs()