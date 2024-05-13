def is_safe(board, row, col, n):
    # Check if there's a student in the same column
    for i in range(row):
        if board[i][col] != '-':
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] != '-':
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] != '-':
            return False
    
    return True

def solve_n_queens_util(board, row, n, students):
    if row == n:
        return True
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = students[row]
            if solve_n_queens_util(board, row + 1, n, students):
                return True
            board[row][col] = '-'
    
    return False

def mix_sections(section1_students, section2_students):
    all_students = []
    min_len = min(len(section1_students), len(section2_students))
    for i in range(min_len):
        all_students.append(section1_students[i])
        all_students.append(section2_students[i])
    if len(section1_students) > len(section2_students):
        all_students.extend(section1_students[min_len:])
    else:
        all_students.extend(section2_students[min_len:])
    return all_students

def solve_seating_arrangement(all_students):
    n = len(all_students)
    board = [['-' for _ in range(n)] for _ in range(n)]
    if not solve_n_queens_util(board, 0, n, all_students):
        print("No seating arrangement possible.")
        return
    
    print("Seating Arrangement:")
    for row in board:
        print(' '.join(row))

# Prompt user for input
def get_student_input():
    section1_name = input("Enter section 1 name: ")
    print(f"Enter students' names for section {section1_name}:")
    section1_students = []
    while True:
        student = input("Enter student name (or type 'done' to finish): ")
        if student.lower() == 'done':
            break
        section1_students.append(student)
    section2_name = input("Enter section 2 name: ")
    print(f"Enter students' names for section {section2_name}:")
    section2_students = []
    while True:
        student = input("Enter student name (or type 'done' to finish): ")
        if student.lower() == 'done':
            break
        section2_students.append(student)
    all_students = mix_sections(section1_students, section2_students)
    return all_students

students_input = get_student_input()
solve_seating_arrangement(students_input)