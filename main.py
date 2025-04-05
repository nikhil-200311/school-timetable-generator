#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
School Timetable Generator

This program generates an optimal weekly timetable for a school based on 
classes, subjects, teachers, and period requirements.
"""

### DO NOT MODIFY THE CODE BELOW THIS LINE ###

# Define the input constraints
# Classes
classes = ["Class 6A", "Class 6B", "Class 7A", "Class 7B"]

# Subjects
subjects = ["Mathematics", "Science", "English", "Social Studies", "Computer Science", "Physical Education"]

# Weekly period requirements for each class and subject
# {class_name: {subject_name: number_of_periods_per_week}}
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

# School timing configuration
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
periods_per_day = 6

### DO NOT MODIFY THE CODE ABOVE THIS LINE ###

def generate_timetable():
    """
    Generate a weekly timetable for the school based on the given constraints.
    
    Returns:
        dict: A data structure representing the complete timetable
              Format: {day: {period: {class: (subject, teacher)}}}
    """
    # Initialize an empty timetable
    timetable = {day: {period: {} for period in range(1, periods_per_day + 1)} for day in days_of_week}
    print(timetable)
    remaining_periods = {cls: class_subject_periods[cls].copy() for cls in classes}
    teacher_schedule = {teacher: {day: set() for day in days_of_week} for teacher in teachers}

    def can_assign(day, period, cls, subject, teacher):
        if period in teacher_schedule[teacher][day]:
            return False
        if subject not in teachers[teacher]:
            return False
        if remaining_periods[cls][subject] <= 0:
            return False
        return True

  



    
    # TODO: Implement the timetable generation algorithm
    
    # 1. Check if a valid timetable is possible with the given constraints
    

    # 2. Assign subjects and teachers to periods for each class
    # 3. Ensure all constraints are satisfied
    
    return timetable


def display_timetable(timetable):
    """
    Display the generated timetable in a readable format.
    
    Args:
        timetable (dict): The generated timetable
    """
    for cls in classes:
        print(f"Timetable for class {cls}")
        print()
    # TODO: Implement timetable display logic
    # Display the timetable for each class
    # Display the timetable for each teacher
    pass


def validate_timetable(timetable):
    """
    Validate that the generated timetable meets all constraints.
    
    Args:
        timetable (dict): The generated timetable
        
    Returns:
        bool: True if timetable is valid, False otherwise
        str: Error message if timetable is invalid
    """
    # TODO: Implement validation logic
    # Check if all classes have their required number of periods for each subject
    # Check if teachers are not double-booked
    # Check if teachers are only teaching subjects they can teach
    
    return False, "To be implemented"


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


# A. For generating timetable:
# 1. Calculate the total number of classes required to create a complete timetable for all classes, ensuring all subject period requirements are met.
# 2. Track the remaining periods needed for each class and subject to ensure all are scheduled appropriately.
# 3. Assess teacher availability by creating a schedule that tracks when each teacher is free or occupied, ensuring they can teach during specific time slots.
# 4. Verify assignment feasibility by:
#    (i) Checking if a teacher is available in a given time slot, ensuring no scheduling conflicts exist.
#    (ii) Confirming that the teacher is qualified to teach the assigned subject.
#    (iii) Ensuring the class still requires periods for the subject, avoiding over-scheduling.
# 5. If all conditions are satisfied, assign the teacher and subject to the class for that time slot, and continue filling the timetable.
# 6. Repeat the process across all days and periods, adjusting as needed to fit the weekly structure (e.g., 5 days, 6 periods per day).
# 7. Ensure the solution accommodates the fixed constraints, such as the number of periods per day and days per week.
# 8. Validate the completed timetable to confirm all requirements are met, including total periods per subject and no teacher overlaps.
# 9. Display the final timetable in a clear format, showing schedules for both classes and teachers.

# These steps outline a systematic approach to creating a balanced and functional school timetable while respecting all given constraints.