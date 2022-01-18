from .Achievement import Achievement
from .User import User
from .Event import Event
from .. import db
from .otp import OTP
from .Complain import Complain
from .Career import Career
from .Academic import Academic

# relations
# Association table to model the many-many relationship of User and Event
user_event_assosiation=db.Table("user_event",
                                db.Column("user_id",db.Integer,db.ForeignKey('user.id')),
                                db.Column("event_id",db.Integer,db.ForeignKey('event.id')))