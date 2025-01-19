from django.core.management.base import BaseCommand
from students.models import Student, Report


class Command(BaseCommand):
    # help = "Load data from csv file into the database"

    def handle(self, *args, **kwargs):
        def ranking(score:float):
            if score > 9.9:
                score = 9.9
            elif score < 2.0:
                score = 2.0
            return int(score//2) - 1
        
        Report.objects.all().delete()
        subjects = ["toan", "ngu_van", "ngoai_ngu", "vat_li", "hoa_hoc", "sinh_hoc", "lich_su", "dia_li", "gdcd"]
        records = {subject: [0, 0, 0, 0] for subject in subjects}
        for student in Student.objects.all():
            for subject in subjects:
                score = getattr(student, subject)
                if score:
                    level = ranking(score)
                    records[subject][level] += 1

        for subject in records:
            for level in range(4):
                Report.objects.create(subject=subject, level=level, student_count=records[subject][level])


        self.stdout.write(self.style.SUCCESS("Reports generated successfully."))
