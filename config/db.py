from  sqlalchemy import create_engine, MetaData
#ngine = create_engine("mysql://scott:tiger@localhost/foo")
engine = create_engine("mysql+pymysql://root:@localhost:3306/youstore")

conn = engine.connect()

meta_data = MetaData()