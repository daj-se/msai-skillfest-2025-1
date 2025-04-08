from rest_framework.views import APIView
from rest_framework.response import Response
from .models import users_collection, teams_collection, activities_collection, leaderboard_collection, workouts_collection
from django.conf import settings
from bson import ObjectId

def convert_objectid_to_str(data):
    if isinstance(data, list):
        return [convert_objectid_to_str(item) for item in data]
    elif isinstance(data, dict):
        return {key: (str(value) if isinstance(value, ObjectId) else convert_objectid_to_str(value)) for key, value in data.items()}
    elif isinstance(data, ObjectId):
        return str(data)
    return data

class ApiRootView(APIView):
    def get(self, request):
        base_url = "https://fictional-goggles-4vp7gv5pwgh5q6x-8000.app.github.dev" if "fictional-goggles" in request.get_host() else "http://localhost:8000"
        return Response({
            "users": f"{base_url}/api/users/",
            "teams": f"{base_url}/api/teams/",
            "activities": f"{base_url}/api/activities/",
            "leaderboard": f"{base_url}/api/leaderboard/",
            "workouts": f"{base_url}/api/workouts/",
        })

class UserViewSet(APIView):
    def get(self, request):
        users = list(users_collection.find({}, {"_id": 0}))
        return Response(users)

class TeamViewSet(APIView):
    def get(self, request):
        teams = list(teams_collection.find({}, {"_id": 0}))
        teams = convert_objectid_to_str(teams)
        return Response(teams)

class ActivityViewSet(APIView):
    def get(self, request):
        activities = list(activities_collection.find({}, {"_id": 0}))
        activities = convert_objectid_to_str(activities)
        return Response(activities)

class LeaderboardViewSet(APIView):
    def get(self, request):
        leaderboard = list(leaderboard_collection.find({}, {"_id": 0}))
        leaderboard = convert_objectid_to_str(leaderboard)
        return Response(leaderboard)

class WorkoutViewSet(APIView):
    def get(self, request):
        workouts = list(workouts_collection.find({}, {"_id": 0}))
        return Response(workouts)