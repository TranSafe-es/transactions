# coding=utf-8
from rest_framework import views
from ssql import get_query
from django.http import JsonResponse


class ShowProducts(views.APIView):

    @staticmethod
    def get(request, id_app, id_luz):
        result = get_query("SELECT [IDModeloProduto], [Codigo], [Descricao], [TipoAplicacao], [DistribuicaoLuz], [LinguaDefault] FROM [IEA_Configurador].[dbo].[ftModeloProduto] WHERE [TipoAplicacao] = %d AND [DistribuicaoLuz] = %d;", id_app, id_luz)
        return JsonResponse(result, safe=False)

