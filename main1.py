import random


days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
periods_per_day = 6
# Classes
classes = ["Class 6A", "Class 6B", "Class 7A", "Class 7B"]

# Subjects
subjects = ["Mathematics", "Science", "English", "Social Studies", "Computer Science", "Physical Education"]

class_subject_periods = {
    "Class 6A": {"Mathematics": 6, "Science": 6, "English": 6, "Social Studies": 6, "Computer Science": 3, "Physical Education": 3},
    "Class 6B": {"Mathematics": 6, "Science": 6, "English": 6, "Social Studies": 6, "Computer Science": 3, "Physical Education": 3},
    "Class 7A": {"Mathematics": 6, "Science": 6, "English": 6, "Social Studies": 6, "Computer Science": 4, "Physical Education": 2},
    "Class 7B": {"Mathematics": 6, "Science": 6, "English": 6, "Social Studies": 6, "Computer Science": 4, "Physical Education": 2}
}

# Teachers and their teaching capabilities
# {teacher_name: [list_of_subjects_they_can_teach]}
teachers = {
    "Mr. Kumar": ["Mathematics"],
    "Mrs. Sharma": ["Mathematics"],
    "Ms. Gupta": ["Science"],
    "Mr. Singh": ["Science", "Social Studies"],
    "Mrs. Patel": ["English"],
    "Mr. Joshi": ["English", "Social Studies"],
    "Mr. Malhotra": ["Computer Science"],
    "Mr. Chauhan": ["Physical Education"]
}

def generate_timetable():
    """
    Generate a weekly timetable for the school based on the given constraints.
    
    Returns:
        dict: A data structure representing the complete timetable
              Format: {day: {period: {class: (subject, teacher)}}}
    """
    # Initialize an empty timetable
    timetable = {day: {period: {} for period in range(1, periods_per_day + 1)} for day in days_of_week}
    
    # Generate all possible time slots and shuffle them
    all_slots = [(day, period) for day in days_of_week for period in range(1, periods_per_day + 1)]
    random.shuffle(all_slots)
    
    # Calculate required PE and CS periods
    total_pe = sum(class_subject_periods[cls]["Physical Education"] for cls in classes)
    total_cs = sum(class_subject_periods[cls]["Computer Science"] for cls in classes)
    
    # Split into PE and CS slots
    pe_slots = all_slots[:total_pe]
    cs_slots = all_slots[total_pe:total_pe + total_cs]
    
    # Assign PE slots to classes
    pe_index = 0
    for class_name in classes:
        required_pe = class_subject_periods[class_name]["Physical Education"]
        for _ in range(required_pe):
            if pe_index >= len(pe_slots):
                return None  # Not enough PE slots (should not happen per problem constraints)
            day, period = pe_slots[pe_index]
            timetable[day][period][class_name] = ("Physical Education", "Mr. Chauhan")
            pe_index += 1
    
    # Assign CS slots to classes
    cs_index = 0
    for class_name in classes:
        required_cs = class_subject_periods[class_name]["Computer Science"]
        for _ in range(required_cs):
            if cs_index >= len(cs_slots):
                return None  # Not enough CS slots (should not happen per problem constraints)
            day, period = cs_slots[cs_index]
            timetable[day][period][class_name] = ("Computer Science", "Mr. Malhotra")
            cs_index += 1
    
    # Assign other subjects to remaining slots for each class
    for class_name in classes:
        # Collect required other subjects
        other_subjects = []
        for subject in ["Mathematics", "Science", "English", "Social Studies"]:
            count = class_subject_periods[class_name].get(subject, 0)
            other_subjects.extend([subject] * count)
        random.shuffle(other_subjects)
        
        # Determine occupied slots (PE and CS)
        occupied = []
        for day in days_of_week:
            for period in range(1, periods_per_day + 1):
                entry = timetable[day][period].get(class_name, None)
                if entry and entry[0] in ["Physical Education", "Computer Science"]:
                    occupied.append((day, period))
        
        # Collect remaining slots
        remaining_slots = []
        for day in days_of_week:
            for period in range(1, periods_per_day + 1):
                if (day, period) not in occupied:
                    remaining_slots.append((day, period))
        
        # Assign other subjects to remaining slots
        if len(remaining_slots) != len(other_subjects):
            return None  # Mismatch (should not happen)
        for i, (day, period) in enumerate(remaining_slots):
            subject = other_subjects[i]
            timetable[day][period][class_name] = (subject, None)
    
    # Assign teachers to other subjects
    for day in days_of_week:
        for period in range(1, periods_per_day + 1):
            current_period = timetable[day][period]
            # Collect unassigned classes and their subjects
            unassigned = []
            assigned_teachers = set()
            for cls in classes:
                entry = current_period.get(cls, None)
                if entry:
                    subject, teacher = entry
                    if teacher is None:
                        unassigned.append((cls, subject))
                    else:
                        assigned_teachers.add(teacher)
            
            # Sort unassigned by number of possible teachers (ascending)
            unassigned.sort(key=lambda x: len([t for t in teachers if x[1] in teachers[t]]))
            
            # Assign teachers
            for cls, subject in unassigned:
                possible_teachers = [t for t in teachers if subject in teachers[t]]
                available_teachers = [t for t in possible_teachers if t not in assigned_teachers]
                if not available_teachers:
                    return None  # No teacher available (should not happen with valid input)
                chosen = available_teachers[0]
                current_period[cls] = (subject, chosen)
                assigned_teachers.add(chosen)
    
    return timetable

