from spyre import server
server.include_df_index = True # for displaying the index of a dataframe. Very useful in displaying time-series data

import psycopg2
from psycopg2.extras import RealDictCursor
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

class ListingDecayApp(server.App):
    title = "Listing Decay Dashboard"
    inputs = [#{"input_type":"dropdown",
    #            "options":[ {"label" : "ldf_logs", "value" : "ldf_logs"},
    #                        {"label" : "ldf_actions", "value" : "ldf_actions"},
    #                        {"label" : "ldf_channels", "value" : "ldf_channels"}],
    #            "variable_name" : "psqltable",
    #            "action_id":"update_data"},
               {"input_type":"text",
                "variable_name":"numRows",
                "value":5,
                "action_id":"update_data"}
               # {"input_type":"slider",
               #  #"label": '# of records', 
               #  "min" : 10,
               #  "max" : 100,
               #  "value" : 50,
               #  "variable_name": "numRows", 
               #  "action_id": "update_data"}
               ]

    controls = [{"control_type" : "button",
                 "label" : "Show data",
                 "control_id" : "update_data"}]

    tabs = ["Tables", "Plots"]

    outputs = [{"output_type":"table",
                "output_id":"logs_table",
                "tab" : "Tables",
                "control_id" : "update_data",
                "on_page_load":True},
               {"output_type" : "plot",
                "output_id" : "plot",
                "control_id" : "update_data",
                "tab" : "Plots",
                "on_page_load" :True}]
    
    def getPlot(self, params):
        f = float(params['numRows'])
        x = np.arange(0,2*np.pi,np.pi/150)
        y = np.sin(f*x)
        fig = plt.figure()
        splt1 = fig.add_subplot(1,1,1)
        splt1.plot(x,y)
        return fig

    def getData(self, params):
        numRows = params['numRows']
        #reqTable = params['psqltable']

        df = pd.DataFrame(fetch_email_response_data(numRows))
        return df

    
def db_connect():
    ''' Create a connection to the database'''
    conn_string = '''host=127.0.0.1 dbname=housing_analytics user=dsl_readonly password=dsl port=5434''' # housing analytics
    conn_string = '''host=127.0.0.1 dbname=housing_production user=housing password=housing port=5433''' # productiondb
    conn = psycopg2.connect(conn_string)
    pgcur = conn.cursor()
    pgcur.execute('''set search_path to public,postgis''')
    return conn

