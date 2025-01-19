from rest_framework import serializers
from students.models import Student, Report


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["sbd", "toan", "ngu_van", "ngoai_ngu", "vat_li", "hoa_hoc", "sinh_hoc", "lich_su", "dia_li", "gdcd", "ma_ngoai_ngu"]

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ["subject", "level", "student_count"]
