from flask import Blueprint,send_file
from ...models.Event import Event
from ...utils.jwt import JWT
from io import BytesIO
poster_bp=Blueprint("poster",__name__,url_prefix="/poster")
@poster_bp.route("/<id>")
def get_poster(id):
    event=Event.query.filter_by(id=int(id)).first()
    title=event.title
    name=f"{title}_poster.jpg" if title else f"poster_{id}.jpg"
    poster=event.poster
    return send_file(BytesIO(poster),download_name=name,as_attachment=False)