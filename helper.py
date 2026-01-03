from PySide6.QtWidgets import QMessageBox
import re

def show_invalid_file_dialog(self, title, text):
    msg = QMessageBox(self)
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec()

def show_info_dialog(self, title, text):
    msg = QMessageBox(self)
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec()

def clean_ocr_text(text):
    """
    Aggressively clean OCR text for any document type while preserving
    meaningful words, numbers, dates, grades, and key phrases.
    """

    # Normalize whitespace
    text = " ".join(text.split())

    # Remove repeated symbols (e.g., ----====, X-X-X-X)
    text = re.sub(r'([^\w\s])(?:\1[-\1]*){3,}', ' ', text)

    # Remove sequences of symbols that are likely garbage (≥5 chars)
    text = re.sub(r'\b[^\w\s]{5,}\b', ' ', text)

    # Remove very short nonsense tokens (1-2 chars of symbols only)
    text = re.sub(r'\b[^\w\s]{1,2}\b', ' ', text)

    # Remove stray punctuation surrounded by whitespace (like " , " or " ; ")
    text = re.sub(r'\s[^\w\s]\s', ' ', text)

    # Remove multiple consecutive non-alphanumeric symbols inside words
    text = re.sub(r'(?<=\w)[^\w\s]{2,}(?=\w)', '', text)

    # Remove stray non-printable/control characters
    text = re.sub(r'[\x00-\x1F\x7F]', '', text)

    # Final cleanup: collapse multiple spaces
    text = " ".join(text.split())

    return text

def label_to_type(labels):
    label_map = {
        "Narrativereport": "Narrative Report",
        "Notice": "Notice",
        "accomplishments": "Accomplishment Report",
        "actionplan": "Action Plan",
        "administrative": "Administrative Manual",
        "advertisementhiring": "Advertisment of Hiring",
        "app": "Approval from the Office",
        "approval": "Approval",
        "assessmentprogram": "Assessment Program",
        "attend": "Certificate of Attendance",
        "award": "Award",
        "banktransac": "Bank Transaction",
        "bulletininfomaterials": "Bulletin Of Information",
        "career": "Career Counseling Programs",
        "cert": "Certificate of Recognition",
        "certacceptance": "Certificate of Acceptance",
        "certcopyright": "Certificate of Copyright",
        "certemployment": "Certificate of Employment",
        "certenrollment": "Certificate of Enrollment",
        "certofappearance": "Certificate of Appearance",
        "certofcash": "Certificate of Cash Incentive",
        "certofmembership": "Certificate of Membership",
        "certofparticipation": "Certificate of Participation",
        "certoftraining": "Certificate of Training",
        "chedro": "Reports to CHEDRO",
        "classobserve": "Classroom Observation",
        "cofservice": "Certificate of Service",
        "collectionpolicy": "Collection Development Policy Statement",
        "collegecode": "College Code",
        "collegesyllabi": "Course Syllabi",
        "consultation": "Consultation Programs",
        "coursesyllabus": "Course Syllabus",
        "criteria": "Criteria",
        "diploma": "Diploma",
        "dtr": "Daily Time Record",
        "dutiesandresponsibilities": "Duties and Responsibilities",
        "employmentrecord": "Employment Record",
        "entranceform": "Entrance Application Form",
        "evalform": "Evaluation/Screening Form",
        "expandtraining": "Related Experiences and Trainings Attended",
        "facultypromotion": "Faculty Promotion",
        "grades of sheet": "Grades",
        "gradesofsheet": "Grades",
        "honorabledismissal": "Files of Honorable Dismissal",
        "ipcr": "Indivudual Performance Commitment Review",
        "lab": "Safety Tips",
        "letter": "Letter",
        "librarygoal": "Library Goals and Objectives",
        "manual": "Manual",
        "medicalrecord": "Medical Record",
        "memo": "Memo",
        "minutes": "Minutes of the Meeting",
        "nbc461": "NBC 461",
        "numofdropout": "Number of Drop-outs per Semester/Year",
        "ojt": "Result of OJT Evaluation",
        "orgchart10": "Organizational Chart",
        "pds": "Personal Data Sheet",
        "policy": "Policy",
        "programinvitation": "Program Invitation",
        "projectproposal": "Project Proposal",
        "proofbystudent": "Proof of Utilized Research",
        "purchaseorder": "Purchase Order",
        "purchaserequest": "Purchase Request",
        "pyroll": "Payroll",
        "researchagenda": "Research and Extension Agenda",
        "resolution": "Resolution",
        "studentinfosheet": "Student Personal Information Sheet",
        "syllabi": "Syllabi",
        "tesdacertification": "TESDA Certification",
        "thesismanuscript": "Thesis Manuscript",
        "tor": "Transcript of Records",
        "tracerstudy": "Tracer Study",
        "travelorder": "Travel Order",
        "vmgo": "College VMGO",
        "workload": "Workload Guidelines",
        "meetingagenda": "Meeting Agenda",
        "financialstatement": "Financial Statement"
    }

    types = []
    for label in labels:
        types.append(label_map[label])
    return types