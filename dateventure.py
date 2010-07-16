from google.appengine.ext import db
from google.appengine.ext import search
from google.appengine.api import users
K_ytt_j_Sukupuolis=('Mies','Nainen','En kerro')
alignment=('Mies','Nainen','En kerro')


class ilmoitus(search.SearchableModel):
    global alignment
    Olen = db.StringProperty(choices=alignment)
    Paikka = db.StringProperty()
    P_iv_m_r_Aika = db.DateTimeProperty()
    Kuvaus = db.StringProperty()
    Vastattu = db.BooleanProperty(default=False)
    vKuvaus = db.StringProperty()
    Ilmoittaja = db.UserProperty(auto_current_user=True, required=True)
    Vastaaja = db.UserProperty()
    Age = db.IntegerProperty(default=0)

      
class palaute(search.SearchableModel):
    # Palautteen lahettajan tiedot
    sukupuoli = db.StringProperty(choices=K_ytt_j_Sukupuolis)
    ika = db.IntegerProperty()

    # Palautteen osat
    kayttaisitko = db.BooleanProperty()
    hyodyllisyys = db.StringProperty(multiline=True)
    hyodyllisyysRating = db.IntegerProperty()
    kaytettavyys = db.StringProperty(multiline=True)
    kaytettavyysRating = db.IntegerProperty()
    vapaaSana = db.StringProperty(multiline=True)


    date = db.DateTimeProperty(auto_now_add=True)


    

#class selaus(search.SearchableModel):
#    Lookup_1 = db.ReferenceProperty(ilmoitus,collection_name="selaus_1_set")
