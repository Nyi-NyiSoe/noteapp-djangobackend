from rest_framework.decorators import api_view
from rest_framework.response import Response    
from . models import Note
from . serializers import NoteSerializer




@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request,id):
    note = Note.objects.get(id=id)
    serializer = NoteSerializer(note,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addNote(request):
    data = request.data
    note = Note.objects.create(
        
        content = data['content']
    )
    serializer = NoteSerializer(note,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateNote(request,id):
    
    note = Note.objects.get(id=id)
    serializer = NoteSerializer(note,data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
@api_view(['DELETE']) 
def deleteNote(request,id):
    note = Note.objects.get(id=id)
    note.delete()
    return Response('Note was deleted')






    