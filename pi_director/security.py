from pyramid.security import authenticated_userid
from pi_director.models.models import DBSession
from pi_director.models.UserModel import UserModel
from sqlalchemy.orm.exc import NoResultFound
from pyramid.decorator import reify
import pdb

def LookupUser(request):
  userid=authenticated_userid(request)
  try:
    logger.debug("Looking up user session for %s", userid)
    UserObject = DBSession.query(UserModel).filter(UserModel.email==userid).one()
    return UserObject
  except NoResultFound, e:
    return None

AccessLevels = {
   -1: "group:invalid",
   0: "g:unregistered",
   1: "g:user",
   2: "g:admin",
}

def groupfinder(userid,request):
  try:
    user = DBSession.query(UserModel).filter(UserModel.email==userid).one()
    if user is not None:
      if user.AccessLevel >= 0:
        return[AccessLevels[user.AccessLevel]]
  except NoResultFound, e:
    return None

