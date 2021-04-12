from flask import request, abort


def get_param_convert():
    if 'cost' in request.args:
        return get_all_data_for_all_time()
    return get_data_by_params()


def get_all_data_for_all_time():
    if (request.args.get('cost') == 'AllTime' and len(request.args) == 1):
        return "Select ROUND(SUM(Cost),2) as 'CoutTotal' From period1;"
    elif (request.args.get('cost') == 'AllTimeBySubscriptionName' and len(request.args) == 1):
        return "Select SubscriptionName, ROUND(SUM(Cost),2) as 'CoutTotal' From period1 GROUP BY SubscriptionName;"
    return abort(404)


def get_data_by_params():
    group_filter = ['SubscriptionName', 'Date',
                    'ServiceName', 'ServiceResource', 'PublicationDate']
    data_filter = {}

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
