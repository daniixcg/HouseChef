from django.shortcuts import render

def inici(request):
    return render(request, 'home.html')

def galetes(request):
    # Dades de galetes estructurades amb seccions i subseccions per renderitzar dinàmicament
    seccions_galetes = [
        {
            'numero': '1',
            'titol': 'Introducció',
            'text': 'HouseChef utilitza galetes per millorar la teva experiència a la nostra plataforma. Aquesta política explica com utilitzem les galetes i com pots controlar-les.'
        },
        {
            'numero': '2',
            'titol': 'Què són les galetes?',
            'text': 'Les galetes són petits arxius de text que es desen al teu dispositiu quan visites un lloc web. Ajuden a recordar informació sobre tu i les teves preferències.'
        },
        {
            'numero': '3',
            'titol': 'Tipus de galetes que utilitzem',
            'subseccions': [
                {
                    'numero': '3.1',
                    'titol': 'Galetes essencials',
                    'text': 'Aquestes galetes són necessàries per al funcionament correcte de la plataforma. Include les que gestionen la seguretat i la sessió de l\'usuari.'
                },
                {
                    'numero': '3.2',
                    'titol': 'Galetes de preferència',
                    'text': 'Recordem les teves preferències i opcions, com l\'idioma o la configuració de visualització.'
                },
                {
                    'numero': '3.3',
                    'titol': 'Galetes analítiques',
                    'text': 'Ens ajuden a entendre com utilitzes la plataforma perquè puguem millorar-la.'
                },
                {
                    'numero': '3.4',
                    'titol': 'Galetes de màrqueting',
                    'text': 'Utilitzades per mostrar-te contingut més rellevant i personalitzat.'
                }
            ]
        },
        {
            'numero': '4',
            'titol': 'Com controlar les galetes',
            'text': 'Pots controlar o eliminar les galetes a través de la configuració del teu navegador. Si desactives les galetes essencials, és possible que alguns serveis no funcionin correctament.'
        },
        {
            'numero': '5',
            'titol': 'Galetes de tercers',
            'text': 'Alguns serveis de tercers, com les xarxes socials, també poden establir galetes al teu dispositiu. Consulta les seves polítiques de privacitat per més informació.'
        },
        {
            'numero': '6',
            'titol': 'Durada de les galetes',
            'text': 'Les galetes de sessió s\'eliminen quan tanques el navegador. Les galetes persistents es guarden fins que les eliminis o expirem.'
        },
        {
            'numero': '7',
            'titol': 'Contacte',
            'text': 'Si tens preguntes sobre la nostra política de galetes, envia\'ns una petició.'
        }
    ]
    
    # Context amb les seccions que es renderitzen amb un bucle al template
    context = {
        'seccions': seccions_galetes
    }
    return render(request, 'cookies.html', context)

def privacitat(request):
    return render(request, 'privacitat.html')

