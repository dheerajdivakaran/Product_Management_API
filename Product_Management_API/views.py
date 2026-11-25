from rest_framework.views import APIView
from rest_framework.response import Response
from Product_Management_API.serializers import RegistrationSerializer, ProductSerializers
from Product_Management_API.models import ProductDb
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

class Register(APIView):

    def post(self, request):
        serializer_instance = RegistrationSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()

            return Response({
                "message": "Successfully registered"
            })

        else:
            return Response(serializer_instance.errors, status=400)

class ProductCreateList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        qs = ProductDb.objects.filter(user=request.user)
        serializer_instance = ProductSerializers(qs,many=True)
        return Response(serializer_instance.data)

    def post(self,request):
        serializer_instance = ProductSerializers(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save(user=request.user)
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class ProductRetrieveUpdateView(APIView):
     permission_classes = [IsAuthenticated]

     def get(self,request,id):
         qs = get_object_or_404(ProductDb,id=id,user=request.user)
         serializer_instance = ProductSerializers(qs)
         return Response(serializer_instance.data)

     def put(self,request,id):
         qs =get_object_or_404(ProductDb,id=id,)
         serializer_instance = ProductSerializers(data=request.data,instance=qs)
         if serializer_instance.is_valid():
             serializer_instance.save(user=request.user)
             return Response(serializer_instance.data)
         else:
             return Response(serializer_instance.errors)

     def delete(self,request,id):
         qs = get_object_or_404(ProductDb,id=id)
         qs.delete()
         return Response(
             {
                 "message" : "deleted successfully"
             }
         )
    

    




