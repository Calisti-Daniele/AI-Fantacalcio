# previsione_miglior_team.py

class PrevisioneMigliorTeam:
    def __init__(self, nome, ruolo, media_voto, squadra, assist=0, goal_fatti=0, ammonizioni=0, espulsioni=0):
        self._idPrevisioneMigliorTeam = None  # Auto-incrementato dal DB
        self._nome = nome
        self._ruolo = ruolo
        self._media_voto = media_voto
        self._squadra = squadra
        self._assist = assist
        self._goal_fatti = goal_fatti
        self._ammonizioni = ammonizioni
        self._espulsioni = espulsioni

    # Getter e Setter per idPrevisioneMigliorTeam
    @property
    def idPrevisioneMigliorTeam(self):
        return self._idPrevisioneMigliorTeam

    @idPrevisioneMigliorTeam.setter
    def idPrevisioneMigliorTeam(self, value):
        self._idPrevisioneMigliorTeam = value

    # Getter e Setter per nome
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    # Getter e Setter per ruolo
    @property
    def ruolo(self):
        return self._ruolo

    @ruolo.setter
    def ruolo(self, value):
        self._ruolo = value

    # Getter e Setter per media_voto
    @property
    def media_voto(self):
        return self._media_voto

    @media_voto.setter
    def media_voto(self, value):
        self._media_voto = value

    # Getter e Setter per squadra
    @property
    def squadra(self):
        return self._squadra

    @squadra.setter
    def squadra(self, value):
        self._squadra = value

    # Getter e Setter per assist
    @property
    def assist(self):
        return self._assist

    @assist.setter
    def assist(self, value):
        self._assist = value

    # Getter e Setter per goal_fatti
    @property
    def goal_fatti(self):
        return self._goal_fatti

    @goal_fatti.setter
    def goal_fatti(self, value):
        self._goal_fatti = value

    # Getter e Setter per ammonizioni
    @property
    def ammonizioni(self):
        return self._ammonizioni

    @ammonizioni.setter
    def ammonizioni(self, value):
        self._ammonizioni = value

    # Getter e Setter per espulsioni
    @property
    def espulsioni(self):
        return self._espulsioni

    @espulsioni.setter
    def espulsioni(self, value):
        self._espulsioni = value
