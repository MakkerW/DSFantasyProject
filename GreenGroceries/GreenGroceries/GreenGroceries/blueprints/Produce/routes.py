from flask import render_template, request, Blueprint
from flask_login import login_required, current_user

from GreenGroceries.forms import FilterProduceForm
from GreenGroceries.models import Produce as ProduceModel, ProduceOrder
from GreenGroceries.queries import insert_produce, get_produce_by_pk, Sell, \
    insert_sell, get_all_produce_by_farmer, get_produce_by_filters, insert_produce_order, update_sell, \
    get_orders_by_customer_pk

Produce = Blueprint('Produce', __name__)


@Produce.route("/produce", methods=['GET', 'POST'])
def produce():
    form = FilterProduceForm()
    title = 'Our produce!'
    produce = []

    if request.method == 'POST':
        produce = get_produce_by_filters(full_name=request.form.get('full_name').capitalize(),
                                         GW=request.form.get('GW'),
                                         goals_scored=request.form.get('goals_scored'),
                                         assists=request.form.get('assists'),
                                         total_points=request.form.get('total_points')

                                         )
        print(request.form.get('GW'))
        title = 'FPL query tool'
    return render_template('pages/produce.html', produce=produce, form=form, title=title, GW=request.form.get('GW'))




