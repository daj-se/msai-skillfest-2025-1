from rest_framework.views import APIView
from rest_framework.response import Response
from .models import users_collection, teams_collection, activities_collection, leaderboard_collection, workouts_collection

class UserViewSet(APIView):
    def get(self, request):
        users = list(users_collection.find({}, {"_id": 0}))
        return Response(users)

class TeamViewSet(APIView):
    def get(self, request):
        teams = list(teams_collection.find({}, {"_id": 0}))
        return Response(teams)

class ActivityViewSet(APIView):
    def get(self, request):
        activities = list(activities_collection.find({}, {"_id": 0}))
        return Response(activities)

class LeaderboardViewSet(APIView):
    def get(self, request):
        leaderboard = list(leaderboard_collection.find({}, {"_id": 0}))
        return Response(leaderboard)

class WorkoutViewSet(APIView):
    def get(self, request):
        workouts = list(workouts_collection.find({}, {"_id": 0}))
        return Response(workouts)