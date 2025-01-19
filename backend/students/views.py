from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from students.models import Student, Report
from students.serializers import StudentSerializer, ReportSerializer


class CheckScoreView(APIView):
    def get(self, request, sbd):
        try:
            student = Student.objects.get(sbd=sbd)
            serializer = StudentSerializer(student)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response(
                {"status": "not exist", "message": "Student with this registration number does not exist."},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ReportView(APIView):
    def get(self, request):
        try:
            reports = Report.objects.all()
            serializer = ReportSerializer(reports, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TopA00View(APIView):
    def get(self, request):
        try:
            limit = request.query_params.get("limit", 10)
            limit = int(limit)
            if limit < 1 or limit > 100:
                raise ValueError
            students = Student.objects.exclude(tong_a00=None).order_by("-tong_a00")[:limit]
            serializer = StudentSerializer(students, many=True)
            return Response({"status": "success", "limit": limit, "data": serializer.data}, status=status.HTTP_200_OK)
        except ValueError:
            return Response(
                {"status": "value error", "message": "Limit out of range."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
