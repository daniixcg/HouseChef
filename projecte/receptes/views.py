from django.shortcuts import render

def receptes(request):
    # Array de receptes que es passen al template per renderitzar dinàmicament
    receptes_llista = [
        {
            'nom': 'Paella Valenciana',
            'imatge': 'paella_valenciana.jpg',
            'ingredients': [
                '350g d\'arròs',
                '500g de conill',
                '150g de mongetes verdes',
                '1 litre de caldo de pollastre',
                'Sàfrana',
                'Oli d\'oliva',
                'Sal i pebre',
            ],
            'passos': [
                'Talla el conill en trossos i sofregeix-lo en oli calent',
                'Afegeix les mongetes verdes i deixa coure 5 minuts',
                'Versa l\'arròs i remena\'s bé',
                'Afegeix el caldo calent amb la sàfrana',
                'Deixa coure a foc viu 15 minuts sense remoure',
                'Baixa el foc i deixa coure 10 minuts més fins que l\'arròs estigui tendre',
            ]
        },
        {
            'nom': 'Crema Catalana',
            'imatge': 'crema_catalana.jpg',
            'ingredients': [
                '500ml de llet',
                '1 rajola de canella',
                'Pell de llimona',
                '4 rovells d\'ou',
                '25g de farina',
                '50g de sucre',
                'Sucre per gratinar',
            ],
            'passos': [
                'Escalfa la llet amb la canella i la pell de llimona',
                'Bat els rovells amb sucre fins que quedin pàl·lids',
                'Afegeix la farina als rovells i remena bé',
                'Versa la llet calenta sobre la barreja de rovells',
                'Torna a bullir sense deixar de remoure fins que s\'espesseixi',
                'Versa en plats de cremat i deixa refredar',
                'Saupeja sucre per sobre i caramelitza amb una cullera calenta',
            ]
        },
        {
            'nom': 'Fideuà',
            'imatge': 'fideua.jpg',
            'ingredients': [
                '350g de fideus',
                '400g de camarons',
                '300g de peix blanc',
                '1 litre de caldo de peix',
                'Sàfrana',
                '4 dents d\'all',
                'Oli d\'oliva i sal',
            ],
            'passos': [
                'Sofregeix l\'all picado en la paellera amb oli',
                'Afegeix el peix trencat en trossos i deixa coure 3 minuts',
                'Versa els fideus i remena fins que estiguin dorats',
                'Afegeix el caldo calent amb la sàfrana',
                'Deixa coure 12 minuts sense remoure',
                'Afegeix els camarons els últims 2 minuts',
                'Apaga el foc i deixa reposar 2 minuts',
            ]
        },
        {
            'nom': 'Tiramisu',
            'imatge': 'tiramisu.jpg',
            'ingredients': [
                '500g de mascarpone',
                '4 rovells d\'ou',
                '100g de sucre',
                '300ml de cafè fort',
                '40 bessuons de xocolata',
                'Cacao en pols',
                'Licor de café (opcional)',
            ],
            'passos': [
                'Bat els rovells amb sucre fins que quedin pàl·lids i esponjosos',
                'Afegeix el mascarpone en porcions petites remenant amb suavitat',
                'Barreja el cafè amb el licor de café si vols',
                'Mulla els bessuons en el cafè i col·loca\'ls en una capa a la base',
                'Afegeix una capa de crema de mascarpone',
                'Repeteix les capes fins acabar',
                'Refrigera almenys 4 hores',
                'Saupeja cacao en pols abans de servir',
            ]
        },
        {
            'nom': 'Gazpacho Andalús',
            'imatge': 'gazpacho.jpg',
            'ingredients': [
                '1kg de tomàquets maduros',
                '1 pimentó roig',
                '1 cogombre',
                '1 trosset de pa blanc',
                '3 cullerades d\'oli d\'oliva',
                '1 cullera de vinagre de xérès',
                'Sal i aigua freda',
            ],
            'passos': [
                'Talla els tomàquets, el pimentó i el cogombre en trossos',
                'Remulla el pa en una mica d\'aigua',
                'Posa tot en una trituradora o robot de cuina',
                'Afegeix oli, vinagre i sal',
                'Tritura fins obtenir una textura suau',
                'Afegeix aigua freda segons la consistència desitjada',
                'Refrigera almenys 2 hores',
                'Serveix bé fred',
            ]
        },
        {
            'nom': 'Canelons de la Casa',
            'imatge': 'canelons.jpg',
            'ingredients': [
                '24 plaques de canelons',
                '500g de carn de porc picada',
                '500g de carn de vedella picada',
                '1 ceba',
                'Beixamel (llet, farina, mantega)',
                'Formatge rellat',
                'Sal, pebre i nous moscada',
            ],
            'passos': [
                'Sofregeix la ceba picada en oli',
                'Afegeix la carn picada i deixa coure fins que es dori',
                'Prepara la beixamel i barreja amb la carn',
                'Cueix els canelons segons les instruccions del paquet',
                'Omple els canelons amb la barreja de carn',
                'Col·loca\'ls en una placa besada amb oli',
                'Cobreix amb més beixamel i formatge rellat',
                'Cou al forn a 180ºC durant 30 minuts',
            ]
        },
    ]
    
    # Passa les receptes al context per ser renderitzades al template
    context = {
        'receptes': receptes_llista
    }
    return render(request, 'receptes.html', context)
