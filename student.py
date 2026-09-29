class Student:
    """Represents one student and their results (Week 3 OOP version)."""

    # Class attributes: shared by every Student object
    DISTINCTION_MARK = 70
    PASS_MARK = 40

    def __init__(self, name, reg_no, marks):
        # Instance attributes: belong to this one student
        self.name = name
        self.reg_no = reg_no
        self.marks = marks  # list of three unit marks

    def calculate_total(self):
        """Return the sum of all the student's marks."""
        return sum(self.marks)

    def calculate_average(self):
        """Return the average of the student's marks."""
        return self.calculate_total() / len(self.marks)

    def classify_result(self):
        """Return Distinction, Pass or Fail based on the average."""
        average = self.calculate_average()
        if average >= self.DISTINCTION_MARK:
            return "Distinction"
        elif average >= self.PASS_MARK:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return f"{self.name} ({self.reg_no}) - {self.classify_result()}"