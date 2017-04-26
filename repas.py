__author__ = 'desilvsa'
template=Import('/site_web/template.py')


def nos_repas():
    repas = '''<div class="section mcontainer">
                        <h2>Service nourriture</h2>
                        <div class="row">
                            <div class="col s12 m4">
                                <div class="card hoverable">
                                    <div class="card-image">
                                        <img src="/site_web/assets/imgs/hotdog.jpg">
                                        <a class="btn-floating btn-large halfway-fab waves-effect waves-light red"><i class="material-icons">shopping_cart</i></a>
                                    </div>
                                    <div class="card-content">
                                        <span class="card-title">Hot dog</span>
                                        <p>Un délicieux hot dog fait maison !</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col s12 m4">
                                <div class="card hoverable">
                                    <div class="card-image">
                                        <img src="/site_web/assets/imgs/hotdog.jpg">
                                        <a class="btn-floating btn-large halfway-fab waves-effect waves-light red"><i class="material-icons">shopping_cart</i></a>
                                    </div>
                                    <div class="card-content">
                                        <span class="card-title">Hot dog</span>
                                        <p>Un délicieux hot dog fait maison !</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col s12 m4">
                                <div class="card hoverable">
                                    <div class="card-image">
                                        <img src="/site_web/assets/imgs/hotdog.jpg">
                                        <a class="btn-floating btn-large halfway-fab waves-effect waves-light red"><i class="material-icons">shopping_cart</i></a>
                                    </div>
                                    <div class="card-content">
                                        <span class="card-title">Hot dog</span>
                                        <p>Un délicieux hot dog fait maison !</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>'''
    return repas


def repas():
    result = template.entete('Repas')
    result += template.nav()
    result += nos_repas()
    result += template.footer()
    return result