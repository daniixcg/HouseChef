"""
Vistes de l'aplicació 'faqs'
Gestiona les preguntes freqüents del siti.
"""

from django.shortcuts import render

def preguntes_frequents(request):
    """
    Vista de preguntes freqüents.
    Renderitza la pàgina FAQs amb dades dinàmiques.
    
    Args:
        request: HttpRequest object
        
    Returns:
        HttpResponse: Renderitza template 'faqs.html'
    """
    preguntes = [
        {
            'pregunta': 'Quant tarda en donar-se d\'alta a HouseChef?',
            'resposta': 'El procés de registre és molt simple i només tarda uns minuts. Necessites proporcionar el teu nom, correu electrònic i una contrasenya. Una vegada completat, tindràs accés immediat a tots els recursos de la comunitat HouseChef.'
        },
        {
            'pregunta': 'Quin és el cost de pertànyer a HouseChef?',
            'resposta': 'HouseChef és completament gratuït! No hi ha cap cost de membresia. Pots gaudir de totes les funcionalitats de la comunitat, compartir receptes, interactuar amb altres membres i accedir a continguts exclusius sense pagar res.'
        },
        {
            'pregunta': 'A on puc dirigir-me si tinc un dubte o problema?',
            'resposta': 'Tens diverses opcions per contactar amb nosaltres. Pots enviar una petició a través de la secció de "Peticions i Sugerències", contactar-nos per correu electrònic o enviar un missatge privat als administradors. Sempre intentarem resoldre\'n els teus dubtes el més aviat possible.'
        },
        {
            'pregunta': 'Puc donar-me de baixa en qualsevol moment?',
            'resposta': 'Sí, pots donar-te de baixa en qualsevol moment sense cap problema ni penalització. Simplement accedeix a la configuració del teu compte i selecciona l\'opció de donar-te de baixa. Els teus dades es conservaran segons la nostra política de privacitat.'
        },
        {
            'pregunta': 'Puc compartir les meves receptes a HouseChef?',
            'resposta': 'Per supuest! Un dels objectius principals de HouseChef és compartir receptes i experiències culinàries. Pots publicar les teves receptes, afegir fotos, descripcions detallades i tutorials. Anima\'t a compartir la teva passió per la cuina amb tota la comunitat.'
        },
        {
            'pregunta': 'Com puc recuperar la meva contrasenya?',
            'resposta': 'Si has oblidat la contrasenya, accedeix a la pàgina d\'inici de sessió i fes clic en "He oblidat la contrasenya". Et sent un enllaç de recuperació al teu correu electrònic. Fes clic en l\'enllaç i crea una contrasenya nova.'
        },
        {
            'pregunta': 'La comunitat és segura i privada?',
            'resposta': 'Sí, la privacitat i seguretat dels nostres membres és prioritat. Utilitzem encriptació moderna per protegir les teves dades. Les teves dades personals mai es compartiran amb tercers sense el teu consentiment. Pots consultar la nostra política de privacitat per més detalls.'
        },
        {
            'pregunta': 'Puc participar en concursos o activitats comunitàries?',
            'resposta': 'Sí! HouseChef regularment organitza concursos de receptes, desafiaments culinaris i activitats comunitàries. Tots els membres registrats poden participar. Prest anunciarem els propers concursos a la pàgina d\'inici. Mantingues\'t atent!'
        },
    ]
    
    context = {
        'preguntes': preguntes
    }
    return render(request, 'faqs.html', context)
