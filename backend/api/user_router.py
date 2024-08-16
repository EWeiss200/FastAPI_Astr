from fastapi import APIRouter,Depends,HTTPException,Response,Cookie
from repositories.user import UserRepository
from .dependencies import user_service
from services.user import UserSercvice
from auth.auth import current_user
from models.models import User
from schemas.schemas import Direction,GymStatus
from fastapi_cache.decorator import cache
from fastapi import BackgroundTasks
from tasks.tasks import send_email_up_gymstatus
from fastapi.responses import JSONResponse
from pydantic import ValidationError,EmailStr
from config import ADMIN
from fastapi.responses import RedirectResponse


router = APIRouter(
    tags=["user_bd"],
    prefix="/user_bd"
)


@router.delete("/del")
async def delete_one(
    id: int,
    user_service : UserSercvice = Depends(user_service),
    user: User = Depends(current_user)
):
    user_id = await user_service.delete_one(id)
    return {"delete_user": user_id}

@router.get("/all")
@cache(expire=30)
async def find_all(
    user_service:UserSercvice = Depends(user_service),
    user:User = Depends(current_user)
):  
    if user.is_superuser:
        user_all = await user_service.find_all()
        return user_all
    raise HTTPException(status_code=403,detail="Forbidden")
    
@router.get("/filter/direction")

async def find_all_by_direction(
    direction: Direction,
    user_service: UserSercvice = Depends(user_service),
    user: User = Depends(current_user)
):
    user_res = await user_service.filter_by_direction(direction)
    return user_res

@router.get('/verification_user')
async def verification_get_key(
    token: int,
    user_service: UserSercvice = Depends(user_service),
    
):
    
    #try:
        #decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        #return decoded_token if decoded_token["expires"] >= time.time() else None
    #except:
        #return {}
    #res = await user_service.verification_user(token)
    #if res:
        #return res
    #else:
        #raise HTTPException(status_code=403, detail="BAD_TOKEN")
    print(cookie_email_token)


@router.get("/filter/gym_status")
@cache(expire=30)
async def find_all_by_fym_status(
    gym_status: GymStatus,
    user_service: UserSercvice = Depends(user_service),
    user: User = Depends(current_user)
):
    user_res = await user_service.filter_by_gym_status(gym_status)
    return user_res





@router.get('/verification_get_key')
async def verification_get_key(
    response: Response,
    email : EmailStr,
    user_service: UserSercvice = Depends(user_service),
    
):
    
    token = await user_service.verification_user_get_token(email)
    response.set_cookie(key="cookie_email_token", value=token)

    



@router.get("/get_user_by_email")
async def get_user_info_by_email(
    user_service: UserSercvice = Depends(user_service),
    user: User = Depends(current_user)
):
    response, tasks= await user_service.get_user_info_by_email(user.id)
    return JSONResponse(response, background=tasks)


@router.get("/{id}")
async def get_user(
    id: int,
    user_service: UserSercvice = Depends(user_service),
    user: User = Depends(current_user)
):
    user = await user_service.find_one_by_id(id)
    return user


@router.post("/copmpleting_workout")
async def completing_workout(
    user_service: UserSercvice = Depends(user_service),
    user: User = Depends(current_user)
    
):
    response, tasks= await user_service.completing_workout(user.id)
    if tasks:
        return JSONResponse(response, background=tasks)
    else:
        return response
    









