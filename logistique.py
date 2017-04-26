__author__ = 'desilvsa'
template=Import('/site_web/template.py')


def membres():
    membres = '''<div class="section mcontainer">
                    <h2 >Pôle communication</h2>
                    <div class="row">
                        <div class="col s12 m3 membre">
                            <img class="circle img-responsive" src="../assets/imgs/papotto.jpg">
                            <div class="nom">Lucas Papotto</div>
                            <div class="titre">Biatch</div>
                        </div>
                        <div class="col s12 m3 membre">
                            <img class="circle img-responsive" src="../assets/imgs/papotto.jpg">
                            <div class="nom">Lucas Papotto</div>
                            <div class="titre">Biatch</div>
                        </div>
                        <div class="col s12 m3 membre">
                            <img class="circle img-responsive" src="../assets/imgs/papotto.jpg">
                            <div class="nom">Lucas Papotto</div>
                            <div class="titre">Biatch</div>
                        </div>
                        <div class="col s12 m3 membre">
                            <img class="circle img-responsive" src="../assets/imgs/papotto.jpg">
                            <div class="nom">Lucas Papotto</div>
                            <div class="titre">Biatch</div>
                        </div>
                        <div class="col s12 m3 membre">
                            <img class="circle img-responsive" src="../assets/imgs/papotto.jpg">
                            <div class="nom">Lucas Papotto</div>
                            <div class="titre">Biatch</div>
                        </div>
                        <div class="col s12 m3 membre">
                            <img class="circle img-responsive" src="../assets/imgs/papotto.jpg">
                            <div class="nom">Lucas Papotto</div>
                            <div class="titre">Biatch</div>
                        </div>
                    </div>
                </div>'''
    return membres

def logistique():
    result = template.entete('Bureau')
    result+=template.nav()
    result+=membres()
    result+=template.footer()
    return result