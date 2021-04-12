from flask import request, abort


def get_param_convert():
    group_filter = ['SubscriptionName', 'Date',
                    'ServiceName', 'ServiceResource', 'PublicationDate']
    data_filter = {}

    if 'cost' in request.args and request.args.get('cost') == 'AllTime':
        return "Select ROUND(SUM(Cost),2) as 'CoutTotal' From period1;"
    elif request.args.get('cost') == 'AllTimeBySubscriptionName':
        return "Select SubscriptionName, ROUND(SUM(Cost),2) as 'CoutTotal' From period1 GROUP BY SubscriptionName;"

    for i in group_filter:
        if i in request.args:
            value = request.args.get(i)
            data_filter[i] = value.replace('%20', ' ') if (
                (value != None) and ('%20' in value)) else value

    if len(data_filter) > 0:
        return create_query_filter(data_filter)
    elif len(request.args) == 0:
        return None
    else:
        return abort(404)


def create_query_filter(dict_query_filter):
    part_1_query = 'Select SubscriptionName, PublicationDate, '
    part_2_query = "ROUND(SUM(Cost),2) as 'CoutTotal' From period1 WHERE "
    for key, value in enumerate(dict_query_filter):
        part_1_query += f'{value}, ' if (
            value != 'PublicationDate' or value != 'SubscriptionName') else None
        part_2_query += f"{value} = '{dict_query_filter[value]}' " if (key == (
            len(dict_query_filter)-1)) else f"{value} = '{dict_query_filter[value]}' AND "
    query_filter = f'{part_1_query}{part_2_query} GROUP BY SubscriptionName, PublicationDate;'
    return query_filter
