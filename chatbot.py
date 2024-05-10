search_tree = {
    "admission": {
        "cutoff": "The admission cutoff for our college varies each year depending on several factors including the number of applicants and the performance in entrance exams. For detailed information on admission cutoff, please contact the college admission office.",
        "fee": "The fee structure for our college is designed considering various factors such as tuition fees, hostel charges (if applicable), and other miscellaneous expenses. For detailed information on the fee structure, please contact the college administration.",
        "branch": "Our college offers a wide range of branches including Computer Science, Information Technology, Electronics and Telecommunication, Mechanical Engineering, Electrical Engineering, and Civil Engineering.",
    },
    "hostel": "Our college provides hostel facilities for both boys and girls within the campus premises. The hostels are equipped with all necessary amenities to ensure a comfortable stay for students.",
    "placement": {
        "statistics": "Our college has a dedicated placement cell that works towards providing excellent placement opportunities for students. The placement statistics vary each year, and detailed information can be obtained from the college placement cell.",
        "activities": "To enhance the employability skills of students, our college conducts various placement activities including workshops, seminars, mock interviews, and aptitude tests.",
    },
    "library": "Our college library is a treasure trove of knowledge with a vast collection of books, journals, and digital resources. It serves as the hub for academic research and provides a conducive environment for learning and self-study.",
    "timetable": "The college timetable is prepared at the beginning of each academic semester and is made available to students through the college portal or notice boards. It includes details of classes, practical sessions, and other academic activities.",
    "syllabus": "The syllabus for each course is carefully designed by expert faculty members to ensure comprehensive coverage of all relevant topics. It is periodically updated to align with the latest industry trends and academic standards.",
    "contact": "For any queries or information related to admissions, placements, or other college activities, please feel free to contact the college administration at [college contact details].",
    "events": "Our college organizes various cultural, technical, and sports events throughout the year to provide students with opportunities for holistic development and recreation. Stay tuned to our college notice boards for updates on upcoming events.",
    "facilities": "Our college provides state-of-the-art facilities including laboratories, auditoriums, sports complexes, and cafeteria to cater to the diverse needs of students.",
    "faculty": "Our faculty members are highly qualified and experienced professionals who are dedicated to providing quality education and mentorship to students.",
    "research": "Our college encourages and supports research activities among students and faculty members. We have well-equipped research labs and collaborations with industry partners to facilitate research projects.",
    "clubs": "Our college hosts various clubs and societies catering to diverse interests such as technical, cultural, sports, and social causes. Joining these clubs provides students with opportunities for skill development and networking.",
    "internships": "Our college facilitates internships for students to gain practical experience and exposure in their respective fields. The placement cell assists students in securing internships with reputed companies.",
    "scholarships": "Our college offers scholarships to meritorious and deserving students based on academic performance, financial need, and other criteria. Detailed information about scholarships and eligibility criteria can be obtained from the college administration.",
    "alumni": "Our college has a strong alumni network comprising successful professionals in various fields. Alumni often contribute to the college's growth by providing mentorship, networking opportunities, and support for current students.",
}


def search(query: str, subtree):
    if type(subtree) == str:
        print(f"Reply: {subtree}")
        return
    children = list(subtree.keys())
    for child in children:
        if child in query:
            search(query, subtree[child])
            break
    else:
        print("Could not understand the context. Available options are: ")
        print(children)


while True:
    question = input("Enter your query: ")
    search(question, search_tree)
