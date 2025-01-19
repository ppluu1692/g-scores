import os
import csv
from dotenv import load_dotenv
from django.core.management.base import BaseCommand
from students.models import Student

load_dotenv()

class Command(BaseCommand):
    help = "Load data from csv file into the database"

    def handle(self, *args, **kwargs):
        file_path = os.environ.get("DATA_PATH")
        Student.objects.all().delete()

        try:
            with open(file_path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                students = []
                invalid_rows = []

                for idx, row in enumerate(reader, start=1):
                    try:
                        sbd = row["sbd"].strip() if "sbd" in row and row["sbd"].strip() else None
                        if not sbd:
                            raise ValueError("Missing or empty registration number")

                        def parse_score(value):
                            score = None
                            if value.strip():
                                score = float(value)
                                if not (0 <= score <= 10):
                                    raise ValueError("Invalid score")

                            return score

                        scores = {
                            subject: parse_score(row[subject])
                            for subject in [
                                "toan",
                                "ngu_van",
                                "ngoai_ngu",
                                "vat_li",
                                "hoa_hoc",
                                "sinh_hoc",
                                "lich_su",
                                "dia_li",
                                "gdcd",
                            ]
                        }

                        a00 = (
                            scores["toan"] + scores["vat_li"] + scores["hoa_hoc"]
                            if scores["toan"] and scores["vat_li"] and scores["hoa_hoc"]
                            else None
                        )

                        student = Student(
                            sbd=sbd,
                            toan=scores["toan"],
                            ngu_van=scores["ngu_van"],
                            ngoai_ngu=scores["ngoai_ngu"],
                            vat_li=scores["vat_li"],
                            hoa_hoc=scores["hoa_hoc"],
                            sinh_hoc=scores["sinh_hoc"],
                            lich_su=scores["lich_su"],
                            dia_li=scores["dia_li"],
                            gdcd=scores["gdcd"],
                            ma_ngoai_ngu=row["ma_ngoai_ngu"].strip() if "ma_ngoai_ngu" in row else None,
                            tong_a00=a00
                        )
                        students.append(student)

                    except ValueError as e:
                        invalid_rows.append((idx, str(e)))

                Student.objects.bulk_create(students, ignore_conflicts=True)

                self.stdout.write(
                    self.style.SUCCESS(f"Successfully imported {len(students)} students from {file_path}")
                )

                if invalid_rows:
                    self.stdout.write(self.style.WARNING(f"{len(invalid_rows)} invalid rows found:"))
                    for row_idx, error in invalid_rows:
                        self.stdout.write(self.style.WARNING(f"Row {row_idx}: {error}"))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File {file_path} not found. Please check the path."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {str(e)}"))
