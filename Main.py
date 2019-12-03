from linkpy import Linky, LinkyLoginException, LinkyServiceException
import datetime
from dateutil.relativedelta import relativedelta

def get_data_daily(deb,fin):
    try:

        res_hour = linky.get_data_per_hour(deb, fin)

        dte_deb=datetime.datetime.strptime(res_hour['graphe']['periode']['dateDebut'], "%d/%m/%Y")
        dte_current=dte_deb
        for point in res_hour['graphe']['data']:
            print(dte_current.strftime("%d/%m/%Y  %H:%M:%S")+';'+str(point['ordre'])+';'+str(point['valeur']/2))
            dte_current=dte_current+relativedelta(minutes=30)

    except LinkyLoginException as exc:
        logging.error(exc)

    except LinkyServiceException as exc:
        logging.error(exc)

#main
linky = Linky()
linky.login(USER, PASS) # Ici, log (email) et mot de passe de votre compte Enedis

date_deb=datetime.datetime(2019,11,1) # ici les dates de début et de fin de la période que vous voulez exporter
date_fin=datetime.datetime(2019,11,30)

print("Date;ordre;cons")

while date_deb<=date_fin:
    get_data_daily(date_deb.strftime("%d/%m/%Y"),(date_deb+relativedelta(days=1)).strftime("%d/%m/%Y"))
    date_deb=date_deb+relativedelta(days=1)
