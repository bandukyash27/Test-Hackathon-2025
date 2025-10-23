from ninja import NinjaAPI

router=NinjaAPI()


@router.get('/hello/')
def hello(request):
    return {
        "message":"Helllo Django ninja"
    }