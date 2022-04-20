from rest_framework import serializers

from tickets import models


class FlightSerializer(serializers.ModelSerializer):
    """Serializes Flight Object"""

    class Meta:
        model = models.Flight
        fields = "__all__"

    def create(self, validated_data):
        flight_number = validated_data.get("flight_number", None)
        flight_time = validated_data.get("flight_time", None)
        departure_date = validated_data.get("departure_date", None)

        # raising error if flight already exists
        if models.Flight.objects.filter(
            flight_number=flight_number,
            flight_time=flight_time,
            departure_date=departure_date,
            cancelled=False,
        ).exists():
            raise serializers.ValidationError("Flight Already Exists")
        return super().create(validated_data)


class TicketSerializer(serializers.ModelSerializer):
    """Serializes Ticket Object"""

    flight_details = serializers.SerializerMethodField("get_flight_details")

    def get_flight_details(self, obj):
        return FlightSerializer(obj.flight).data

    class Meta:
        model = models.Ticket
        fields = "__all__"
        extra_fields = ("flight_details",)

    def create(self, validated_data):
        seat_no = validated_data.get("seat_no", None)
        flight = validated_data.get("flight", None)

        # raising error if ticket for that seat already exists
        if models.Ticket.objects.filter(seat_no=seat_no, flight=flight).exists():
            raise serializers.ValidationError("Ticket Already Exists")
        return super().create(validated_data)


class FilteredTicketSerializer(serializers.ModelSerializer):
    """Serializes Ticket Object"""

    flight_details = serializers.SerializerMethodField("get_flight_details")
    price = serializers.SerializerMethodField("get_price")

    def get_flight_details(self, obj):
        return FlightSerializer(obj.flight).data

    def get_price(self, obj):
        request = self.context.get("request")
        nationality = request.query_params.get("nationality")
        if nationality and str(nationality).lower() != "nepalese":
            return obj.price_for_non_nepali.amount
        return obj.price_for_nepali.amount

    class Meta:
        model = models.Ticket
        fields = [
            "ticket_class",
            "seat_no",
            "flight",
            "refundable",
            "flight_details",
            "price",
        ]
        extra_fields = ("flight_details", "price")
