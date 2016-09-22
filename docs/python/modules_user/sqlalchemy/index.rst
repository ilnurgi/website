.. py:module:: sqlalchemy

sqlalchemy
==========

.. code-block:: py

    import sqlalchemy as sa

    conn = sa.create_engine("sqlite://")
    conn.execute(create_table_sql)
    conn.execute(insert_sql)
    rows = conn.execute(select_sql)
    for row in rows:
        print(row)

.. code-block:: py

    import sqlalchemy as sa

    conn = sa.create_engine("sqlite://")
    meta = sa.MetaData()
    some_table = sa.Table(
        'table_name',
        meta,
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("count", sa.Integer),
    )

    meta.create_all(conn)

    conn.execute(some_table.insert((1, 1)))
    conn.execute(some_table.select())
    rows = conn.fetchall()

.. code-block:: py

    import sqlalchemy as sa
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker

    conn = sa.create_engine("sqlite://")
    Base = declarative_base()

    class SomeTable(Base):
        __tablename__ = 'table_name'
        id = sa.Column('id', sa.Integer, primary_key=True)
        count = sa.Column('count', sa.Integer)

        def __init__(self, id, count):
            self.id = id
            self.count = count

        def __repr__(self):
            return "<SomeTable({}, {})>".format(self.id, self.count)

    Base.metadata.create_all(conn)

    Session = sessionmaker(bind=conn)
    session = Session()
    session.add(SomeTable(1, 1))
    session.add_all((SomeTable(1, 1), SomeTable(2, 2)))
    session.commit()