Avant de commencer : pip install -r requirements.txt

GET /api/chambres/disponibles : Renvoie la liste des chambres disponibles pour les dates spécifiées dans les paramètres de requête date_arrivee et date_depart.

POST /api/reservations : Crée une nouvelle réservation avec les détails fournis dans le corps de la requête au format JSON.

DELETE /api/reservations/<id> : Annule la réservation correspondant à l'identifiant spécifié dans l'URL.

POST /api/chambres : Ajoute une nouvelle chambre avec les détails fournis dans le corps de la requête au format JSON.

PUT /api/chambres/<id> : Met à jour les détails de la chambre correspondant à l'identifiant spécifié dans l'URL avec les données fournies dans le corps de la requête au format JSON.

DELETE /api/chambres/<id> : Supprime la chambre correspondant à l'identifiant spécifié dans l'URL.