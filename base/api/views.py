from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .utils import validate_animals_data, filter_valid_animals


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["GET"])
def get_routes(request):
    """returns a view containing all the possible routes"""
    routes = ["/api/token", "/api/token/refresh"]

    return Response(routes)


# In-memory storage
animals_database = [
    {"id": 1, "name": "Chicken", "quantity": 2},
    {"id": 2, "name": "Cow", "quantity": 3},
    {"id": 3, "name": "Pig", "quantity": 1},
    {"id": 4, "name": "Sheep", "quantity": 5},
    {"id": 5, "name": "Goat", "quantity": 2},
]


class FarmManagementView(APIView):
    """
    API View for managing farm records.

    This view supports the following HTTP methods: GET and POST.

    Authentication:
    Access to this view is restricted to authenticated users only.

    """

    # Permissions: Only allow authenticated users
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Handle GET requests.

        On GET request, the view filters out valid animal entries from the
        database and returns them in a HTTP Response, with a success status (200).
        """

        valid_animals_data = filter_valid_animals(animals_database)
        return Response(valid_animals_data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Handle POST requests.

        On POST request, the view receives animal data, validates it and if valid,
        saves the data into the animals database, then returns the saved data in a
        HTTP Response, with a created status (201).

        If the data is invalid, it returns a HTTP Response with an error description
        and a bad request status (400).
        """

        global animals_database  # The animals database is a global variable
        animals_data = request.data
        validate_animals = validate_animals_data(animals_data)

        # If the validation is unsuccessful (data is invalid), return an error response
        if not validate_animals.get("ok"):
            return Response(
                {"error": validate_animals.get("message")},
                status=status.HTTP_400_BAD_REQUEST,
            )

        animals_database = animals_data  # Save valid animals data into the animals_database global variable

        return Response(status=status.HTTP_201_CREATED)
