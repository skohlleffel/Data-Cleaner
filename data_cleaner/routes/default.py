from flask import render_template, request, Response, Blueprint
from data_cleaner.cleaning.cleaner import get_cleaned_file

#==============================================================================
# default API 
#==============================================================================
# define namespace
bp = Blueprint('default', __name__)


@bp.route('/', methods=['GET'])
def get_data():
    """default get handler"""

    return render_template('clean.html', title='Cleaner')


@bp.route('/', methods=['POST'])
def post_data():
    """default post handler"""

    try:
        req        = request.form
        path       = request.files['path']
        cap_list   = req.getlist('cap_list')
        num_list   = req.getlist('num_list')
        email_list = req.getlist('email_list')
        part_list  = req.getlist('part_list')
        drop_list  = req.getlist('drop_list')
        cleaned_page = get_cleaned_file(path=path, capitalize_list=cap_list, numeric_list=num_list, email_list=email_list, partners_list=part_list, drop_empty_list=drop_list)

    except Exception as e:
        print(e)
        error = e
        return render_template('clean.html', title='Error Occurred', error=error)

    return Response(cleaned_page, mimetype='text/csv')
#==============================================================================