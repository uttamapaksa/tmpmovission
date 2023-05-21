
from rest_framework.response import Response
from rest_framework.decorators import api_view
# # Authentication Decorators
# # from rest_framework.decorators import authentication_classes

# # permission Decorators
# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ReviewListSerializer, ReviewSerializer, Review_CommentSerializer, PartyListSerializer, PartySerializer, Party_CommentSerializer
from .models import Review, Review_Comment, Party, Party_Comment



@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def review_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        reviews = get_list_or_404(Review)
        print(reviews)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':    #게시판 생성
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):
    # article = Article.objects.get(pk=article_pk)
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def review_comment_list(request):
    if request.method == 'GET':
        # comments = Comment.objects.all()
        review_comments = get_list_or_404(Review_Comment)
        serializer = Review_CommentSerializer(review_comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def review_comment_detail(request, review_comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    review_comment = get_object_or_404(Review_Comment, pk=review_comment_pk)

    if request.method == 'GET':
        serializer = Review_CommentSerializer(review_comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review_comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = Review_CommentSerializer(review_comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    


@api_view(['POST'])
def review_comment_create(request, review_pk):
    # article = Article.objects.get(pk=article_pk)
    review = get_object_or_404(Review, pk=review_pk)
    serializer = Review_CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

#파티게시판

@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def party_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        parties = get_list_or_404(Party)
        serializer = PartyListSerializer(parties, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':    #게시판 생성
        serializer = PartySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def party_detail(request, party_pk):
    # article = Article.objects.get(pk=article_pk)
    party = get_object_or_404(Party, pk=party_pk)

    if request.method == 'GET':
        serializer = PartySerializer(party)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        party.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = PartySerializer(party, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def party_comment_list(request):
    if request.method == 'GET':
        party_comments = get_list_or_404(Party_Comment)
        serializer = Party_CommentSerializer(party_comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def party_comment_detail(request, party_comment_pk):
    party_comment = get_object_or_404(Party_Comment, pk=party_comment_pk)

    if request.method == 'GET':
        serializer = Party_CommentSerializer(party_comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        party_comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = Party_CommentSerializer(party_comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    


@api_view(['POST'])
def party_comment_create(request, party_pk):
    party = get_object_or_404(Party, pk=party_pk)
    serializer = Party_CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(party=party)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