def display_timetable(timetable):
    """
    Display the generated timetable in a readable format.
    
    Args:
        timetable (dict): The generated timetable
    """
    # Display for each class
    for class_name in classes:
        print(f"\nTimetable for {class_name}:")
        for day in days_of_week:
            print(f"\n{day}:")
            for period in range(1, periods_per_day + 1):
                entry = timetable[day][period].get(class_name, None)
                if entry:
                    subject, teacher = entry
                    print(f"Period {period}: {subject} ({teacher})")
                else:
                    print(f"Period {period}: Free")
    
    # Display for each teacher
    teacher_schedules = {teacher: {day: {period: [] for period in range(1, periods_per_day + 1)} for day in days_of_week} for teacher in teachers}
    for day in days_of_week:
        for period in range(1, periods_per_day + 1):
            for class_name in classes:
                entry = timetable[day][period].get(class_name, None)
                if entry:
                    subject, teacher = entry
                    teacher_schedules[teacher][day][period].append( (class_name, subject) )
    
    for teacher in teachers:
        print(f"\nSchedule for {teacher}:")
        for day in days_of_week:
            print(f"\n{day}:")
            for period in range(1, periods_per_day + 1):
                entries = teacher_schedules[teacher][day][period]
                if entries:
                    class_subjects = ", ".join([f"{cls} ({subj})" for cls, subj in entries])
                    print(f"Period {period}: {class_subjects}")
                else:
                    print(f"Period {period}: Free")

def validate_timetable(timetable):
    """
    Validate that the generated timetable meets all constraints.
    
    Args:
        timetable (dict): The generated timetable
        
    Returns:
        bool: True if timetable is valid, False otherwise
        str: Error message if timetable is invalid
    """
    # Check all periods are filled for each class
    for class_name in classes:
        for day in days_of_week:
            for period in range(1, periods_per_day + 1):
                if class_name not in timetable[day][period]:
                    return False, f"Missing entry for {class_name} on {day} period {period}"
    
    # Check subject period counts
    class_counts = {cls: {subj:0 for subj in subjects} for cls in classes}
    for day in days_of_week:
        for period in range(1, periods_per_day + 1):
            for cls in classes:
                entry = timetable[day][period][cls]
                subject = entry[0]
                class_counts[cls][subject] += 1
    
    for cls in classes:
        for subj, req in class_subject_periods[cls].items():
            if class_counts[cls][subj] != req:
                return False, f"Class {cls} has {class_counts[cls][subj]} periods for {subj} instead of {req}"
    
    # Check teachers qualifications
    for day in days_of_week:
        for period in range(1, periods_per_day + 1):
            for cls in classes:
                subject, teacher = timetable[day][period][cls]
                if subject not in teachers.get(teacher, []):
                    return False, f"Teacher {teacher} is not qualified to teach {subject} for {cls} on {day} period {period}"
    
    # Check teacher overlaps
    for day in days_of_week:
        for period in range(1, periods_per_day + 1):
            seen_teachers = set()
            for cls in classes:
                teacher = timetable[day][period][cls][1]
                if teacher in seen_teachers:
                    return False, f"Teacher {teacher} is teaching multiple classes on {day} period {period}"
                seen_teachers.add(teacher)
    
    return True, "Timetable is valid."

def main():
    """
    Main function to generate and display the timetable.
    """
    print("Generating school timetable...")
    
    # Generate the timetable
    timetable = generate_timetable()
    
    # Validate the timetable
    is_valid, message = validate_timetable(timetable)
    
    if is_valid:
        # Display the timetable
        display_timetable(timetable)
    else:
        print(f"Failed to generate valid timetable: {message}")

if __name__ == "__main__":
    main()