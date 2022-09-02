import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from recommender.ranking import RankingModule
from recommender.serializers import RequestSerializer, ResponseSerializer


class MovieRanking(APIView):
    logging.basicConfig(filename='./MyLog.log', level=logging.INFO)

    def post(self, request):
        try:
            req_serializer = RequestSerializer(data=request.data)
            if req_serializer.is_valid():
                uid = req_serializer.data['uid']
                movie_ids = req_serializer.data['movie_ids']

                logging.info('#######################################################################')
                logging.info("[INFO] RECEIVED A REQUEST, uid: %s , movie_ids: %s", uid, movie_ids)

                ranking = RankingModule(_uid=uid, _movies=movie_ids)
                ranking.rank()

                res_serializer = ResponseSerializer(ranking)
                logging.info("[INFO] RESPONSE, uid: %s, movies: %s, results: %s",
                             uid, movie_ids, ranking.results)

                return Response(res_serializer.data, status=status.HTTP_200_OK)
            return Response(req_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValueError as e:
            return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
