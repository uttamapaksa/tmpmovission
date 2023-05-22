from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import Genre, Movie
from .serializers import GenreSerializer, MovieSerializer,MovieCommentSerializer

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)



@api_view(['GET','POST'])
def comment_list(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    print('view.py', 11111)
    if request.method == 'POST':  # 생성
        print('view.py', 22222)
        serializer = MovieCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print('view.py', 3333)
            serializer.save(movie=movie, user=user)
            return Response(serializer.data)
        else : 
            print('view.py', 44444)
            return
        
    elif request.method == 'GET':   #조회
        comments_lst = movie.TMDB_Comment.all()   #역참조, 해당 영화에 있는 댓글집합
        serializer = MovieCommentSerializer(comments_lst, many=True)
        return Response(serializer.data)


@api_view(['DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    pass
#     comment = Comment.objects.get(pk=comment_pk)


#     if request.method == 'DELETE': #삭제
#         comment.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     elif request.method == 'PUT':
#         serializer = MovieCommentSerializer(comment, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)




















# @api_view(['GET', 'POST'])
# # @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def rating_list_create(request, movie_id):
#     movie = get_object_or_404(Movie, id=movie_id)
#     if request.method=='GET':
#         ratings = movie.ratings.all()
#         serializer= RatingSerializer(ratings, many=True)
#         return Response(serializer.data)
#     else:
#         serializer = RatingSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(user=request.user, movie=movie)
#             return Response(serializer.data)

# @api_view(['DELETE'])
# # @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def rating_delete(request, rating_pk):
#     rating = get_object_or_404(Rating, pk=rating_pk)
#     rating.delete()
#     return Response({'id': rating_pk})

# @api_view(['PUT'])
# # @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def rating_update(request,movie_pk):
#     movie = get_object_or_404(Movie, id=movie_pk)
#     rating = get_object_or_404(Rating, user=request.user)
#     rating.delete()
#     serializer = RatingSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(user=request.user, movie=movie)
#         return Response(serializer.data)