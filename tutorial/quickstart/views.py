from .models import Contact
from .models import Montact
from .serializers import ContactSerializer
from .serializers import MontactSerializer
from rest_framework import generics


class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    #def list(self, request, *args, **kwargs):
        #queryset = Contact.objects.all()

        # response.Response({"results": self.get_serializer(queryset, many=True).data}, status=200)

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class MontactList(generics.ListCreateAPIView):
    queryset = Montact.objects.all()
    serializer_class = MontactSerializer

class MontactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Montact.objects.all()
    serializer_class = MontactSerializer




# Create your views here.

# Create your views here.
