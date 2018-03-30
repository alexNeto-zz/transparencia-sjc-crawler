import sqlalchemy


class DatabaseCommunication:
    """
    Classe par criar comunicação com banco de dados
    Apenas 1 conecção para o projeto
    """

    class __DatabaseCommunication:
        def __init__(self):
            self.user = "transparencia"
            self.password = "postgres123"
            self.database = "transparencia_development"
            self.host = "localhost"
            self.port = 5432

        def __str__(self):
            return repr(self)

    instance = None

    def __init__(self):
        if not DatabaseCommunication.instance:
            DatabaseCommunication.instance = DatabaseCommunication.__DatabaseCommunication()

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def connect(self):
        url = 'postgresql+psycopg2://{}:{}@{}:{}/{}'
        url = url.format(self.user, self.password, self.host, self.port, self.database)
        con = sqlalchemy.create_engine(url)
        meta = sqlalchemy.MetaData(bind=con, reflect=True)

        return con, meta