def fetch_email_response_data(numRows):
    '''Fetch email response logs'''
    conn = db_connect()
    pgcur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    query = "SELECT * from ((SELECT t3.*, owners.name as listing_owner_name, owners.email_id as listing_owner_email FROM (SELECT max(act_date) as recent_act_date, t2.deact_date, t2.listing_id, t2.listing_owner_type, t2.city, t2.locality, t2.url, t2.apt_type, t2.ppty_type, t2.usr_id, t2.usr_profile_id, t2.usr_phone_no, t2.usr_email FROM (SELECT date(logs.created_at) AS act_date, t1.* FROM (SELECT date(logs.created_at) AS deact_date, logs.listings_id AS listing_id, usr.profile_type AS listing_owner_type, cities.name AS city, localities.name AS locality, rf.canonical_url AS url, apt_type.name AS apt_type, ppty_type.name AS ppty_type, usr.id AS usr_id, usr.profile_id AS usr_profile_id, usr.contact_no AS usr_phone_no, usr.email AS usr_email FROM logs, rent_flats_linked_users rflu, users usr, apartment_types apt_type, property_types ppty_type, rent_flats rf, localities, cities, regions WHERE logs.action=3 AND logs.message LIKE '%ldf%multiple%reports%' AND logs.listings_type='RentFlat' AND logs.listings_id=rflu.rent_flat_id AND rflu.user_id=usr.id AND logs.listings_id=rf.id AND rf.locality_id=localities.id AND localities.region_id=regions.id AND regions.city_id=cities.id AND rf.apartment_type_id=apt_type.id AND rf.property_type_id=ppty_type.id AND date(logs.created_at)>=current_date-7 AND date(logs.created_at)<=current_date-1 ) AS t1, logs WHERE t1.listing_id=logs.listings_id AND logs.action=2 AND logs.listings_type='RentFlat' AND date(logs.created_at)<t1.deact_date ) AS t2 GROUP BY t2.deact_date, t2.listing_id, t2.listing_owner_type, t2.city, t2.locality, t2.url, t2.apt_type, t2.ppty_type, t2.usr_id, t2.usr_profile_id, t2.usr_phone_no, t2.usr_email) AS t3, owners WHERE t3.listing_owner_type='Owner' AND t3.usr_profile_id=owners.id) UNION ALL (SELECT t3.*, brokers.name as listing_owner_name, brokers.email_id as listing_owner_email FROM (SELECT max(act_date) as recent_act_date, t2.deact_date, t2.listing_id, t2.listing_owner_type, t2.city, t2.locality, t2.url, t2.apt_type, t2.ppty_type, t2.usr_id, t2.usr_profile_id, t2.usr_phone_no, t2.usr_email FROM (SELECT date(logs.created_at) AS act_date, t1.* FROM (SELECT date(logs.created_at) AS deact_date, logs.listings_id AS listing_id, usr.profile_type AS listing_owner_type, cities.name AS city, localities.name AS locality, rf.canonical_url AS url, apt_type.name AS apt_type, ppty_type.name AS ppty_type, usr.id AS usr_id, usr.profile_id AS usr_profile_id, usr.contact_no AS usr_phone_no, usr.email AS usr_email FROM logs, rent_flats_linked_users rflu, users usr, apartment_types apt_type, property_types ppty_type, rent_flats rf, localities, cities, regions WHERE logs.action=3 AND logs.message LIKE '%ldf%multiple%reports%' AND logs.listings_type='RentFlat' AND logs.listings_id=rflu.rent_flat_id AND rflu.user_id=usr.id AND logs.listings_id=rf.id AND rf.locality_id=localities.id AND localities.region_id=regions.id AND regions.city_id=cities.id AND rf.apartment_type_id=apt_type.id AND rf.property_type_id=ppty_type.id AND date(logs.created_at)>=current_date-7 AND date(logs.created_at)<=current_date-1 ) AS t1, logs WHERE t1.listing_id=logs.listings_id AND logs.action=2 AND logs.listings_type='RentFlat' AND date(logs.created_at)<t1.deact_date ) AS t2 GROUP BY t2.deact_date, t2.listing_id, t2.listing_owner_type, t2.city, t2.locality, t2.url, t2.apt_type, t2.ppty_type, t2.usr_id, t2.usr_profile_id, t2.usr_phone_no, t2.usr_email) AS t3, brokers WHERE t3.listing_owner_type='Broker' AND t3.usr_profile_id=brokers.id)) as ft ORDER BY deact_date desc, usr_phone_no asc limit " + str(numRows)
    query = "SELECT t1.* FROM(SELECT date(logs.created_at) AS deact_date, logs.listings_id AS listing_id, usr.profile_type AS listing_owner_type, cities.name AS city, localities.name AS locality, rf.canonical_url AS url, apt_type.name AS apt_type, ppty_type.name AS ppty_type, usr.id AS usr_id, usr.profile_id AS usr_profile_id, usr.contact_no AS usr_phone_no, usr.email AS usr_email FROM logs, rent_flats_linked_users rflu, users usr, apartment_types apt_type, property_types ppty_type, rent_flats rf, localities, cities, regions WHERE logs.action=3 AND logs.message LIKE '%ldf%multiple%reports%' AND logs.listings_type in ('RentFlat','BuyFlat') AND logs.listings_id=rflu.rent_flat_id AND rflu.user_id=usr.id AND logs.listings_id=rf.id AND rf.locality_id=localities.id AND localities.region_id=regions.id AND regions.city_id=cities.id AND rf.apartment_type_id=apt_type.id AND rf.property_type_id=ppty_type.id AND date(logs.created_at)>=current_date-7 AND date(logs.created_at)<=current_date-1 ) AS t1 limit 5";
    query = "SELECT t3.*, owners.name as listing_owner_name, owners.email_id as listing_owner_email FROM (SELECT max(act_date) as recent_act_date, t2.deact_date, t2.listing_id, t2.listing_owner_type, t2.city, t2.locality, t2.url, t2.apt_type, t2.ppty_type, t2.usr_id, t2.usr_profile_id, t2.usr_phone_no, t2.usr_email FROM (SELECT date(logs.created_at) AS act_date, t1.* FROM (SELECT date(logs.created_at) AS deact_date, logs.listings_id AS listing_id, usr.profile_type AS listing_owner_type, cities.name AS city, localities.name AS locality, rf.canonical_url AS url, apt_type.name AS apt_type, ppty_type.name AS ppty_type, usr.id AS usr_id, usr.profile_id AS usr_profile_id, usr.contact_no AS usr_phone_no, usr.email AS usr_email FROM logs, rent_flats_linked_users rflu, users usr, apartment_types apt_type, property_types ppty_type, rent_flats rf, localities, cities, regions WHERE logs.action=3 AND logs.message LIKE '%ldf%multiple%reports%' AND logs.listings_type='RentFlat' AND logs.listings_id=rflu.rent_flat_id AND rflu.user_id=usr.id AND logs.listings_id=rf.id AND rf.locality_id=localities.id AND localities.region_id=regions.id AND regions.city_id=cities.id AND rf.apartment_type_id=apt_type.id AND rf.property_type_id=ppty_type.id AND date(logs.created_at)>=current_date-7 AND date(logs.created_at)<=current_date-1 ) AS t1, logs WHERE t1.listing_id=logs.listings_id AND logs.action=2 AND logs.listings_type='RentFlat' AND date(logs.created_at)<t1.deact_date ) AS t2 GROUP BY t2.deact_date, t2.listing_id, t2.listing_owner_type, t2.city, t2.locality, t2.url, t2.apt_type, t2.ppty_type, t2.usr_id, t2.usr_profile_id, t2.usr_phone_no, t2.usr_email) AS t3, owners WHERE t3.listing_owner_type='Owner' AND t3.usr_profile_id=owners.id"
    query = "SELECT * from ((SELECT t3.*, owners.name as listing_owner_name, owners.email_id as listing_owner_email FROM (SELECT max(act_date) as recent_act_date, t2.deact_date, t2.listing_id, t2.listings_type, t2.listing_owner_type, t2.city, t2.locality, t2.url, t2.apt_type, t2.ppty_type, t2.usr_id, t2.usr_profile_id, t2.usr_phone_no, t2.usr_email FROM (SELECT date(logs.created_at) AS act_date, t1.* FROM (SELECT date(logs.created_at) AS deact_date, logs.listings_id AS listing_id, logs.listings_type AS listings_type, usr.profile_type AS listing_owner_type, cities.name AS city, localities.name AS locality, rf.canonical_url AS url, apt_type.name AS apt_type, ppty_type.name AS ppty_type, usr.id AS usr_id, usr.profile_id AS usr_profile_id, usr.contact_no AS usr_phone_no, usr.email AS usr_email FROM logs, rent_flats_linked_users rflu, users usr, apartment_types apt_type, property_types ppty_type, rent_flats rf, localities, cities, regions WHERE logs.action=3 AND logs.message LIKE '%ldf%multiple%reports%' AND logs.listings_type='RentFlat' AND logs.listings_id=rflu.rent_flat_id AND rflu.user_id=usr.id AND logs.listings_id=rf.id AND rf.locality_id=localities.id AND localities.region_id=regions.id AND regions.city_id=cities.id AND rf.apartment_type_id=apt_type.id AND rf.property_type_id=ppty_type.id AND date(logs.created_at)>=current_date-7 AND date(logs.created_at)<=current_date-1 ) AS t1, logs WHERE t1.listing_id=logs.listings_id AND logs.action=2 AND logs.listings_type='RentFlat' AND date(logs.created_at)<t1.deact_date ) AS t2 GROUP BY t2.deact_date, t2.listing_id, t2.listings_type, t2.listing_owner_type, t2.city, t2.locality, t2.url, t2.apt_type, t2.ppty_type, t2.usr_id, t2.usr_profile_id, t2.usr_phone_no, t2.usr_email) AS t3, owners WHERE t3.listing_owner_type='Owner' AND t3.usr_profile_id=owners.id) UNION ALL (SELECT t3.*, owners.name as listing_owner_name, owners.email_id as listing_owner_email FROM (SELECT max(act_date) as recent_act_date, t2.deact_date, t2.listing_id, t2.listings_type, t2.listing_owner_type, t2.city, t2.locality, t2.url, t2.apt_type, t2.ppty_type, t2.usr_id, t2.usr_profile_id, t2.usr_phone_no, t2.usr_email FROM (SELECT date(logs.created_at) AS act_date, t1.* FROM (SELECT date(logs.created_at) AS deact_date, logs.listings_id AS listing_id, logs.listings_type AS listings_type, usr.profile_type AS listing_owner_type, cities.name AS city, localities.name AS locality, bf.canonical_url AS url, apt_type.name AS apt_type, ppty_type.name AS ppty_type, usr.id AS usr_id, usr.profile_id AS usr_profile_id, usr.contact_no AS usr_phone_no, usr.email AS usr_email FROM logs, user_buy_flats ubf, users usr, apartment_types apt_type, property_types ppty_type, buy_flats bf, localities, cities, regions WHERE logs.action=3 AND logs.message LIKE '%ldf%multiple%reports%' AND logs.listings_type='BuyFlat' AND logs.listings_id= ubf.buy_flat_id AND ubf.user_id=usr.id AND logs.listings_id=bf.id AND bf.locality_id=localities.id AND localities.region_id=regions.id AND regions.city_id=cities.id AND bf.apartment_type_id=apt_type.id AND bf.property_type_id=ppty_type.id AND date(logs.created_at)>=current_date-7 AND date(logs.created_at)<=current_date-1 ) AS t1, logs WHERE t1.listing_id=logs.listings_id AND logs.action=2 AND logs.listings_type='BuyFlat' AND date(logs.created_at)<t1.deact_date ) AS t2 GROUP BY t2.deact_date, t2.listing_id, t2.listings_type, t2.listing_owner_type, t2.city, t2.locality, t2.url, t2.apt_type, t2.ppty_type, t2.usr_id, t2.usr_profile_id, t2.usr_phone_no, t2.usr_email) AS t3, owners WHERE t3.listing_owner_type='Owner' AND t3.usr_profile_id=owners.id)) as ft ORDER BY deact_date desc, usr_phone_no asc limit %s;" % (numRows)
    pgcur.execute(query)
    results = pgcur.fetchall()
    return results

if __name__ == "__main__":
    app = ListingDecayApp()
    app.launch(host = "localhost", port = 8080) # use host = "0.0.0.0" for external access