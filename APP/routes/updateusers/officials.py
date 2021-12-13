from flask import Blueprint,request,make_response,jsonify
from ...utils.sheet import Sheet
officials_bp=Blueprint('officials',__name__,url_prefix="/officials")

@officials_bp.route('/',methods=['POST'])
def updateOfficials():
	Sheet.get_officials()
	return jsonify({"message": "officals updated in the database"})