import streamlit as st
import pandas as pd
import random

# List of predefined student names
student_names = ['Ali', 'Ayesha', 'Alina', 'Alyana', 'Ayan', 'Alisha', 'Mira']

# Function to generate student data
def generate_student_data(num_students):
    student_data = []
    for _ in range(num_students):
        student = {
            'Student ID': random.randint(100000, 999999),  # Random 6-digit student ID
            'Name': random.choice(student_names),  # Randomly pick from the predefined names
            'Age': random.randint(18, 25),  # Random age between 18 and 25
            'Gender': random.choice(['Male', 'Female', 'Other']),  # Random gender
            'Email': f"{random.choice(student_names).lower()}@example.com",  # Generate a simple email
            'Major': random.choice(['Computer Science', 'Mathematics', 'Physics', 'Biology', 'Engineering']),  # Random major
            'GPA': round(random.uniform(2.0, 4.0), 2)  # Random GPA between 2.0 and 4.0
        }
        student_data.append(student)
    return student_data

# Streamlit UI components
st.title("Student Data Generator")

# User input for number of students
num_students = st.number_input("Number of students to generate:", min_value=1, max_value=1000, value=10)

# Button to generate data
if st.button("Generate Data"):
    student_data = generate_student_data(num_students)
    df = pd.DataFrame(student_data)

    # Show data
    st.write(f"Generated {num_students} student records:")
    st.dataframe(df)
    
    # Convert DataFrame to CSV
    csv = df.to_csv(index=False)

    # Download button for CSV
    st.download_button("Download CSV", csv, "student_data.csv", "text/csv")

# Footer
st.markdown(
    """
    <footer style="text-align: center;">
    <p>Made with Manahil Nadeem! <br/>using Streamlit and Random Data Generation.</p>
    </footer>
    """,
    unsafe_allow_html=True,
)
