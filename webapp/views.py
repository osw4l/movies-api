from __future__ import print_function

from rest_framework.views import APIView
from rest_framework.response import Response
from . functions import *


class movieList(APIView):
    def get(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        table_name = body['table_name']
        if len(body.keys()) == 1 and 'table_name' in body.keys():
            return Response(read_table(table_name))
        else:
            year = int(body['year'])
            title = body['title']
            return Response(read(table_name, year, title))

    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        table_name = body['table_name']
        year = int(body['year'])
        title = body['title']
        info = body['info']
        return Response(create(table_name, title, year, info))

    def put(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        table_name = body['table_name']
        year = int(body['year'])
        title = body['title']
        rating = body['info']['rating']
        plot = body['info']['plot']
        return Response(update(table_name, year, title, rating, plot))

    def delete(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        table_name = body['table_name']
        year = int(body['year'])
        title = body['title']
        return Response(delete(table_name, title, year))



